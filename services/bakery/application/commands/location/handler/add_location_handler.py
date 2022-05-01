import psycopg2
import sqlalchemy.exc
from bson import ObjectId
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.location.add_location_command import AddLocationsCommand, AddLocationCommand
from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.entity import EntityOperationStatus
from bakery.domain.model.location import Location
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger
from shared.util.datetime import now


@Mediator.register_handler(AddLocationsCommand)
@singleton
class AddLocationsHandler:

    @inject
    def __init__(self, location_repository: EntityRepository, location_mapper: DTOMapper, logger: Logger,
                 mediator: Mediator):
        self._location_mapper = location_mapper
        self._location_repository = location_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, locations_command: AddLocationsCommand) -> None:
        """
        responsible for adding locations
        :param locations_command:
        :return:
        """
        self._logger.info("command received for add location")
        location_data = []
        for location_command in locations_command.locations_list:
            location_command: AddLocationCommand
            location = Location(id=str(ObjectId()), name=location_command.location_name,
                                description=location_command.location_description,
                                created_on=now(),
                                updated_on=now(),
                                created_by='626d38970b9eabe51bb35a65',
                                updated_by='626d38970b9eabe51bb35a65')
            location.operation_status = EntityOperationStatus.ADDED.value
            location_data.append(location)
        try:
            with self._location_repository.session_scope() as session:
                self._location_repository.add_entities(location_data, session=session)
            self._logger.info("command for add location completed successfully")
            return [self._location_mapper.map_location_dto(location) for location in location_data]
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                starts = str(e.orig.args).find("=") + 2
                ends = str(e.orig.args)[starts:].find(")")
                message = "location with name " + str(e.orig.args)[starts:starts + ends] + " already exist"
                raise BakeryException(message=message, status_code=HTTP_400_BAD_REQUEST)

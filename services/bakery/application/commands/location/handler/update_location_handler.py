import sqlalchemy.exc
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.location.update_location_command import UpdateLocationCommand
from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.dto.location_dto import LocationDTO
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.model.location import Location
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger


@Mediator.register_handler(UpdateLocationCommand)
@singleton
class UpdateLocationsHandler:

    @inject
    def __init__(self, location_repository: EntityRepository, logger: Logger, location_mapper: DTOMapper,
                 mediator: Mediator):
        self._location_mapper = location_mapper
        self._location_repository = location_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, location_command: UpdateLocationCommand) -> LocationDTO:
        self._logger.info("command received for update location")
        try:
            with self._location_repository.session_scope() as session:
                location = self._location_repository.get_entity(entity=Location,entity_id=location_command.location_id, session=session)
                if location:
                    location.name = location_command.location_name
                    location.description = location_command.location_description
                    # update updated by also
                    self._location_repository.update_entity(entity=location, session=session)
                    self._logger.info("command for update location completed successfully")
                    return self._location_mapper.map_location_dto(location)
                else:
                    raise BakeryException(message="Location not found", status_code=HTTP_400_BAD_REQUEST)
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                raise BakeryException(message="Location with this name already exist", status_code=HTTP_400_BAD_REQUEST)

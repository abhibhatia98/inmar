import sqlalchemy.exc
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.location.update_location_command import UpdateLocationCommand
from bakery.application.core.location_mapper import LocationMapper
from bakery.application.dto.location_dto import LocationDTO
from bakery.application.exception.bakery_exception import BakeryException
from bakery.infrastructure.repositories.location_repository import LocationRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger


@Mediator.register_handler(UpdateLocationCommand)
@singleton
class UpdateLocationsHandler:

    @inject
    def __init__(self, location_repository: LocationRepository, logger: Logger, location_mapper: LocationMapper,
                 mediator: Mediator):
        self._location_mapper = location_mapper
        self._location_repository = location_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, location_command: UpdateLocationCommand) -> LocationDTO:
        try:
            with self._location_repository.session_scope() as session:
                location = self._location_repository.get_location(location_command.location_id, session=session)
                if location:
                    location.name = location_command.location_name
                    location.description = location_command.location_description
                    # update updated by also
                    self._location_repository.update_location(location=location, session=session)
                    return self._location_mapper.map_location_dto(location)
                else:
                    raise BakeryException(message="Location not found", status_code=HTTP_400_BAD_REQUEST)
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                raise BakeryException(message="Location with this name already exist", status_code=HTTP_400_BAD_REQUEST)

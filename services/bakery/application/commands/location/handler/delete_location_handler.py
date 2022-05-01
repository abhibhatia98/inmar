import psycopg2
import sqlalchemy.exc
from bson import ObjectId
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION
from psycopg2 import errors
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.location.add_location_command import AddLocationsCommand, AddLocationCommand
from bakery.application.commands.location.delete_location_command import DeleteLocationCommand
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.entity import EntityOperationStatus
from bakery.domain.model.location import Location
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger
from shared.util.datetime import now


@Mediator.register_handler(DeleteLocationCommand)
@singleton
class DeleteLocationsHandler:

    @inject
    def __init__(self, location_repository: EntityRepository, logger: Logger, mediator: Mediator):
        self._location_repository = location_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, location: DeleteLocationCommand) -> bool:
        with self._location_repository.session_scope() as session:
            if self._location_repository.delete_entity(Location,location.location_id, session=session) == 0:
                raise BakeryException(message="location with this id does not exist", status_code=HTTP_400_BAD_REQUEST)
        return True

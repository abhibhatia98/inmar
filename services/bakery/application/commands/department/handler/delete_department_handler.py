from injector import singleton, inject
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.department.delete_department_command import DeleteDepartmentCommand
from bakery.application.exception.bakery_exception import BakeryException
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger


@Mediator.register_handler(DeleteDepartmentCommand)
@singleton
class DeleteDepartmentHandler:

    @inject
    def __init__(self, entity_repository: EntityRepository, logger: Logger, mediator: Mediator):
        self._entity_repository = entity_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, department: DeleteDepartmentCommand) -> bool:
        self._logger.info("command received for delete department")
        with self._entity_repository.session_scope() as session:
            if self._entity_repository.delete_department(department_id=department.department_id,
                                                         location_id=department.location_id, session=session) == 0:
                raise BakeryException(message="Department with this id does not exist",
                                      status_code=HTTP_400_BAD_REQUEST)
        self._logger.info("command for delete department completed successfully")
        return True

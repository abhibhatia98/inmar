import sqlalchemy.exc
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.department.update_department_command import UpdateDepartmentCommand
from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.dto.department_dto import DepartmentDTO
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.model.department import Department
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger


@Mediator.register_handler(UpdateDepartmentCommand)
@singleton
class UpdateDepartmentHandler:

    @inject
    def __init__(self, entity_repository: EntityRepository, logger: Logger, dto_mapper: DTOMapper,
                 mediator: Mediator):
        self._dto_mapper = dto_mapper
        self._entity_repository = entity_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, department_command: UpdateDepartmentCommand) -> DepartmentDTO:
        try:
            with self._entity_repository.session_scope() as session:
                department = self._entity_repository.get_entity(Department,department_command.department_id, session=session)
                if department:
                    department.name = department_command.department_name
                    department.description = department_command.department_description
                    # update updated by also
                    self._entity_repository.update_entity(entity=department, session=session)
                    return self._dto_mapper.map_location_dto(department)
                else:
                    raise BakeryException(message="Department not found", status_code=HTTP_400_BAD_REQUEST)
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                raise BakeryException(message="Location with this name already exist", status_code=HTTP_400_BAD_REQUEST)

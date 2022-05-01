import sqlalchemy.exc
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.category.update_category_command import UpdateCategoryCommand
from bakery.application.commands.department.update_department_command import UpdateDepartmentCommand
from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.dto.category_dto import CategoryDTO
from bakery.application.dto.department_dto import DepartmentDTO
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.model.category import Category
from bakery.domain.model.department import Department
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger


@Mediator.register_handler(UpdateCategoryCommand)
@singleton
class UpdateDepartmentHandler:

    @inject
    def __init__(self, entity_repository: EntityRepository, logger: Logger, dto_mapper: DTOMapper,
                 mediator: Mediator):
        self._dto_mapper = dto_mapper
        self._entity_repository = entity_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, category_command: UpdateCategoryCommand) -> CategoryDTO:
        """
        responsible for updating categories to a department
        :param category_command:
        :return:
        """
        try:
            with self._entity_repository.session_scope() as session:
                category = self._entity_repository.get_entity(Category, category_command.category_id, session=session)
                if category:
                    category.name = category_command.category_name
                    category.description = category_command.category_description
                    # update updated by also
                    self._entity_repository.update_entity(entity=category, session=session)
                    return self._dto_mapper.map_category_dto(category)
                else:
                    raise BakeryException(message="category not found", status_code=HTTP_400_BAD_REQUEST)
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                raise BakeryException(message="Location with this name already exist", status_code=HTTP_400_BAD_REQUEST)

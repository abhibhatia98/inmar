import psycopg2
import sqlalchemy.exc
from bson import ObjectId
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION, FOREIGN_KEY_VIOLATION
from psycopg2 import errors
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.category.add_category_command import AddCategoryCommand, CategoryCommand
from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.entity import EntityOperationStatus
from bakery.domain.model.category import Category
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger
from shared.util.datetime import now


@Mediator.register_handler(AddCategoryCommand)
@singleton
class AddDepartmentsHandler:

    @inject
    def __init__(self, entity_repository: EntityRepository, dto_mapper: DTOMapper, logger: Logger,
                 mediator: Mediator):
        self._dto_mapper = dto_mapper
        self._entity_repository = entity_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, add_category_command: AddCategoryCommand) -> None:
        category_data = []
        for category_command in add_category_command.category_list:
            category_command: CategoryCommand
            category = Category(id=str(ObjectId()),
                                location_id=add_category_command.location_id,
                                department_id=add_category_command.department_id,
                                name=category_command.category_name,
                                description=category_command.category_description,
                                created_on=now(),
                                updated_on=now(),
                                created_by='626d38970b9eabe51bb35a65',
                                updated_by='626d38970b9eabe51bb35a65')
            category.operation_status = EntityOperationStatus.ADDED.value
            category_data.append(category)
        try:
            with self._entity_repository.session_scope() as session:
                self._entity_repository.add_entities(category_data, session=session)
            return [self._dto_mapper.map_category_dto(category) for category in category_data]
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                starts = str(e.orig.args).find("=") + 2
                ends = str(e.orig.args)[starts:].find(")")
                message = "Category with name " + str(e.orig.args)[starts:starts + ends] + " already exist"
                raise BakeryException(message=message, status_code=HTTP_400_BAD_REQUEST)
            if e.orig.pgcode == FOREIGN_KEY_VIOLATION:
                raise BakeryException(message="Please provided correct department and location information",
                                      status_code=HTTP_400_BAD_REQUEST)

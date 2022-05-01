import psycopg2
import sqlalchemy.exc
from bson import ObjectId
from injector import singleton, inject
from psycopg2.errorcodes import UNIQUE_VIOLATION, FOREIGN_KEY_VIOLATION
from psycopg2 import errors
from starlette.status import HTTP_400_BAD_REQUEST

from bakery.application.commands.department.add_department_command import AddDepartmentsCommand, DepartmentCommand
from bakery.application.commands.location.add_location_command import AddLocationsCommand, AddLocationCommand
from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.exception.bakery_exception import BakeryException
from bakery.domain.entity import EntityOperationStatus
from bakery.domain.model.department import Department
from bakery.domain.model.location import Location
from bakery.infrastructure.repositories.entity_repository import EntityRepository
from shared.integration.mediator import Mediator
from shared.logging.logger import Logger
from shared.util.datetime import now


@Mediator.register_handler(AddDepartmentsCommand)
@singleton
class AddDepartmentsHandler:

    @inject
    def __init__(self, entity_repository: EntityRepository, dto_mapper: DTOMapper, logger: Logger,
                 mediator: Mediator):
        self._dto_mapper = dto_mapper
        self._entity_repository = entity_repository
        self._logger = logger
        self._mediator = mediator

    def handle(self, departments_command: AddDepartmentsCommand) -> None:
        """
        responsible for adding departments to a location
        :param departments_command:
        :return:
        """
        self._logger.info("command received for add department")
        department_data = []
        for department_command in departments_command.departments_list:
            department_command: DepartmentCommand
            department = Department(id=str(ObjectId()),
                                    location_id=departments_command.location_id,
                                    name=department_command.department_name,
                                    description=department_command.department_description,
                                    created_on=now(),
                                    updated_on=now(),
                                    created_by='626d38970b9eabe51bb35a65',
                                    updated_by='626d38970b9eabe51bb35a65')
            department.operation_status = EntityOperationStatus.ADDED.value
            department_data.append(department)
        try:
            with self._entity_repository.session_scope() as session:
                self._entity_repository.add_entities(department_data, session=session)
            self._logger.info("command for add department completed success")
            return [self._dto_mapper.map_department_dto(department) for department in department_data]
        except sqlalchemy.exc.IntegrityError as e:
            if e.orig.pgcode == UNIQUE_VIOLATION:
                starts = str(e.orig.args).find("=") + 2
                ends = str(e.orig.args)[starts:].find(")")
                message = "location with name " + str(e.orig.args)[starts:starts + ends] + " already exist"
                raise BakeryException(message=message, status_code=HTTP_400_BAD_REQUEST)
            if e.orig.pgcode == FOREIGN_KEY_VIOLATION:
                raise BakeryException(message="Please provided correct location information",
                                      status_code=HTTP_400_BAD_REQUEST)


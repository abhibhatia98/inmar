from injector import inject
from sqlalchemy import asc

from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.queries.query_base import QueryBase
from bakery.domain.model.department import Department
from shared.logging.logger import Logger


class DepartmentQueries(QueryBase):
    @inject
    def __init__(self, logger: Logger, dto_mapper: DTOMapper):
        self._logger = logger
        self._dto_mapper = dto_mapper
        super().__init__()

    def get_departments(self, location_id: str, skip: int, page_size: int):
        with self.session_scope() as session:
            departments = session.query(Department).filter(Department.location_id==location_id).order_by(asc(Department.name)).limit(page_size).offset(skip)
            department_dto = [self._dto_mapper.map_department_dto(department) for department in departments]
            return department_dto

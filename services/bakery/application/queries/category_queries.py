from injector import inject
from sqlalchemy import asc, and_

from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.queries.query_base import QueryBase
from bakery.domain.model.category import Category
from bakery.domain.model.department import Department
from shared.logging.logger import Logger


class CategoriesQueries(QueryBase):
    @inject
    def __init__(self, logger: Logger, dto_mapper: DTOMapper):
        self._logger = logger
        self._dto_mapper = dto_mapper
        super().__init__()

    def get_department_categories(self, location_id: str, department_id: str, skip: int, page_size: int):
        with self.session_scope() as session:
            categories = session.query(Category).filter(and_(Department.id == department_id,Department.location_id==location_id)).order_by(
                asc(Category.name)).limit(page_size).offset(skip)
            category_dto = [self._dto_mapper.map_category_dto(category) for category in categories]
            return category_dto

from injector import inject
from sqlalchemy import asc

from bakery.application.core.dto_mapper import DTOMapper
from bakery.application.queries.query_base import QueryBase
from bakery.domain.model.location import Location
from shared.logging.logger import Logger


class LocationQueries(QueryBase):
    @inject
    def __init__(self, logger: Logger, location_mapper: DTOMapper):
        self._logger = logger
        self._location_mapper = location_mapper
        super().__init__()

    def get_locations(self, skip: int, page_size: int):
        with self.session_scope() as session:
            locations = session.query(Location).filter().order_by(asc(Location.name)).limit(page_size).offset(skip)
            location_dto = [self._location_mapper.map_location_dto(location) for location in locations]
            return location_dto

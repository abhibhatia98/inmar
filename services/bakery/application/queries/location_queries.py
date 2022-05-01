from injector import inject
from sqlalchemy import asc

from bakery.application.core.location_mapper import LocationMapper
from bakery.application.dto.location_dto import LocationDTO
from bakery.application.queries.query_base import QueryBase
from bakery.domain.model.location import Location
from shared.application.custom_types.oid import OID
from shared.application.enums.model_property import ModelProps
from shared.application.filter.query_builder import QueryBuilder
from shared.constant.mongo_constant import MongoConstant
from shared.logging.logger import Logger


class LocationQueries(QueryBase):
    @inject
    def __init__(self, logger: Logger,location_mapper:LocationMapper):
        self._logger = logger
        self._location_mapper = location_mapper
        super().__init__()

    def get_locations(self,skip: int,
                      page_size: int,location_id: OID = None,search_text: str = None):
        with self.session_scope() as session:
            locations = session.query(Location).filter().order_by(asc(Location.name)).limit(page_size).offset(skip)
            location_dto = [self._location_mapper.map_location_dto(location) for location in locations]
            return location_dto
from typing import List

from injector import singleton
from sqlalchemy.orm import Session

from bakery.domain.entity import EntityOperationStatus
from bakery.domain.model.location import Location
from bakery.infrastructure.repository import BaseRepository


# from bakery.domain.location import Entity


@singleton
class LocationRepository(BaseRepository):
    def add_locations(self, locations: List[Location], session) -> None:
        # added_entities = []
        # for location in locations:
        #     if location.operation_status == EntityOperationStatus.ADDED.value:
        #         added_entities.append(location)
        #     elif location.operation_status == EntityOperationStatus.DELETED.value:
        #         transaction_session.delete(location)
        #     elif location.operation_status == EntityOperationStatus.UPDATED.value:
        #         transaction_session.add(location)
        session.bulk_save_objects(locations)

    def delete_location(self, location_id: str, session: Session) -> int:
        return session.query(Location).filter(Location.id == location_id).delete()

    def get_location(self, location_id: str, session: Session) -> Location:
        return session.query(Location).filter(Location.id == location_id).first()

    def update_location(self, location: Location, session: Session):
        session.add(location)

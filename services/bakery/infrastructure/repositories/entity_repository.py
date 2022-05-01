from typing import List

from injector import singleton
from sqlalchemy import and_
from sqlalchemy.orm import Session

from bakery.domain.entity import EntityOperationStatus, Entity
from bakery.domain.model.department import Department
from bakery.domain.model.location import Location
from bakery.infrastructure.repository import BaseRepository


# from bakery.domain.location import Entity


@singleton
class EntityRepository(BaseRepository):

    def add_entities(self, entities: List[Entity], session) -> None:
        # added_entities = []
        # for location in locations:
        #     if location.operation_status == EntityOperationStatus.ADDED.value:
        #         added_entities.append(location)
        #     elif location.operation_status == EntityOperationStatus.DELETED.value:
        #         transaction_session.delete(location)
        #     elif location.operation_status == EntityOperationStatus.UPDATED.value:
        #         transaction_session.add(location)
        session.bulk_save_objects(entities)

    def delete_entity(self, entity: Entity, entity_id: str, session: Session) -> int:
        return session.query(entity).filter(entity.id == entity_id).delete()

    def get_entity(self, entity: Entity, entity_id: str, session: Session) -> Entity:
        return session.query(entity).filter(entity.id == entity_id).first()

    def update_entity(self, entity: Entity, session: Session):
        session.add(entity)

    def delete_department(self,location_id:str,department_id:str,session:Session)-> int:
        return session.query(Department).filter(and_(Department.id==department_id,Department.location_id==location_id)).delete()

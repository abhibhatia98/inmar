from typing import List

from injector import singleton
from sqlalchemy import and_
from sqlalchemy.orm import Session

from bakery.domain.entity import EntityOperationStatus, Entity
from bakery.domain.model.category import Category
from bakery.domain.model.department import Department
from bakery.domain.model.location import Location
from bakery.infrastructure.repository import BaseRepository


# from bakery.domain.location import Entity


@singleton
class EntityRepository(BaseRepository):

    def add_entities(self, entities: List[Entity], session) -> None:
        added_entities = []
        for entity in entities:
            if entity.operation_status == EntityOperationStatus.ADDED.value:
                added_entities.append(entity)
            elif entity.operation_status == EntityOperationStatus.DELETED.value:
                session.delete(entity)
            elif entity.operation_status == EntityOperationStatus.UPDATED.value:
                session.add(entity)
        session.bulk_save_objects(entities)

    def delete_entity(self, entity: Entity, entity_id: str, session: Session) -> int:
        return session.delete(self.get_entity(entity,entity_id,session))

    def get_entity(self, entity: Entity, entity_id: str, session: Session) -> Entity:
        return session.query(entity).filter(entity.id == entity_id).first()

    def update_entity(self, entity: Entity, session: Session):
        session.add(entity)

    def delete_department(self, location_id: str, department_id: str, session: Session) -> int:
        return session.delete(session.query(Department).filter(
            and_(Department.id == department_id, Department.location_id == location_id)).first())

    def delete_category(self, location_id: str, department_id: str, category_id: str, session: Session) -> int:
        return session.delete(session.query(Category).filter(
            and_(Category.id == category_id, Category.location_id == location_id,
                 Category.department_id == department_id)).first())

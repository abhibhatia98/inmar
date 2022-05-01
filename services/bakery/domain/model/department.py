from sqlalchemy import Column, DateTime, String, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, backref

from bakery.domain.entity import Entity
from bakery.domain.model.location import Location


class Department(Entity):
    __tablename__ = "department"
    id = Column(String, primary_key=True)
    location_id = Column(String, ForeignKey("location.id", ondelete='CASCADE'), nullable=False)
    name = Column(String)
    description = Column(String)
    updated_on = Column(DateTime())
    updated_by = Column(String)
    created_on = Column(DateTime())
    created_by = Column(String)
    category = relationship("Category", cascade="all, delete")

    __table_args__ = (
        UniqueConstraint("location_id", "name", name="unique_department_name"),
    )

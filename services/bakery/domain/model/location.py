from bson import ObjectId
from mongoengine import *
from sqlalchemy import UniqueConstraint, Column, DateTime, String
from sqlalchemy.orm import relationship

from bakery.domain.entity import Entity
from shared.util.datetime import now


class Location(Entity):
    __tablename__ = "location"
    id = Column(String, primary_key=True)
    name = Column(String, unique=True)
    description = Column(String)
    updated_on = Column(DateTime())
    updated_by = Column(String)
    created_on = Column(DateTime())
    created_by = Column(String)
    department = relationship("Department",cascade="all, delete")
    category = relationship("Category", cascade="all, delete")

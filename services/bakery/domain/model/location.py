from bson import ObjectId
from mongoengine import *
from sqlalchemy import UniqueConstraint, Column, DateTime, String

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

#
# location = Location(id=ObjectId(), name="Holigate")
# location.created_by = location.updated_by = ObjectId()
# location.created_on = location.updated_on = now()
# location.add()

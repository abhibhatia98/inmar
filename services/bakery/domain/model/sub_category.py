from bson import ObjectId
from mongoengine import *

from bakery.domain.entity import Entity


class SubCategory(Entity):
    pass

    def __init__(self, *args, **values):
        super().__init__(*args, **values)



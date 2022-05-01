from bson import ObjectId
from mongoengine import *

from bakery.domain.entity import Entity


class SubCategory(Entity):
    id = ObjectIdField(primary_key=True)
    category_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField(required=False)
    updated_on = DateTimeField(required=True)
    updated_by = StringField(required=True)
    created_on = DateTimeField(required=True)
    created_by = ObjectIdField(required=True)

    def __init__(self, *args, **values):
        super().__init__(*args, **values)


# loc = Location(id=ObjectId(), name="jamuna nagar")
# loc.save()

from bson import ObjectId
from mongoengine import *
from pymongo.common import validate

from bakery.domain.entity import Entity


class Category(Entity):
    id = ObjectIdField(primary_key=True)
    department_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField(required=False)
    updated_on = DateTimeField(required=True)
    updated_by = StringField(required=True)
    created_on = DateTimeField(required=True)
    created_by = ObjectIdField(required=True)

    # def __init__(self, *args, **values):
    #     super().__init__(*args, **values)

    meta = {
        # 'collection': 'master_category',
        'indexes': [
            {
                'fields': ['department_id', 'name'],
                'unique': True
            }
        ]
    }

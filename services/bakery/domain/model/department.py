from mongoengine import ObjectIdField
from bakery.domain.entity import Entity
from mongoengine import *


class department(Entity):
    id = ObjectIdField(primary_key=True)
    location_id = ObjectIdField(required=True)
    name = StringField(required=True)
    description = StringField(required=False)
    updated_on = DateTimeField(required=True)
    updated_by = StringField(required=True)
    created_on = DateTimeField(required=True)
    created_by = ObjectIdField(required=True)

    meta = {
        # 'collection': 'master_category',
        'indexes': [
            {
                'fields': ['location_id', 'name'],
                'unique': True
            }
        ]
    }

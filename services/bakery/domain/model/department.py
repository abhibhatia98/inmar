from bakery.domain.entity import Entity
from sqlalchemy import Column, DateTime, String
from bakery.domain.entity import Entity


class Department(Entity):
    __tablename__ = "department"
    id = Column(String, primary_key=True)
    location_id = Column(String)
    name = Column(String)
    description = Column(String)
    updated_on = Column(DateTime())
    updated_by = Column(String)
    created_on = Column(DateTime())
    created_by = Column(String)

    meta = {
        # 'collection': 'master_category',
        'indexes': [
            {
                'fields': ['location_id', 'name'],
                'unique': True
            }
        ]
    }

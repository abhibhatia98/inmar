from sqlalchemy import Column, DateTime, String, UniqueConstraint, ForeignKey
from bakery.domain.entity import Entity


class Category(Entity):
    __tablename__ = "category"
    id = Column(String, primary_key=True)
    location_id = Column(String,ForeignKey("location.id"), nullable=False)
    department_id = Column(String,ForeignKey("department.id"), nullable=False)
    name = Column(String)
    description = Column(String)
    updated_on = Column(DateTime())
    updated_by = Column(String)
    created_on = Column(DateTime())
    created_by = Column(String)

    __table_args__ = (
        UniqueConstraint("department_id", "name", name="unique_category_name"),
    )

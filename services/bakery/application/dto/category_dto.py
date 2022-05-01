from bakery.application.dto.dto import DTO
from datetime import datetime
from typing import List


class CategoryDTO(DTO):
    """
    Response returned to frontend for location create and get APIs
    """

    def __init__(self, location_id: str, department_id: str, category_id: str, category_name: str, description: str,
                 updated_by: str):
        self.category_id = category_id
        self.department_id = department_id
        self.location_id = location_id
        self.category_name = category_name
        self.description = description
        self.updated_by = updated_by

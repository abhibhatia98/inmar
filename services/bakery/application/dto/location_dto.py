from bakery.application.dto.dto import DTO
from typing import List


class LocationDTO(DTO):
    def __init__(self, location_id:str,location_name: str, description: str,updated_by):
        self.location_id = location_id
        self.location_name = location_name
        self.description = description
        self.updated_by = str(updated_by)
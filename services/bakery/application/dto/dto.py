from shared.util.mapper import map_values
from pydantic import BaseModel


class DTO:

    def map_item(self, item, destination):
        return map_values(item, destination)

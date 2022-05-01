from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class CategoryCommand(CommandBase):
    category_name: str
    category_description: Optional[str]


class AddCategoryCommand(CommandBase):
    _location_id: str
    _department_id:str
    category_list: List[CategoryCommand]

    @property
    def location_id(self):
        return self._location_id

    def set_location_id(self, value):
        self._location_id = value

    @property
    def department_id(self):
        return self._department_id

    def set_department_id(self, value):
        self._department_id = value

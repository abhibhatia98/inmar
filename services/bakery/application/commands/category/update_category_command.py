from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class UpdateCategoryCommand(CommandBase):
    _location_id: str
    _department_id:str
    _category_id:str
    category_name: str
    category_description: Optional[str]

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

    @property
    def category_id(self):
        return self._category_id

    def set_category_id(self, value):
        self._category_id = value



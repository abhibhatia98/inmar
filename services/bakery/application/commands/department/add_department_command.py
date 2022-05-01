from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class DepartmentCommand(CommandBase):
    department_name: str
    department_description: Optional[str]


class AddDepartmentsCommand(CommandBase):
    _location_id: str
    departments_list: List[DepartmentCommand]

    @property
    def location_id(self):
        return self._location_id

    def set_location_id(self, value):
        self._location_id = value

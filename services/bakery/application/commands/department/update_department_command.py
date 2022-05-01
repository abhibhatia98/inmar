from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class UpdateDepartmentCommand(CommandBase):
    _location_id: str
    _department_id:str
    department_name: str
    department_description: Optional[str]

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



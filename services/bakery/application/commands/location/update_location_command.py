from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class UpdateLocationCommand(CommandBase):
    _location_id: str
    location_name: str
    location_description: Optional[str]

    @property
    def location_id(self):
        return self._location_id

    def set_location_id(self, value):
        self._location_id = value



from typing import List

from bakery.application.commands.command_base import CommandBase


class DeleteLocationCommand(CommandBase):
    _location_id: str

    @property
    def location_id(self):
        return self._location_id

    def set_location_id(self, value):
        self._location_id = value

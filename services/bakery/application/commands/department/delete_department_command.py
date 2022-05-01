from typing import List

from bakery.application.commands.command_base import CommandBase


class DeleteLocationCommand(CommandBase):
    location_id: str

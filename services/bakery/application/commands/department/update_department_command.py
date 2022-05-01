from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class UpdateLocationCommand(CommandBase):
    location_id: str
    location_name: str
    location_description: Optional[str]



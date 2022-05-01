from typing import List, Optional

from bakery.application.commands.command_base import CommandBase


class AddLocationCommand(CommandBase):
    location_name: str
    location_description: Optional[str]


class AddLocationsCommand(CommandBase):
    locations_list: List[AddLocationCommand]

from typing import Optional

from shared.authorization.context import Context
from pydantic import BaseModel


class CommandBase(BaseModel):
    _created_by: Optional[str]
    _updated_by: Optional[str]
    _context: Optional[Context] = None

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)

    class Config:
        arbitrary_types_allowed = True
        underscore_attrs_are_private = True

    @property
    def created_by(self):
        return self._created_by

    def set_created_by(self, value):
        self._created_by = value

    @property
    def updated_by(self):
        return self._updated_by

    def set_updated_by(self, value):
        self._updated_by = value

    @property
    def context(self) -> Context:
        return self._context

    def set_context(self, value: Context) -> None:
        self._context = value



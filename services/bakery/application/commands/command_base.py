from typing import Optional

from shared.application.custom_types.oid import OID
from shared.authorization.context import Context
from pydantic import BaseModel
from shared.logging.logging_properties import LoggingProperties


class CommandBase(BaseModel):
    _created_by: Optional[str]
    _updated_by: Optional[str]
    _organization_id: Optional[OID]
    _context: Optional[Context] = None
    _logg_props: Optional[LoggingProperties] = None

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
    def organization_id(self) -> OID:
        return self._organization_id

    def set_organization_id(self, value: OID) -> None:
        self._organization_id = value

    @property
    def context(self) -> Context:
        return self._context

    def set_context(self, value: Context) -> None:
        self._context = value

    @property
    def logg_props(self) -> LoggingProperties:
        return self._logg_props

    def set_logg_props(self, value: LoggingProperties) -> None:
        self._logg_props = value


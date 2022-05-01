from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class Context(BaseModel):
    user: str
    trace_id: Optional[str]
    permissions: Optional[List[str]]
    user_sub: Optional[str]
    user_email: Optional[EmailStr]
    user_role: Optional[str]
    organization_id: Optional[str]
    token: Optional[str]
    exat: Optional[datetime]

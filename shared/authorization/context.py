from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime


class Context(BaseModel):
    user: str
    trace_id: Optional[str]
    user_email: Optional[EmailStr]
    token: Optional[str]
    exat: Optional[datetime]

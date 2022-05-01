from typing import Optional
from pydantic import BaseModel


class CustomDimension(BaseModel):
    organization_id: Optional[str] = None
    trace_id: str = None
    project_id: Optional[str]
    master_category_id: Optional[str]
    user_id: Optional[str]
    request_url: Optional[str]  # used for generic exception handling only

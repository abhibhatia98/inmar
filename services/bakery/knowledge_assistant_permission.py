from pydantic.main import BaseModel
from typing import List
from shared.application.permissions.services import Services


class KnowledgeAssistantPermission(BaseModel):
    service: str = Services.KNOWLEDGE_ASSISTANT
    permissions: List[str]

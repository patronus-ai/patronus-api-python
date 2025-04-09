# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["PromptCreateResponse", "Prompt"]


class Prompt(BaseModel):
    id: str

    account_id: str

    body: str

    created_at: datetime

    labels: List[str]

    name: str

    project_id: str

    version: int

    description: Optional[str] = None


class PromptCreateResponse(BaseModel):
    prompt: Prompt

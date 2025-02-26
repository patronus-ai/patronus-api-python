# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ListTagsResponse", "Tag"]


class Tag(BaseModel):
    created_at: datetime

    key: str

    last_used: datetime

    value: str


class ListTagsResponse(BaseModel):
    tags: List[Tag]

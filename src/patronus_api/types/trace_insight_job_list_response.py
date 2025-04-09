# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TraceInsightJobListResponse", "Insight"]


class Insight(BaseModel):
    job_id: Optional[str] = None

    status: Optional[str] = None

    trace_id: str


class TraceInsightJobListResponse(BaseModel):
    insights: List[Insight]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["TraceInsightJobListResponse", "InsightJob"]


class InsightJob(BaseModel):
    app: Optional[str] = None

    created_at: datetime

    experiment_id: Optional[str] = None

    job_id: str

    project_id: str

    status: str

    trace_id: str


class TraceInsightJobListResponse(BaseModel):
    insight_jobs: List[InsightJob]

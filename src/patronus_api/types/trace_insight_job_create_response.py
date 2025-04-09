# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["TraceInsightJobCreateResponse"]


class TraceInsightJobCreateResponse(BaseModel):
    job_id: str

    status: str

    trace_id: str

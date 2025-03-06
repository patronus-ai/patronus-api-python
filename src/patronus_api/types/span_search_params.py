# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SpanSearchParams"]


class SpanSearchParams(TypedDict, total=False):
    limit: int

    parent_span_id: Optional[Literal["any"]]

    project_id: Optional[str]

    trace_id: Optional[str]

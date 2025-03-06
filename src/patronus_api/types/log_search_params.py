# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["LogSearchParams"]


class LogSearchParams(TypedDict, total=False):
    limit: int

    trace_id: Optional[str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ClientAnnotateParams"]


class ClientAnnotateParams(TypedDict, total=False):
    annotation_criteria_id: Required[str]

    log_id: Required[str]

    explanation: Optional[str]

    value_pass: Optional[bool]

    value_score: Optional[float]

    value_text: Optional[str]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["FeedbackRetrieveParams"]


class FeedbackRetrieveParams(TypedDict, total=False):
    evaluation_result_id: Optional[str]

    evaluation_run_candidate_input_id: Optional[int]

    evaluation_run_id: Optional[str]

    evaluator_id: Optional[str]

    limit: int

    offset: int

    profile_name: Optional[str]

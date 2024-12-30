# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["FeedbackGiveParams"]


class FeedbackGiveParams(TypedDict, total=False):
    feedback_positive: Required[bool]
    """Whether the feedback is positive or negative."""

    evaluation_result_id: Optional[str]
    """Evaluation Result ID for which feedback is given.

    Only applicable for LLM Monitoring results.
    """

    evaluation_run_candidate_input_id: Optional[int]
    """ID of the sample for which feedback is given.

    Only applicable for Evaluation Run results.
    """

    evaluation_run_id: Optional[str]
    """
    Evaluation Run ID associated with sample for which feedback is given. Only
    applicable for Evaluation Run results.
    """

    evaluator_id: Optional[str]
    """
    Evaluator ID associated with sample for which feedback is given. Only applicable
    for Evaluation Run results.
    """

    profile_name: Optional[str]
    """Evaluation run profile name."""

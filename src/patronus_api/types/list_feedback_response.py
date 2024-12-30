# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ListFeedbackResponse", "Feedback"]


class Feedback(BaseModel):
    id: str
    """ID of the feedback record."""

    created_at: datetime
    """Timestamp when the feedback record was created."""

    evaluation_result_id: Optional[str] = None
    """Evaluation Result ID for which feedback is given.

    Only applicable for LLM Monitoring
    """

    evaluation_run_candidate_input_id: Optional[int] = None
    """ID of the sample for which feedback is given.

    Only applicable for Evaluation Run results.
    """

    evaluation_run_id: Optional[str] = None
    """evaluation run id."""

    evaluator_id: str
    """Evaluation run criterion id."""

    feedback_positive: Optional[bool] = None
    """Whether the feedback is positive or negative."""

    profile_name: Optional[str] = None
    """Evaluation run profile name."""


class ListFeedbackResponse(BaseModel):
    feedbacks: List[Feedback]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AnnotateResponse", "Evaluation"]


class Evaluation(BaseModel):
    id: str

    created_at: Optional[datetime] = None

    criteria: Optional[str] = None

    criteria_id: Optional[str] = None

    evaluation_duration: Optional[str] = None

    evaluator_family: Optional[str] = None

    evaluator_id: Optional[str] = None

    explain_strategy: Optional[str] = None

    explanation: Optional[str] = None

    explanation_duration: Optional[str] = None

    log_id: str

    score: Optional[float] = None

    text_output: Optional[str] = None

    annotation_criteria_id: Optional[str] = None

    criteria_config: Optional[object] = None

    criteria_revision: Optional[int] = None

    evaluation_feedback: Optional[bool] = None

    evaluation_type: Optional[str] = None

    metadata: Optional[object] = None

    metric_description: Optional[str] = None

    metric_name: Optional[str] = None

    pass_: Optional[bool] = FieldInfo(alias="pass", default=None)

    usage: Optional[object] = None


class AnnotateResponse(BaseModel):
    evaluation: Evaluation

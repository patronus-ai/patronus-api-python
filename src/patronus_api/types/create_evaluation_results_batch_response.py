# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CreateEvaluationResultsBatchResponse", "EvaluationResult"]


class EvaluationResult(BaseModel):
    id: Optional[str] = None

    app: Optional[str] = None

    created_at: Optional[datetime] = None

    evaluator_id: str


class CreateEvaluationResultsBatchResponse(BaseModel):
    evaluation_results: List[EvaluationResult]

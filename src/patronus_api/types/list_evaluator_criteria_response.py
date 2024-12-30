# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ListEvaluatorCriteriaResponse", "EvaluatorCriterion"]


class EvaluatorCriterion(BaseModel):
    config: Optional[object] = None

    created_at: datetime

    evaluator_family: Optional[str] = None

    is_patronus_managed: bool

    name: Optional[str] = None

    public_id: str

    revision: int

    description: Optional[str] = None


class ListEvaluatorCriteriaResponse(BaseModel):
    evaluator_criteria: List[EvaluatorCriterion]

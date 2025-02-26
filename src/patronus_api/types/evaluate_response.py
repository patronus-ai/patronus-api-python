# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .evaluation_result import EvaluationResult

__all__ = ["EvaluateResponse", "Result"]


class Result(BaseModel):
    criteria: Optional[str] = None

    error_message: Optional[str] = None

    evaluation_result: Optional[EvaluationResult] = None

    evaluator_id: str

    status: str
    """Status of the criterion evaluation. "success" indicates successful evaluation."""


class EvaluateResponse(BaseModel):
    results: List[Result]

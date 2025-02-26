# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .evaluation_result import EvaluationResult

__all__ = ["EvaluationResultSearchResponse"]


class EvaluationResultSearchResponse(BaseModel):
    results: List[EvaluationResult]

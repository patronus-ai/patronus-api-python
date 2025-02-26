# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .evaluation_result import EvaluationResult

__all__ = ["EvaluationResultRetrieveResponse"]


class EvaluationResultRetrieveResponse(BaseModel):
    evaluation_result: EvaluationResult

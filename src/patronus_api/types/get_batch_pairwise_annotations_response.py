# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["GetBatchPairwiseAnnotationsResponse", "PairwiseAnnotation"]


class PairwiseAnnotation(BaseModel):
    created_at: datetime

    log_a_id: str

    log_a_score: float

    log_b_id: str

    log_b_score: float

    name: str


class GetBatchPairwiseAnnotationsResponse(BaseModel):
    pairwise_annotations: List[Optional[PairwiseAnnotation]]

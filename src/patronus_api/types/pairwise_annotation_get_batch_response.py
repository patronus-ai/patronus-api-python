# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pairwise_annotation import PairwiseAnnotation

__all__ = ["PairwiseAnnotationGetBatchResponse"]


class PairwiseAnnotationGetBatchResponse(BaseModel):
    pairwise_annotations: List[Optional[PairwiseAnnotation]]

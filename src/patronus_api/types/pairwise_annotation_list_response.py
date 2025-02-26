# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .pairwise_annotation import PairwiseAnnotation

__all__ = ["PairwiseAnnotationListResponse"]


class PairwiseAnnotationListResponse(BaseModel):
    pairwise_annotations: List[PairwiseAnnotation]

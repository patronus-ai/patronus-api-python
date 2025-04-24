# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel
from .pairwise_annotation import PairwiseAnnotation

__all__ = ["PairwiseAnnotationCreateResponse"]


class PairwiseAnnotationCreateResponse(BaseModel):
    pairwise_annotation: PairwiseAnnotation

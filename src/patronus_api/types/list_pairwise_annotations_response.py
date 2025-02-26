# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ListPairwiseAnnotationsResponse"]


class ListPairwiseAnnotationsResponse(BaseModel):
    pairwise_annotations: List[object]

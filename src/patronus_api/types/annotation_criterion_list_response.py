# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .annotation_criteria import AnnotationCriteria

__all__ = ["AnnotationCriterionListResponse"]


class AnnotationCriterionListResponse(BaseModel):
    annotation_criteria: List[AnnotationCriteria]

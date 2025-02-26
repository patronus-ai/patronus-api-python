# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .annotation_criteria import AnnotationCriteria

__all__ = ["AnnotationCriterionCreateResponse"]


class AnnotationCriterionCreateResponse(BaseModel):
    annotation_criteria: AnnotationCriteria

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel
from .annotation_criteria import AnnotationCriteria

__all__ = ["AnnotationCriterionUpdateResponse"]


class AnnotationCriterionUpdateResponse(BaseModel):
    annotation_criteria: AnnotationCriteria

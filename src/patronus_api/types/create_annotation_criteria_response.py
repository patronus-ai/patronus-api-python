# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["CreateAnnotationCriteriaResponse", "AnnotationCriteria", "AnnotationCriteriaCategory"]


class AnnotationCriteriaCategory(BaseModel):
    label: Optional[str] = None

    score: Optional[float] = None


class AnnotationCriteria(BaseModel):
    id: str

    annotation_type: str

    categories: Optional[List[AnnotationCriteriaCategory]] = None

    created_at: datetime

    description: Optional[str] = None

    name: str

    project_id: str

    updated_at: datetime


class CreateAnnotationCriteriaResponse(BaseModel):
    annotation_criteria: AnnotationCriteria

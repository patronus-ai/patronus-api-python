# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["ListAnnotationCriteriaResponse", "AnnotationCriterion", "AnnotationCriterionCategory"]


class AnnotationCriterionCategory(BaseModel):
    label: Optional[str] = None

    score: Optional[float] = None


class AnnotationCriterion(BaseModel):
    id: str

    annotation_type: str

    categories: Optional[List[AnnotationCriterionCategory]] = None

    created_at: datetime

    description: Optional[str] = None

    name: str

    project_id: str

    updated_at: datetime


class ListAnnotationCriteriaResponse(BaseModel):
    annotation_criteria: List[AnnotationCriterion]

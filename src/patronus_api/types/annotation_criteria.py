# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel
from .annotation_category import AnnotationCategory

__all__ = ["AnnotationCriteria"]


class AnnotationCriteria(BaseModel):
    id: str

    annotation_type: str

    categories: Optional[List[AnnotationCategory]] = None

    created_at: datetime

    description: Optional[str] = None

    name: str

    project_id: str

    updated_at: datetime

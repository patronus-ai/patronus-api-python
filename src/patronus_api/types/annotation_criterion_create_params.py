# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .annotation_type import AnnotationType
from .annotation_category_param import AnnotationCategoryParam

__all__ = ["AnnotationCriterionCreateParams"]


class AnnotationCriterionCreateParams(TypedDict, total=False):
    annotation_type: Required[AnnotationType]

    name: Required[str]

    project_id: Required[str]

    categories: Optional[Iterable[AnnotationCategoryParam]]

    description: Optional[str]

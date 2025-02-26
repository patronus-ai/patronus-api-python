# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AnnotationCriterionCreateParams", "Category"]


class AnnotationCriterionCreateParams(TypedDict, total=False):
    annotation_type: Required[Literal["binary", "continuous", "discrete", "categorical", "text_annotation"]]

    name: Required[str]

    project_id: Required[str]

    categories: Optional[Iterable[Category]]

    description: Optional[str]


class Category(TypedDict, total=False):
    label: Optional[str]

    score: Optional[float]

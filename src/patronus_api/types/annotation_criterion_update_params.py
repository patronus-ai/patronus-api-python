# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["AnnotationCriterionUpdateParams"]


class AnnotationCriterionUpdateParams(TypedDict, total=False):
    annotation_type: Required[object]

    name: Required[str]

    categories: Optional[Iterable[object]]

    description: Optional[str]

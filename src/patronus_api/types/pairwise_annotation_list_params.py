# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional
from typing_extensions import TypedDict

__all__ = ["PairwiseAnnotationListParams"]


class PairwiseAnnotationListParams(TypedDict, total=False):
    experiment_id: Optional[Iterable[int]]

    limit: int

    log_id: Optional[str]

    name: Optional[str]

    offset: int

    project_id: Optional[List[str]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["PairwiseAnnotationGetBatchParams", "PairwiseAnnotation"]


class PairwiseAnnotationGetBatchParams(TypedDict, total=False):
    pairwise_annotations: Required[Iterable[PairwiseAnnotation]]


class PairwiseAnnotation(TypedDict, total=False):
    log_a_id: Required[str]

    log_b_id: Required[str]

    name: Required[str]

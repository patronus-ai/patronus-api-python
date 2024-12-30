# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PairwiseAnnotationDeleteParams"]


class PairwiseAnnotationDeleteParams(TypedDict, total=False):
    log_a_id: Required[str]

    log_b_id: Required[str]

    name: Required[str]

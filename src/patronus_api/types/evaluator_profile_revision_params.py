# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluatorProfileRevisionParams"]


class EvaluatorProfileRevisionParams(TypedDict, total=False):
    config: Required[object]

    description: Optional[str]

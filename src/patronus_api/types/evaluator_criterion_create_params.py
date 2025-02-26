# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluatorCriterionCreateParams"]


class EvaluatorCriterionCreateParams(TypedDict, total=False):
    config: Required[Dict[str, object]]

    evaluator_family: Required[str]

    name: Required[str]

    description: Optional[str]

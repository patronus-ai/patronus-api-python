# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EvaluationResultEvaluationFeedbackParams"]


class EvaluationResultEvaluationFeedbackParams(TypedDict, total=False):
    feedback: Required[Literal["positive", "negative"]]

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .evaluation_explain_strategies import EvaluationExplainStrategies

__all__ = ["EvaluationResultSearchParams"]


class EvaluationResultSearchParams(TypedDict, total=False):
    after_datetime: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter results to those recorded after this date and time."""

    after_id: Optional[int]
    """Filter results to those with an ID greater than this value."""

    app: Optional[str]
    """Filter by the application name related to the evaluation results."""

    before_datetime: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Filter results to those recorded before this date and time."""

    before_id: Optional[int]
    """Filter results to those with an ID less than this value."""

    criteria: Optional[str]
    """
    Filter by the name of the evaluator criteria associated with the evaluation
    results.
    """

    dataset_id: Optional[str]
    """Filter by the dataset ID related to the evaluation results."""

    evaluation_feedback_status: Optional[Literal["given", "notgiven", "positive", "negative"]]

    evaluation_run_id: Optional[str]
    """Filter by the evaluation run ID related to the evaluation results."""

    evaluation_type: Optional[Literal["patronus_evaluation", "client_evaluation", "annotation"]]

    evaluator_family: Optional[str]
    """Filter by the evaluator family associated with the evaluation results."""

    evaluator_id: Optional[str]
    """Filter by the ID of the evaluation criterion."""

    evaluator_profile_public_id: Optional[str]
    """Filter by public id of evaluator profile used in evaluation."""

    experiment_id: Optional[str]
    """Filter by the experiment ID related to the evaluation results."""

    explain: Optional[bool]
    """Filter results by having explanation."""

    explain_strategy: Optional[EvaluationExplainStrategies]
    """Filter results by explain strategy."""

    favorite: Optional[bool]

    limit: int
    """Maximum number of results to return."""

    order: Literal["created_at", "-created_at", "dataset_sample_id", "-dataset_sample_id"]
    """Ordering option for the search results."""

    pass_: Annotated[Optional[bool], PropertyInfo(alias="pass")]
    """Filter results by those which pass or failed the evaluation."""

    profile_name: Optional[str]
    """
    Filter by the name of the evaluator profile associated with the evaluation
    results.
    """

    project_id: Optional[str]
    """Filter by the project ID related to the evaluation results."""

    score_raw_max: Optional[float]

    score_raw_min: Optional[float]

    tags: Optional[Dict[str, str]]
    """Filter by given tags.

    Tags given in this filter are combined with the and clause. Example:
    {"model_version": "1.0.0", "next_tag": "1234"} Will return only those evaluation
    results which have both tags with given values. This is an exact match.
    """

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["EvaluationResultBatchCreateParams", "EvaluationResult", "EvaluationResultEvaluatedModelAttachment"]


class EvaluationResultBatchCreateParams(TypedDict, total=False):
    evaluation_results: Required[Iterable[EvaluationResult]]


class EvaluationResultEvaluatedModelAttachment(TypedDict, total=False):
    media_type: Required[str]

    url: Required[str]

    usage_type: Required[str]


_EvaluationResultReservedKeywords = TypedDict(
    "_EvaluationResultReservedKeywords",
    {
        "pass": Optional[bool],
    },
    total=False,
)


class EvaluationResult(_EvaluationResultReservedKeywords, total=False):
    evaluator_id: Required[str]
    """External evaluator identifier."""

    app: Optional[str]
    """Defaults to 'default' if `app` or `experiment_id` is not provided.

    Cannot be provided together with `experiment_id`.`
    """

    criteria: Optional[str]

    dataset_id: Optional[str]

    dataset_sample_id: Optional[int]

    evaluated_model_attachments: Optional[Iterable[EvaluationResultEvaluatedModelAttachment]]

    evaluated_model_gold_answer: Optional[str]

    evaluated_model_input: Optional[str]

    evaluated_model_name: Optional[str]
    """Name of the evaluated model. E.g. 'gpt-4o', 'my-assistant'."""

    evaluated_model_output: Optional[str]

    evaluated_model_params: Optional[Dict[str, Union[float, str, None]]]

    evaluated_model_provider: Optional[str]
    """Provider of the evaluated model. E.g. 'OpenAI', 'PatronusAI' etc."""

    evaluated_model_retrieved_context: Union[List[str], str, None]

    evaluated_model_selected_model: Optional[str]
    """ID/name of the base-model used by evaluated model/assistant.

    E.g. 'gpt-4o', 'llama3' etc.
    """

    evaluated_model_system_prompt: Optional[str]

    evaluation_duration: Optional[str]

    evaluation_metadata: Optional[object]

    experiment_id: Optional[str]

    explanation: Optional[str]

    explanation_duration: Optional[str]

    profile_name: Optional[str]
    """profile_name is deprecated. Please use 'criteria' field instead."""

    score_raw: Optional[float]

    tags: object
    """Tags are key-value pairs used to label resources"""

    text_output: Optional[str]

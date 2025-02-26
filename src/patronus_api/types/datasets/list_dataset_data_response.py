# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ListDatasetDataResponse", "Data"]


class Data(BaseModel):
    dataset_id: str

    evaluated_model_gold_answer: Optional[str] = None

    evaluated_model_input: Optional[str] = None

    evaluated_model_output: Optional[str] = None

    evaluated_model_retrieved_context: Optional[List[str]] = None

    evaluated_model_system_prompt: Optional[str] = None

    label: Optional[str] = None
    """The field is deprecated. Please use evaluated_model_gold_answer instead."""

    meta_evaluated_model_name: Optional[str] = None

    meta_evaluated_model_params: Optional[object] = None

    meta_evaluated_model_provider: Optional[str] = None

    meta_evaluated_model_selected_model: Optional[str] = None

    sid: int

    text: Optional[str] = None
    """The field is deprecated. Please use evaluated_model_input instead."""


class ListDatasetDataResponse(BaseModel):
    data: List[Data]

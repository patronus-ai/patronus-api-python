# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UpdateDatasetResponse", "Dataset"]


class Dataset(BaseModel):
    id: str
    """Unique identifier for the dataset."""

    created_at: datetime
    """The date and time when the dataset was created."""

    creation_date: date
    """The date when the dataset was created.

    This field is deprecated. Please use 'created_at' instead.
    """

    criteria: Optional[List[str]] = None

    description: Optional[str] = None
    """A brief overview or summary of the dataset's contents or purpose."""

    has_evaluated_model_gold_answers: Literal["none", "some", "all"]
    """Indicated Whether the dataset has evaluated model gold answers."""

    has_evaluated_model_inputs: Literal["none", "some", "all"]
    """Indicates whether the dataset has evaluated model inputs."""

    has_evaluated_model_outputs: Literal["none", "some", "all"]
    """Indicates whether the dataset has evaluated model outputs."""

    has_evaluated_model_retrieved_contexts: Literal["none", "some", "all"]
    """Indicates whether the dataset has evaluated model retrieved context."""

    has_evaluated_model_system_prompts: Literal["none", "some", "all"]
    """Indicates whether the dataset has evaluated model prompts."""

    labeled: bool
    """Indicates whether the dataset contains labeled samples."""

    name: str
    """The name of the dataset."""

    samples: int
    """The number of samples present in the dataset."""

    type: Literal["Patronus Managed", "User Managed"]

    use_case: Optional[str] = None


class UpdateDatasetResponse(BaseModel):
    id: str

    dataset: Dataset

    name: str

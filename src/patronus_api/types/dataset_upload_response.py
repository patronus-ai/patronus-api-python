# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .dataset import Dataset
from .._models import BaseModel

__all__ = ["DatasetUploadResponse"]


class DatasetUploadResponse(BaseModel):
    dataset: Dataset

    dataset_id: str

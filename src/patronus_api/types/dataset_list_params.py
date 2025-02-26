# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .dataset_type import DatasetType

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    type: Optional[DatasetType]

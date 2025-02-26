# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["DatasetUploadParams"]


class DatasetUploadParams(TypedDict, total=False):
    dataset_name: Required[str]

    file: Required[FileTypes]

    custom_field_mapping: Optional[str]

    dataset_description: Optional[str]

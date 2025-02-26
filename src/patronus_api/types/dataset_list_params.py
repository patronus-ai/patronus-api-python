# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["DatasetListParams"]


class DatasetListParams(TypedDict, total=False):
    type: Optional[Literal["Patronus Managed", "User Managed"]]

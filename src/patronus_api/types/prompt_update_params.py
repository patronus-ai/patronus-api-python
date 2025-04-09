# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromptUpdateParams"]


class PromptUpdateParams(TypedDict, total=False):
    project_id: Optional[str]

    project_name: Optional[str]

    description: Optional[str]

    body_name: Annotated[Optional[str], PropertyInfo(alias="name")]

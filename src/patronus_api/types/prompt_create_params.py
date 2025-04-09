# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["PromptCreateParams"]


class PromptCreateParams(TypedDict, total=False):
    body: Required[str]

    name: Required[str]

    description: Optional[str]

    labels: List[str]

    project_id: Optional[str]

    project_name: Optional[str]

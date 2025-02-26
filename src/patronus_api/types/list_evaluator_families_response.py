# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["ListEvaluatorFamiliesResponse", "EvaluatorFamily"]


class EvaluatorFamily(BaseModel):
    family_name: str

    optional_input_fields: List[str]

    profile_config_schema: Optional[Dict[str, object]] = None

    required_input_fields: List[str]


class ListEvaluatorFamiliesResponse(BaseModel):
    evaluator_families: List[EvaluatorFamily]

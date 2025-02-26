# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["AppResponse", "App"]


class App(BaseModel):
    name: str


class AppResponse(BaseModel):
    apps: List[App]

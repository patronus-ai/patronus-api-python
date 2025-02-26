# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from .._models import BaseModel

__all__ = ["UpdateDatasetResponse"]


class UpdateDatasetResponse(BaseModel):
    id: str

    dataset: object

    name: str

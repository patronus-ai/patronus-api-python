# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types.datasets import ListDatasetDataResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestData:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: PatronusAPI) -> None:
        data = client.datasets.data.retrieve(
            "id",
        )
        assert_matches_type(ListDatasetDataResponse, data, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PatronusAPI) -> None:
        response = client.datasets.data.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = response.parse()
        assert_matches_type(ListDatasetDataResponse, data, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PatronusAPI) -> None:
        with client.datasets.data.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = response.parse()
            assert_matches_type(ListDatasetDataResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.data.with_raw_response.retrieve(
                "",
            )


class TestAsyncData:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        data = await async_client.datasets.data.retrieve(
            "id",
        )
        assert_matches_type(ListDatasetDataResponse, data, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.data.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        data = await response.parse()
        assert_matches_type(ListDatasetDataResponse, data, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.data.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            data = await response.parse()
            assert_matches_type(ListDatasetDataResponse, data, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.data.with_raw_response.retrieve(
                "",
            )

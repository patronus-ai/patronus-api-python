# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import (
    GetDatasetsResponse,
    ListDatasetsResponse,
    CreateDatasetResponse,
    UpdateDatasetResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PatronusAPI) -> None:
        dataset = client.datasets.create(
            dataset_name="x",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PatronusAPI) -> None:
        dataset = client.datasets.create(
            dataset_name="x",
            file=b"raw file contents",
            custom_field_mapping="custom_field_mapping",
            dataset_description="dataset_description",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.create(
            dataset_name="x",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.create(
            dataset_name="x",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PatronusAPI) -> None:
        dataset = client.datasets.retrieve(
            "id",
        )
        assert_matches_type(GetDatasetsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(GetDatasetsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(GetDatasetsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_update(self, client: PatronusAPI) -> None:
        dataset = client.datasets.update(
            dataset_id="dataset_id",
        )
        assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: PatronusAPI) -> None:
        dataset = client.datasets.update(
            dataset_id="dataset_id",
            description="description",
            name="x",
        )
        assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.update(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.update(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @parametrize
    def test_method_list(self, client: PatronusAPI) -> None:
        dataset = client.datasets.list()
        assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: PatronusAPI) -> None:
        dataset = client.datasets.list(
            type="Patronus Managed",
        )
        assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PatronusAPI) -> None:
        dataset = client.datasets.delete(
            "id",
        )
        assert dataset is None

    @parametrize
    def test_raw_response_delete(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @parametrize
    def test_streaming_response_delete(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.delete(
                "",
            )


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.create(
            dataset_name="x",
            file=b"raw file contents",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.create(
            dataset_name="x",
            file=b"raw file contents",
            custom_field_mapping="custom_field_mapping",
            dataset_description="dataset_description",
        )
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.create(
            dataset_name="x",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.create(
            dataset_name="x",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(CreateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.retrieve(
            "id",
        )
        assert_matches_type(GetDatasetsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(GetDatasetsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(GetDatasetsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="dataset_id",
        )
        assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="dataset_id",
            description="description",
            name="x",
        )
        assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.update(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.update(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(UpdateDatasetResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.list(
            type="Patronus Managed",
        )
        assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(ListDatasetsResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.delete(
            "id",
        )
        assert dataset is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.delete(
                "",
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import (
    DatasetListResponse,
    DatasetUpdateResponse,
    DatasetUploadResponse,
    DatasetListDataResponse,
    DatasetRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: PatronusAPI) -> None:
        dataset = client.datasets.retrieve(
            "id",
        )
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_retrieve(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: PatronusAPI) -> None:
        dataset = client.datasets.update(
            dataset_id="dataset_id",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: PatronusAPI) -> None:
        dataset = client.datasets.update(
            dataset_id="dataset_id",
            description="description",
            name="x",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.update(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.update(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: PatronusAPI) -> None:
        dataset = client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: PatronusAPI) -> None:
        dataset = client.datasets.list(
            type="Patronus Managed",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: PatronusAPI) -> None:
        dataset = client.datasets.delete(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_download_csv(self, client: PatronusAPI) -> None:
        dataset = client.datasets.download_csv(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_download_csv(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.download_csv(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_download_csv(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.download_csv(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_download_csv(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.download_csv(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_download_jsonl(self, client: PatronusAPI) -> None:
        dataset = client.datasets.download_jsonl(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_download_jsonl(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.download_jsonl(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_download_jsonl(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.download_jsonl(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_download_jsonl(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.download_jsonl(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list_data(self, client: PatronusAPI) -> None:
        dataset = client.datasets.list_data(
            "id",
        )
        assert_matches_type(DatasetListDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_data(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.list_data(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_data(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.list_data(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListDataResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_data(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.datasets.with_raw_response.list_data(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_upload(self, client: PatronusAPI) -> None:
        dataset = client.datasets.upload(
            dataset_name="x",
            file=b"raw file contents",
        )
        assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_upload_with_all_params(self, client: PatronusAPI) -> None:
        dataset = client.datasets.upload(
            dataset_name="x",
            file=b"raw file contents",
            custom_field_mapping="custom_field_mapping",
            dataset_description="dataset_description",
        )
        assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_upload(self, client: PatronusAPI) -> None:
        response = client.datasets.with_raw_response.upload(
            dataset_name="x",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_upload(self, client: PatronusAPI) -> None:
        with client.datasets.with_streaming_response.upload(
            dataset_name="x",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.retrieve(
            "id",
        )
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrieveResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="dataset_id",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="dataset_id",
            description="description",
            name="x",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.update(
            dataset_id="dataset_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.update(
            dataset_id="dataset_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.list(
            type="Patronus Managed",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.delete(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip()
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_download_csv(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.download_csv(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_download_csv(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.download_csv(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_download_csv(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.download_csv(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_download_csv(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.download_csv(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_download_jsonl(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.download_jsonl(
            "id",
        )
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_download_jsonl(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.download_jsonl(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert dataset is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_download_jsonl(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.download_jsonl(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert dataset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_download_jsonl(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.download_jsonl(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_data(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.list_data(
            "id",
        )
        assert_matches_type(DatasetListDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_data(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.list_data(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListDataResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_data(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.list_data(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListDataResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_data(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.datasets.with_raw_response.list_data(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.upload(
            dataset_name="x",
            file=b"raw file contents",
        )
        assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        dataset = await async_client.datasets.upload(
            dataset_name="x",
            file=b"raw file contents",
            custom_field_mapping="custom_field_mapping",
            dataset_description="dataset_description",
        )
        assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.datasets.with_raw_response.upload(
            dataset_name="x",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.datasets.with_streaming_response.upload(
            dataset_name="x",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetUploadResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

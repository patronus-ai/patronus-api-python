# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import (
    ListPairwiseAnnotationsResponse,
    CreatePairwiseAnnotationResponse,
    GetBatchPairwiseAnnotationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPairwiseAnnotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PatronusAPI) -> None:
        pairwise_annotation = client.pairwise_annotations.create(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_a_score=0,
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_score=0,
            name="x",
        )
        assert_matches_type(CreatePairwiseAnnotationResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PatronusAPI) -> None:
        response = client.pairwise_annotations.with_raw_response.create(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_a_score=0,
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_score=0,
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = response.parse()
        assert_matches_type(CreatePairwiseAnnotationResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PatronusAPI) -> None:
        with client.pairwise_annotations.with_streaming_response.create(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_a_score=0,
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_score=0,
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = response.parse()
            assert_matches_type(CreatePairwiseAnnotationResponse, pairwise_annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: PatronusAPI) -> None:
        pairwise_annotation = client.pairwise_annotations.list()
        assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: PatronusAPI) -> None:
        pairwise_annotation = client.pairwise_annotations.list(
            experiment_id=[0],
            limit=1000,
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            offset=0,
            project_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PatronusAPI) -> None:
        response = client.pairwise_annotations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = response.parse()
        assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PatronusAPI) -> None:
        with client.pairwise_annotations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = response.parse()
            assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PatronusAPI) -> None:
        pairwise_annotation = client.pairwise_annotations.delete(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert pairwise_annotation is None

    @parametrize
    def test_raw_response_delete(self, client: PatronusAPI) -> None:
        response = client.pairwise_annotations.with_raw_response.delete(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = response.parse()
        assert pairwise_annotation is None

    @parametrize
    def test_streaming_response_delete(self, client: PatronusAPI) -> None:
        with client.pairwise_annotations.with_streaming_response.delete(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = response.parse()
            assert pairwise_annotation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_batch(self, client: PatronusAPI) -> None:
        pairwise_annotation = client.pairwise_annotations.get_batch(
            pairwise_annotations=[
                {
                    "log_a_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "log_b_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(GetBatchPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_raw_response_get_batch(self, client: PatronusAPI) -> None:
        response = client.pairwise_annotations.with_raw_response.get_batch(
            pairwise_annotations=[
                {
                    "log_a_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "log_b_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = response.parse()
        assert_matches_type(GetBatchPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    def test_streaming_response_get_batch(self, client: PatronusAPI) -> None:
        with client.pairwise_annotations.with_streaming_response.get_batch(
            pairwise_annotations=[
                {
                    "log_a_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "log_b_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = response.parse()
            assert_matches_type(GetBatchPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPairwiseAnnotations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPatronusAPI) -> None:
        pairwise_annotation = await async_client.pairwise_annotations.create(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_a_score=0,
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_score=0,
            name="x",
        )
        assert_matches_type(CreatePairwiseAnnotationResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.pairwise_annotations.with_raw_response.create(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_a_score=0,
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_score=0,
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = await response.parse()
        assert_matches_type(CreatePairwiseAnnotationResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.pairwise_annotations.with_streaming_response.create(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_a_score=0,
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_score=0,
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = await response.parse()
            assert_matches_type(CreatePairwiseAnnotationResponse, pairwise_annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncPatronusAPI) -> None:
        pairwise_annotation = await async_client.pairwise_annotations.list()
        assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        pairwise_annotation = await async_client.pairwise_annotations.list(
            experiment_id=[0],
            limit=1000,
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
            offset=0,
            project_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.pairwise_annotations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = await response.parse()
        assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.pairwise_annotations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = await response.parse()
            assert_matches_type(ListPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPatronusAPI) -> None:
        pairwise_annotation = await async_client.pairwise_annotations.delete(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert pairwise_annotation is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.pairwise_annotations.with_raw_response.delete(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = await response.parse()
        assert pairwise_annotation is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.pairwise_annotations.with_streaming_response.delete(
            log_a_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_b_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = await response.parse()
            assert pairwise_annotation is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_batch(self, async_client: AsyncPatronusAPI) -> None:
        pairwise_annotation = await async_client.pairwise_annotations.get_batch(
            pairwise_annotations=[
                {
                    "log_a_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "log_b_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                }
            ],
        )
        assert_matches_type(GetBatchPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_raw_response_get_batch(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.pairwise_annotations.with_raw_response.get_batch(
            pairwise_annotations=[
                {
                    "log_a_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "log_b_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pairwise_annotation = await response.parse()
        assert_matches_type(GetBatchPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

    @parametrize
    async def test_streaming_response_get_batch(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.pairwise_annotations.with_streaming_response.get_batch(
            pairwise_annotations=[
                {
                    "log_a_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "log_b_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "name": "name",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pairwise_annotation = await response.parse()
            assert_matches_type(GetBatchPairwiseAnnotationsResponse, pairwise_annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

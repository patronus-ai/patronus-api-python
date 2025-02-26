# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import (
    EvaluationResultSearchResponse,
    EvaluationResultListTagsResponse,
    EvaluationResultRetrieveResponse,
    EvaluationResultCreateBatchResponse,
)
from patronus_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.retrieve(
            0,
        )
        assert_matches_type(EvaluationResultRetrieveResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(EvaluationResultRetrieveResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(EvaluationResultRetrieveResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_create_batch(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.create_batch(
            evaluation_results=[{"evaluator_id": "evaluator_id"}],
        )
        assert_matches_type(EvaluationResultCreateBatchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create_batch(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.create_batch(
            evaluation_results=[{"evaluator_id": "evaluator_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(EvaluationResultCreateBatchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create_batch(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.create_batch(
            evaluation_results=[{"evaluator_id": "evaluator_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(EvaluationResultCreateBatchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_tags(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.list_tags()
        assert_matches_type(EvaluationResultListTagsResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_tags(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.list_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(EvaluationResultListTagsResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_tags(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.list_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(EvaluationResultListTagsResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.search()
        assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.search(
            after_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            after_id=0,
            app="app",
            before_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            before_id=0,
            criteria="criteria",
            dataset_id="dataset_id",
            evaluation_feedback_status="given",
            evaluation_run_id="evaluation_run_id",
            evaluation_type="patronus_evaluation",
            evaluator_family="evaluator_family",
            evaluator_id="evaluator_id",
            evaluator_profile_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_id="experiment_id",
            explain=True,
            explain_strategy="never",
            favorite=True,
            limit=1,
            order="created_at",
            pass_=True,
            profile_name="profile_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_raw_max=0,
            score_raw_min=0,
            tags={"foo": "string"},
        )
        assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluationResults:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.retrieve(
            0,
        )
        assert_matches_type(EvaluationResultRetrieveResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(EvaluationResultRetrieveResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(EvaluationResultRetrieveResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_batch(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.create_batch(
            evaluation_results=[{"evaluator_id": "evaluator_id"}],
        )
        assert_matches_type(EvaluationResultCreateBatchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create_batch(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.create_batch(
            evaluation_results=[{"evaluator_id": "evaluator_id"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(EvaluationResultCreateBatchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create_batch(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.create_batch(
            evaluation_results=[{"evaluator_id": "evaluator_id"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(EvaluationResultCreateBatchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_tags(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.list_tags()
        assert_matches_type(EvaluationResultListTagsResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_tags(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.list_tags()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(EvaluationResultListTagsResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_tags(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.list_tags() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(EvaluationResultListTagsResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.search()
        assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.search(
            after_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            after_id=0,
            app="app",
            before_datetime=parse_datetime("2019-12-27T18:11:19.117Z"),
            before_id=0,
            criteria="criteria",
            dataset_id="dataset_id",
            evaluation_feedback_status="given",
            evaluation_run_id="evaluation_run_id",
            evaluation_type="patronus_evaluation",
            evaluator_family="evaluator_family",
            evaluator_id="evaluator_id",
            evaluator_profile_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            experiment_id="experiment_id",
            explain=True,
            explain_strategy="never",
            favorite=True,
            limit=1,
            order="created_at",
            pass_=True,
            profile_name="profile_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_raw_max=0,
            score_raw_min=0,
            tags={"foo": "string"},
        )
        assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(EvaluationResultSearchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

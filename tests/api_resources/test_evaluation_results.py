# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import (
    GetEvaluationResult,
    EvaluateResultSearchResponse,
    CreateEvaluationResultsBatchResponse,
)
from patronus_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationResults:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.retrieve(
            0,
        )
        assert_matches_type(GetEvaluationResult, evaluation_result, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(GetEvaluationResult, evaluation_result, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(GetEvaluationResult, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_batch_create(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.batch_create(
            evaluation_results=[{}],
        )
        assert_matches_type(CreateEvaluationResultsBatchResponse, evaluation_result, path=["response"])

    @parametrize
    def test_raw_response_batch_create(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.batch_create(
            evaluation_results=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(CreateEvaluationResultsBatchResponse, evaluation_result, path=["response"])

    @parametrize
    def test_streaming_response_batch_create(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.batch_create(
            evaluation_results=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(CreateEvaluationResultsBatchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_evaluation_feedback(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.evaluation_feedback(
            id=0,
            feedback="positive",
        )
        assert evaluation_result is None

    @parametrize
    def test_raw_response_evaluation_feedback(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.evaluation_feedback(
            id=0,
            feedback="positive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert evaluation_result is None

    @parametrize
    def test_streaming_response_evaluation_feedback(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.evaluation_feedback(
            id=0,
            feedback="positive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_favorite(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.favorite(
            0,
        )
        assert evaluation_result is None

    @parametrize
    def test_raw_response_favorite(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.favorite(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert evaluation_result is None

    @parametrize
    def test_streaming_response_favorite(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.favorite(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_evaluation_feedback(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.remove_evaluation_feedback(
            0,
        )
        assert evaluation_result is None

    @parametrize
    def test_raw_response_remove_evaluation_feedback(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.remove_evaluation_feedback(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert evaluation_result is None

    @parametrize
    def test_streaming_response_remove_evaluation_feedback(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.remove_evaluation_feedback(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.search()
        assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

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
            explain_strategy={},
            favorite=True,
            limit=1,
            order={},
            pass_=True,
            profile_name="profile_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_raw_max=0,
            score_raw_min=0,
            tags={"foo": "string"},
        )
        assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unfavorite(self, client: PatronusAPI) -> None:
        evaluation_result = client.evaluation_results.unfavorite(
            0,
        )
        assert evaluation_result is None

    @parametrize
    def test_raw_response_unfavorite(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.with_raw_response.unfavorite(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = response.parse()
        assert evaluation_result is None

    @parametrize
    def test_streaming_response_unfavorite(self, client: PatronusAPI) -> None:
        with client.evaluation_results.with_streaming_response.unfavorite(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluationResults:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.retrieve(
            0,
        )
        assert_matches_type(GetEvaluationResult, evaluation_result, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(GetEvaluationResult, evaluation_result, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(GetEvaluationResult, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_batch_create(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.batch_create(
            evaluation_results=[{}],
        )
        assert_matches_type(CreateEvaluationResultsBatchResponse, evaluation_result, path=["response"])

    @parametrize
    async def test_raw_response_batch_create(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.batch_create(
            evaluation_results=[{}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(CreateEvaluationResultsBatchResponse, evaluation_result, path=["response"])

    @parametrize
    async def test_streaming_response_batch_create(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.batch_create(
            evaluation_results=[{}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(CreateEvaluationResultsBatchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_evaluation_feedback(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.evaluation_feedback(
            id=0,
            feedback="positive",
        )
        assert evaluation_result is None

    @parametrize
    async def test_raw_response_evaluation_feedback(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.evaluation_feedback(
            id=0,
            feedback="positive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert evaluation_result is None

    @parametrize
    async def test_streaming_response_evaluation_feedback(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.evaluation_feedback(
            id=0,
            feedback="positive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_favorite(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.favorite(
            0,
        )
        assert evaluation_result is None

    @parametrize
    async def test_raw_response_favorite(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.favorite(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert evaluation_result is None

    @parametrize
    async def test_streaming_response_favorite(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.favorite(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_evaluation_feedback(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.remove_evaluation_feedback(
            0,
        )
        assert evaluation_result is None

    @parametrize
    async def test_raw_response_remove_evaluation_feedback(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.remove_evaluation_feedback(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert evaluation_result is None

    @parametrize
    async def test_streaming_response_remove_evaluation_feedback(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.remove_evaluation_feedback(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.search()
        assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

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
            explain_strategy={},
            favorite=True,
            limit=1,
            order={},
            pass_=True,
            profile_name="profile_name",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score_raw_max=0,
            score_raw_min=0,
            tags={"foo": "string"},
        )
        assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert_matches_type(EvaluateResultSearchResponse, evaluation_result, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unfavorite(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_result = await async_client.evaluation_results.unfavorite(
            0,
        )
        assert evaluation_result is None

    @parametrize
    async def test_raw_response_unfavorite(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.with_raw_response.unfavorite(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_result = await response.parse()
        assert evaluation_result is None

    @parametrize
    async def test_streaming_response_unfavorite(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.with_streaming_response.unfavorite(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_result = await response.parse()
            assert evaluation_result is None

        assert cast(Any, response.is_closed) is True

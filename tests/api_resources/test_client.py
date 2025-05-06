# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import (
    WhoamiResponse,
    EvaluateResponse,
    ListAppsResponse,
    ListEvaluatorsResponse,
    ListEvaluatorFamiliesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClient:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_evaluate(self, client: PatronusAPI) -> None:
        client_ = client.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )
        assert_matches_type(EvaluateResponse, client_, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: PatronusAPI) -> None:
        client_ = client.evaluate(
            evaluators=[
                {
                    "evaluator": "evaluator",
                    "criteria": "x",
                    "explain_strategy": "never",
                }
            ],
            app="xx",
            capture="all",
            confidence_interval_strategy="none",
            dataset_id="dataset_id",
            dataset_sample_id="dataset_sample_id",
            evaluated_model_attachments=[
                {
                    "media_type": "image/jpeg",
                    "url": "https://example.com",
                    "usage_type": "evaluated_model_system_prompt",
                }
            ],
            experiment_id="experiment_id",
            gold_answer="gold_answer",
            log_id="log_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            span_id="span_id",
            system_prompt="system_prompt",
            tags={},
            task_context=["string"],
            task_input="task_input",
            task_output="task_output",
            trace_id="trace_id",
        )
        assert_matches_type(EvaluateResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: PatronusAPI) -> None:
        response = client.with_raw_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(EvaluateResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: PatronusAPI) -> None:
        with client.with_streaming_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(EvaluateResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_apps(self, client: PatronusAPI) -> None:
        client_ = client.list_apps()
        assert_matches_type(ListAppsResponse, client_, path=["response"])

    @parametrize
    def test_method_list_apps_with_all_params(self, client: PatronusAPI) -> None:
        client_ = client.list_apps(
            limit=0,
            offset=0,
        )
        assert_matches_type(ListAppsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_list_apps(self, client: PatronusAPI) -> None:
        response = client.with_raw_response.list_apps()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ListAppsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_list_apps(self, client: PatronusAPI) -> None:
        with client.with_streaming_response.list_apps() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ListAppsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_evaluator_families(self, client: PatronusAPI) -> None:
        client_ = client.list_evaluator_families()
        assert_matches_type(ListEvaluatorFamiliesResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_list_evaluator_families(self, client: PatronusAPI) -> None:
        response = client.with_raw_response.list_evaluator_families()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ListEvaluatorFamiliesResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_list_evaluator_families(self, client: PatronusAPI) -> None:
        with client.with_streaming_response.list_evaluator_families() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ListEvaluatorFamiliesResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_evaluators(self, client: PatronusAPI) -> None:
        client_ = client.list_evaluators()
        assert_matches_type(ListEvaluatorsResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_list_evaluators(self, client: PatronusAPI) -> None:
        response = client.with_raw_response.list_evaluators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(ListEvaluatorsResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_list_evaluators(self, client: PatronusAPI) -> None:
        with client.with_streaming_response.list_evaluators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(ListEvaluatorsResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_whoami(self, client: PatronusAPI) -> None:
        client_ = client.whoami()
        assert_matches_type(WhoamiResponse, client_, path=["response"])

    @parametrize
    def test_raw_response_whoami(self, client: PatronusAPI) -> None:
        response = client.with_raw_response.whoami()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_ = response.parse()
        assert_matches_type(WhoamiResponse, client_, path=["response"])

    @parametrize
    def test_streaming_response_whoami(self, client: PatronusAPI) -> None:
        with client.with_streaming_response.whoami() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_ = response.parse()
            assert_matches_type(WhoamiResponse, client_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClient:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_evaluate(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )
        assert_matches_type(EvaluateResponse, client, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.evaluate(
            evaluators=[
                {
                    "evaluator": "evaluator",
                    "criteria": "x",
                    "explain_strategy": "never",
                }
            ],
            app="xx",
            capture="all",
            confidence_interval_strategy="none",
            dataset_id="dataset_id",
            dataset_sample_id="dataset_sample_id",
            evaluated_model_attachments=[
                {
                    "media_type": "image/jpeg",
                    "url": "https://example.com",
                    "usage_type": "evaluated_model_system_prompt",
                }
            ],
            experiment_id="experiment_id",
            gold_answer="gold_answer",
            log_id="log_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            span_id="span_id",
            system_prompt="system_prompt",
            tags={},
            task_context=["string"],
            task_input="task_input",
            task_output="task_output",
            trace_id="trace_id",
        )
        assert_matches_type(EvaluateResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.with_raw_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(EvaluateResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.with_streaming_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(EvaluateResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_apps(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.list_apps()
        assert_matches_type(ListAppsResponse, client, path=["response"])

    @parametrize
    async def test_method_list_apps_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.list_apps(
            limit=0,
            offset=0,
        )
        assert_matches_type(ListAppsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_list_apps(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.with_raw_response.list_apps()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ListAppsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_list_apps(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.with_streaming_response.list_apps() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ListAppsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_evaluator_families(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.list_evaluator_families()
        assert_matches_type(ListEvaluatorFamiliesResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_list_evaluator_families(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.with_raw_response.list_evaluator_families()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ListEvaluatorFamiliesResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_list_evaluator_families(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.with_streaming_response.list_evaluator_families() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ListEvaluatorFamiliesResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_evaluators(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.list_evaluators()
        assert_matches_type(ListEvaluatorsResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_list_evaluators(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.with_raw_response.list_evaluators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(ListEvaluatorsResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_list_evaluators(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.with_streaming_response.list_evaluators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(ListEvaluatorsResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_whoami(self, async_client: AsyncPatronusAPI) -> None:
        client = await async_client.whoami()
        assert_matches_type(WhoamiResponse, client, path=["response"])

    @parametrize
    async def test_raw_response_whoami(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.with_raw_response.whoami()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client = await response.parse()
        assert_matches_type(WhoamiResponse, client, path=["response"])

    @parametrize
    async def test_streaming_response_whoami(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.with_streaming_response.whoami() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client = await response.parse()
            assert_matches_type(WhoamiResponse, client, path=["response"])

        assert cast(Any, response.is_closed) is True

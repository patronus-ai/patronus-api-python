# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import EvaluateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_evaluate(self, client: PatronusAPI) -> None:
        evaluation = client.evaluations.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )
        assert_matches_type(EvaluateResponse, evaluation, path=["response"])

    @parametrize
    def test_method_evaluate_with_all_params(self, client: PatronusAPI) -> None:
        evaluation = client.evaluations.evaluate(
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
            dataset_sample_id=0,
            evaluated_model_attachments=[
                {
                    "media_type": "image/jpeg",
                    "url": "https://example.com",
                    "usage_type": "evaluated_model_system_prompt",
                }
            ],
            evaluated_model_gold_answer="evaluated_model_gold_answer",
            evaluated_model_input="evaluated_model_input",
            evaluated_model_output="evaluated_model_output",
            evaluated_model_retrieved_context=["string"],
            evaluated_model_system_prompt="evaluated_model_system_prompt",
            experiment_id="experiment_id",
            log_id="log_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            span_id="span_id",
            tags={},
            trace_id="trace_id",
        )
        assert_matches_type(EvaluateResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_evaluate(self, client: PatronusAPI) -> None:
        response = client.evaluations.with_raw_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluateResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_evaluate(self, client: PatronusAPI) -> None:
        with client.evaluations.with_streaming_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_evaluate(self, async_client: AsyncPatronusAPI) -> None:
        evaluation = await async_client.evaluations.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )
        assert_matches_type(EvaluateResponse, evaluation, path=["response"])

    @parametrize
    async def test_method_evaluate_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        evaluation = await async_client.evaluations.evaluate(
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
            dataset_sample_id=0,
            evaluated_model_attachments=[
                {
                    "media_type": "image/jpeg",
                    "url": "https://example.com",
                    "usage_type": "evaluated_model_system_prompt",
                }
            ],
            evaluated_model_gold_answer="evaluated_model_gold_answer",
            evaluated_model_input="evaluated_model_input",
            evaluated_model_output="evaluated_model_output",
            evaluated_model_retrieved_context=["string"],
            evaluated_model_system_prompt="evaluated_model_system_prompt",
            experiment_id="experiment_id",
            log_id="log_id",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_name="project_name",
            span_id="span_id",
            tags={},
            trace_id="trace_id",
        )
        assert_matches_type(EvaluateResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_evaluate(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluations.with_raw_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluateResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_evaluate(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluations.with_streaming_response.evaluate(
            evaluators=[{"evaluator": "evaluator"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluateResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

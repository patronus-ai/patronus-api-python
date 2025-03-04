# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from patronus_api import PatronusAPI, AsyncPatronusAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: PatronusAPI) -> None:
        evaluation_feedback = client.evaluation_results.evaluation_feedback.delete(
            0,
        )
        assert evaluation_feedback is None

    @parametrize
    def test_raw_response_delete(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.evaluation_feedback.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_feedback = response.parse()
        assert evaluation_feedback is None

    @parametrize
    def test_streaming_response_delete(self, client: PatronusAPI) -> None:
        with client.evaluation_results.evaluation_feedback.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_feedback = response.parse()
            assert evaluation_feedback is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit(self, client: PatronusAPI) -> None:
        evaluation_feedback = client.evaluation_results.evaluation_feedback.submit(
            id=0,
            feedback="positive",
        )
        assert evaluation_feedback is None

    @parametrize
    def test_raw_response_submit(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.evaluation_feedback.with_raw_response.submit(
            id=0,
            feedback="positive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_feedback = response.parse()
        assert evaluation_feedback is None

    @parametrize
    def test_streaming_response_submit(self, client: PatronusAPI) -> None:
        with client.evaluation_results.evaluation_feedback.with_streaming_response.submit(
            id=0,
            feedback="positive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_feedback = response.parse()
            assert evaluation_feedback is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluationFeedback:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_feedback = await async_client.evaluation_results.evaluation_feedback.delete(
            0,
        )
        assert evaluation_feedback is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.evaluation_feedback.with_raw_response.delete(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_feedback = await response.parse()
        assert evaluation_feedback is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.evaluation_feedback.with_streaming_response.delete(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_feedback = await response.parse()
            assert evaluation_feedback is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit(self, async_client: AsyncPatronusAPI) -> None:
        evaluation_feedback = await async_client.evaluation_results.evaluation_feedback.submit(
            id=0,
            feedback="positive",
        )
        assert evaluation_feedback is None

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.evaluation_feedback.with_raw_response.submit(
            id=0,
            feedback="positive",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_feedback = await response.parse()
        assert evaluation_feedback is None

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.evaluation_feedback.with_streaming_response.submit(
            id=0,
            feedback="positive",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_feedback = await response.parse()
            assert evaluation_feedback is None

        assert cast(Any, response.is_closed) is True

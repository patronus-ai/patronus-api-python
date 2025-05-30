# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types.otel import SpanSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSpans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search(self, client: PatronusAPI) -> None:
        span = client.otel.spans.search()
        assert_matches_type(SpanSearchResponse, span, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: PatronusAPI) -> None:
        span = client.otel.spans.search(
            filters=[
                {
                    "and_": [{}],
                    "field": "field",
                    "op": "eq",
                    "or_": [{}],
                    "value": {},
                }
            ],
            limit=1,
            order="timestamp asc",
        )
        assert_matches_type(SpanSearchResponse, span, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: PatronusAPI) -> None:
        response = client.otel.spans.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = response.parse()
        assert_matches_type(SpanSearchResponse, span, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: PatronusAPI) -> None:
        with client.otel.spans.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = response.parse()
            assert_matches_type(SpanSearchResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSpans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_search(self, async_client: AsyncPatronusAPI) -> None:
        span = await async_client.otel.spans.search()
        assert_matches_type(SpanSearchResponse, span, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        span = await async_client.otel.spans.search(
            filters=[
                {
                    "and_": [{}],
                    "field": "field",
                    "op": "eq",
                    "or_": [{}],
                    "value": {},
                }
            ],
            limit=1,
            order="timestamp asc",
        )
        assert_matches_type(SpanSearchResponse, span, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.otel.spans.with_raw_response.search()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        span = await response.parse()
        assert_matches_type(SpanSearchResponse, span, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.otel.spans.with_streaming_response.search() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            span = await response.parse()
            assert_matches_type(SpanSearchResponse, span, path=["response"])

        assert cast(Any, response.is_closed) is True

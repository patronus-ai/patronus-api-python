# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import ListEvaluatorFamilyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluatorFamilies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: PatronusAPI) -> None:
        evaluator_family = client.evaluator_families.list()
        assert_matches_type(ListEvaluatorFamilyResponse, evaluator_family, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PatronusAPI) -> None:
        response = client.evaluator_families.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluator_family = response.parse()
        assert_matches_type(ListEvaluatorFamilyResponse, evaluator_family, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PatronusAPI) -> None:
        with client.evaluator_families.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluator_family = response.parse()
            assert_matches_type(ListEvaluatorFamilyResponse, evaluator_family, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncEvaluatorFamilies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncPatronusAPI) -> None:
        evaluator_family = await async_client.evaluator_families.list()
        assert_matches_type(ListEvaluatorFamilyResponse, evaluator_family, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluator_families.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluator_family = await response.parse()
        assert_matches_type(ListEvaluatorFamilyResponse, evaluator_family, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluator_families.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluator_family = await response.parse()
            assert_matches_type(ListEvaluatorFamilyResponse, evaluator_family, path=["response"])

        assert cast(Any, response.is_closed) is True

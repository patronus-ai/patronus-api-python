# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types import AnnotateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAnnotations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_annotate(self, client: PatronusAPI) -> None:
        annotation = client.annotations.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotateResponse, annotation, path=["response"])

    @parametrize
    def test_method_annotate_with_all_params(self, client: PatronusAPI) -> None:
        annotation = client.annotations.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
            value_pass=True,
            value_score=0,
            value_text="value_text",
        )
        assert_matches_type(AnnotateResponse, annotation, path=["response"])

    @parametrize
    def test_raw_response_annotate(self, client: PatronusAPI) -> None:
        response = client.annotations.with_raw_response.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = response.parse()
        assert_matches_type(AnnotateResponse, annotation, path=["response"])

    @parametrize
    def test_streaming_response_annotate(self, client: PatronusAPI) -> None:
        with client.annotations.with_streaming_response.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = response.parse()
            assert_matches_type(AnnotateResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAnnotations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_annotate(self, async_client: AsyncPatronusAPI) -> None:
        annotation = await async_client.annotations.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AnnotateResponse, annotation, path=["response"])

    @parametrize
    async def test_method_annotate_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        annotation = await async_client.annotations.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            explanation="explanation",
            value_pass=True,
            value_score=0,
            value_text="value_text",
        )
        assert_matches_type(AnnotateResponse, annotation, path=["response"])

    @parametrize
    async def test_raw_response_annotate(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.annotations.with_raw_response.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        annotation = await response.parse()
        assert_matches_type(AnnotateResponse, annotation, path=["response"])

    @parametrize
    async def test_streaming_response_annotate(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.annotations.with_streaming_response.annotate(
            annotation_criteria_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            log_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            annotation = await response.parse()
            assert_matches_type(AnnotateResponse, annotation, path=["response"])

        assert cast(Any, response.is_closed) is True

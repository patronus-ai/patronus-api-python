# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from patronus_api import PatronusAPI, AsyncPatronusAPI
from patronus_api.types.evaluator_criteria import AddEvaluatorCriteriaRevision

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRevision:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PatronusAPI) -> None:
        revision = client.evaluator_criteria.revision.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
        )
        assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PatronusAPI) -> None:
        revision = client.evaluator_criteria.revision.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            description="description",
        )
        assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PatronusAPI) -> None:
        response = client.evaluator_criteria.revision.with_raw_response.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = response.parse()
        assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PatronusAPI) -> None:
        with client.evaluator_criteria.revision.with_streaming_response.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = response.parse()
            assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: PatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `public_id` but received ''"):
            client.evaluator_criteria.revision.with_raw_response.create(
                public_id="",
                config={},
            )


class TestAsyncRevision:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPatronusAPI) -> None:
        revision = await async_client.evaluator_criteria.revision.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
        )
        assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPatronusAPI) -> None:
        revision = await async_client.evaluator_criteria.revision.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
            description="description",
        )
        assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluator_criteria.revision.with_raw_response.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        revision = await response.parse()
        assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluator_criteria.revision.with_streaming_response.create(
            public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            revision = await response.parse()
            assert_matches_type(AddEvaluatorCriteriaRevision, revision, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncPatronusAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `public_id` but received ''"):
            await async_client.evaluator_criteria.revision.with_raw_response.create(
                public_id="",
                config={},
            )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from patronus_api import PatronusAPI, AsyncPatronusAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFavorite:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_mark(self, client: PatronusAPI) -> None:
        favorite = client.evaluation_results.favorite.mark(
            0,
        )
        assert favorite is None

    @parametrize
    def test_raw_response_mark(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.favorite.with_raw_response.mark(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = response.parse()
        assert favorite is None

    @parametrize
    def test_streaming_response_mark(self, client: PatronusAPI) -> None:
        with client.evaluation_results.favorite.with_streaming_response.mark(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = response.parse()
            assert favorite is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unmark(self, client: PatronusAPI) -> None:
        favorite = client.evaluation_results.favorite.unmark(
            0,
        )
        assert favorite is None

    @parametrize
    def test_raw_response_unmark(self, client: PatronusAPI) -> None:
        response = client.evaluation_results.favorite.with_raw_response.unmark(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = response.parse()
        assert favorite is None

    @parametrize
    def test_streaming_response_unmark(self, client: PatronusAPI) -> None:
        with client.evaluation_results.favorite.with_streaming_response.unmark(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = response.parse()
            assert favorite is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFavorite:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_mark(self, async_client: AsyncPatronusAPI) -> None:
        favorite = await async_client.evaluation_results.favorite.mark(
            0,
        )
        assert favorite is None

    @parametrize
    async def test_raw_response_mark(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.favorite.with_raw_response.mark(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = await response.parse()
        assert favorite is None

    @parametrize
    async def test_streaming_response_mark(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.favorite.with_streaming_response.mark(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = await response.parse()
            assert favorite is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unmark(self, async_client: AsyncPatronusAPI) -> None:
        favorite = await async_client.evaluation_results.favorite.unmark(
            0,
        )
        assert favorite is None

    @parametrize
    async def test_raw_response_unmark(self, async_client: AsyncPatronusAPI) -> None:
        response = await async_client.evaluation_results.favorite.with_raw_response.unmark(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        favorite = await response.parse()
        assert favorite is None

    @parametrize
    async def test_streaming_response_unmark(self, async_client: AsyncPatronusAPI) -> None:
        async with async_client.evaluation_results.favorite.with_streaming_response.unmark(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            favorite = await response.parse()
            assert favorite is None

        assert cast(Any, response.is_closed) is True

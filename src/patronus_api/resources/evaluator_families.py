# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.list_evaluator_family_response import ListEvaluatorFamilyResponse

__all__ = ["EvaluatorFamiliesResource", "AsyncEvaluatorFamiliesResource"]


class EvaluatorFamiliesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluatorFamiliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return EvaluatorFamiliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluatorFamiliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return EvaluatorFamiliesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorFamilyResponse:
        """List Evaluator Families"""
        return self._get(
            "/v1/evaluator-families",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEvaluatorFamilyResponse,
        )


class AsyncEvaluatorFamiliesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluatorFamiliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluatorFamiliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluatorFamiliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncEvaluatorFamiliesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorFamilyResponse:
        """List Evaluator Families"""
        return await self._get(
            "/v1/evaluator-families",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEvaluatorFamilyResponse,
        )


class EvaluatorFamiliesResourceWithRawResponse:
    def __init__(self, evaluator_families: EvaluatorFamiliesResource) -> None:
        self._evaluator_families = evaluator_families

        self.list = to_raw_response_wrapper(
            evaluator_families.list,
        )


class AsyncEvaluatorFamiliesResourceWithRawResponse:
    def __init__(self, evaluator_families: AsyncEvaluatorFamiliesResource) -> None:
        self._evaluator_families = evaluator_families

        self.list = async_to_raw_response_wrapper(
            evaluator_families.list,
        )


class EvaluatorFamiliesResourceWithStreamingResponse:
    def __init__(self, evaluator_families: EvaluatorFamiliesResource) -> None:
        self._evaluator_families = evaluator_families

        self.list = to_streamed_response_wrapper(
            evaluator_families.list,
        )


class AsyncEvaluatorFamiliesResourceWithStreamingResponse:
    def __init__(self, evaluator_families: AsyncEvaluatorFamiliesResource) -> None:
        self._evaluator_families = evaluator_families

        self.list = async_to_streamed_response_wrapper(
            evaluator_families.list,
        )

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.evaluator_criteria import revision_create_params
from ...types.evaluator_criteria.add_evaluator_criteria_revision import AddEvaluatorCriteriaRevision

__all__ = ["RevisionResource", "AsyncRevisionResource"]


class RevisionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RevisionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return RevisionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RevisionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return RevisionResourceWithStreamingResponse(self)

    def create(
        self,
        public_id: str,
        *,
        config: object,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddEvaluatorCriteriaRevision:
        """
        Add Evaluator Criteria Revision

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        return self._post(
            f"/v1/evaluator-criteria/{public_id}/revision",
            body=maybe_transform(
                {
                    "config": config,
                    "description": description,
                },
                revision_create_params.RevisionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddEvaluatorCriteriaRevision,
        )


class AsyncRevisionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRevisionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRevisionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRevisionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncRevisionResourceWithStreamingResponse(self)

    async def create(
        self,
        public_id: str,
        *,
        config: object,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AddEvaluatorCriteriaRevision:
        """
        Add Evaluator Criteria Revision

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        return await self._post(
            f"/v1/evaluator-criteria/{public_id}/revision",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "description": description,
                },
                revision_create_params.RevisionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddEvaluatorCriteriaRevision,
        )


class RevisionResourceWithRawResponse:
    def __init__(self, revision: RevisionResource) -> None:
        self._revision = revision

        self.create = to_raw_response_wrapper(
            revision.create,
        )


class AsyncRevisionResourceWithRawResponse:
    def __init__(self, revision: AsyncRevisionResource) -> None:
        self._revision = revision

        self.create = async_to_raw_response_wrapper(
            revision.create,
        )


class RevisionResourceWithStreamingResponse:
    def __init__(self, revision: RevisionResource) -> None:
        self._revision = revision

        self.create = to_streamed_response_wrapper(
            revision.create,
        )


class AsyncRevisionResourceWithStreamingResponse:
    def __init__(self, revision: AsyncRevisionResource) -> None:
        self._revision = revision

        self.create = async_to_streamed_response_wrapper(
            revision.create,
        )

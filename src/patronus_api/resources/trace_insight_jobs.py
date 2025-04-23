# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import trace_insight_job_list_params, trace_insight_job_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.trace_insight_job_list_response import TraceInsightJobListResponse
from ..types.trace_insight_job_create_response import TraceInsightJobCreateResponse

__all__ = ["TraceInsightJobsResource", "AsyncTraceInsightJobsResource"]


class TraceInsightJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TraceInsightJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return TraceInsightJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TraceInsightJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return TraceInsightJobsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        trace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TraceInsightJobCreateResponse:
        """
        Create Insight Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/trace-insight-jobs",
            body=maybe_transform({"trace_id": trace_id}, trace_insight_job_create_params.TraceInsightJobCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TraceInsightJobCreateResponse,
        )

    def list(
        self,
        *,
        trace_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TraceInsightJobListResponse:
        """
        List Insight Jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/trace-insight-jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"trace_id": trace_id}, trace_insight_job_list_params.TraceInsightJobListParams),
            ),
            cast_to=TraceInsightJobListResponse,
        )


class AsyncTraceInsightJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTraceInsightJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTraceInsightJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTraceInsightJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncTraceInsightJobsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        trace_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TraceInsightJobCreateResponse:
        """
        Create Insight Job

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/trace-insight-jobs",
            body=await async_maybe_transform(
                {"trace_id": trace_id}, trace_insight_job_create_params.TraceInsightJobCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TraceInsightJobCreateResponse,
        )

    async def list(
        self,
        *,
        trace_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TraceInsightJobListResponse:
        """
        List Insight Jobs

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/trace-insight-jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"trace_id": trace_id}, trace_insight_job_list_params.TraceInsightJobListParams
                ),
            ),
            cast_to=TraceInsightJobListResponse,
        )


class TraceInsightJobsResourceWithRawResponse:
    def __init__(self, trace_insight_jobs: TraceInsightJobsResource) -> None:
        self._trace_insight_jobs = trace_insight_jobs

        self.create = to_raw_response_wrapper(
            trace_insight_jobs.create,
        )
        self.list = to_raw_response_wrapper(
            trace_insight_jobs.list,
        )


class AsyncTraceInsightJobsResourceWithRawResponse:
    def __init__(self, trace_insight_jobs: AsyncTraceInsightJobsResource) -> None:
        self._trace_insight_jobs = trace_insight_jobs

        self.create = async_to_raw_response_wrapper(
            trace_insight_jobs.create,
        )
        self.list = async_to_raw_response_wrapper(
            trace_insight_jobs.list,
        )


class TraceInsightJobsResourceWithStreamingResponse:
    def __init__(self, trace_insight_jobs: TraceInsightJobsResource) -> None:
        self._trace_insight_jobs = trace_insight_jobs

        self.create = to_streamed_response_wrapper(
            trace_insight_jobs.create,
        )
        self.list = to_streamed_response_wrapper(
            trace_insight_jobs.list,
        )


class AsyncTraceInsightJobsResourceWithStreamingResponse:
    def __init__(self, trace_insight_jobs: AsyncTraceInsightJobsResource) -> None:
        self._trace_insight_jobs = trace_insight_jobs

        self.create = async_to_streamed_response_wrapper(
            trace_insight_jobs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            trace_insight_jobs.list,
        )

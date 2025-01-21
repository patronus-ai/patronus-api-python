# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import annotation_annotate_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.annotate_response import AnnotateResponse

__all__ = ["AnnotationsResource", "AsyncAnnotationsResource"]


class AnnotationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AnnotationsResourceWithStreamingResponse(self)

    def annotate(
        self,
        *,
        annotation_criteria_id: str,
        log_id: str,
        explanation: Optional[str] | NotGiven = NOT_GIVEN,
        value_pass: Optional[bool] | NotGiven = NOT_GIVEN,
        value_score: Optional[float] | NotGiven = NOT_GIVEN,
        value_text: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotateResponse:
        """
        Annotate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/annotate",
            body=maybe_transform(
                {
                    "annotation_criteria_id": annotation_criteria_id,
                    "log_id": log_id,
                    "explanation": explanation,
                    "value_pass": value_pass,
                    "value_score": value_score,
                    "value_text": value_text,
                },
                annotation_annotate_params.AnnotationAnnotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotateResponse,
        )


class AsyncAnnotationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncAnnotationsResourceWithStreamingResponse(self)

    async def annotate(
        self,
        *,
        annotation_criteria_id: str,
        log_id: str,
        explanation: Optional[str] | NotGiven = NOT_GIVEN,
        value_pass: Optional[bool] | NotGiven = NOT_GIVEN,
        value_score: Optional[float] | NotGiven = NOT_GIVEN,
        value_text: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AnnotateResponse:
        """
        Annotate

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/annotate",
            body=await async_maybe_transform(
                {
                    "annotation_criteria_id": annotation_criteria_id,
                    "log_id": log_id,
                    "explanation": explanation,
                    "value_pass": value_pass,
                    "value_score": value_score,
                    "value_text": value_text,
                },
                annotation_annotate_params.AnnotationAnnotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotateResponse,
        )


class AnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.annotate = to_raw_response_wrapper(
            annotations.annotate,
        )


class AsyncAnnotationsResourceWithRawResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.annotate = async_to_raw_response_wrapper(
            annotations.annotate,
        )


class AnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AnnotationsResource) -> None:
        self._annotations = annotations

        self.annotate = to_streamed_response_wrapper(
            annotations.annotate,
        )


class AsyncAnnotationsResourceWithStreamingResponse:
    def __init__(self, annotations: AsyncAnnotationsResource) -> None:
        self._annotations = annotations

        self.annotate = async_to_streamed_response_wrapper(
            annotations.annotate,
        )

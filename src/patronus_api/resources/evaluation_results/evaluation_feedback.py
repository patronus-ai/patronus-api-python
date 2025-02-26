# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.evaluation_results import evaluation_feedback_submit_params

__all__ = ["EvaluationFeedbackResource", "AsyncEvaluationFeedbackResource"]


class EvaluationFeedbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return EvaluationFeedbackResourceWithStreamingResponse(self)

    def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Evaluation Feedback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/evaluation-results/{id}/evaluation-feedback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def submit(
        self,
        id: int,
        *,
        feedback: Literal["positive", "negative"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Give Evaluation Feedback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/evaluation-results/{id}/evaluation-feedback",
            body=maybe_transform(
                {"feedback": feedback}, evaluation_feedback_submit_params.EvaluationFeedbackSubmitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvaluationFeedbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncEvaluationFeedbackResourceWithStreamingResponse(self)

    async def delete(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Evaluation Feedback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/evaluation-results/{id}/evaluation-feedback",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def submit(
        self,
        id: int,
        *,
        feedback: Literal["positive", "negative"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Give Evaluation Feedback

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/evaluation-results/{id}/evaluation-feedback",
            body=await async_maybe_transform(
                {"feedback": feedback}, evaluation_feedback_submit_params.EvaluationFeedbackSubmitParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvaluationFeedbackResourceWithRawResponse:
    def __init__(self, evaluation_feedback: EvaluationFeedbackResource) -> None:
        self._evaluation_feedback = evaluation_feedback

        self.delete = to_raw_response_wrapper(
            evaluation_feedback.delete,
        )
        self.submit = to_raw_response_wrapper(
            evaluation_feedback.submit,
        )


class AsyncEvaluationFeedbackResourceWithRawResponse:
    def __init__(self, evaluation_feedback: AsyncEvaluationFeedbackResource) -> None:
        self._evaluation_feedback = evaluation_feedback

        self.delete = async_to_raw_response_wrapper(
            evaluation_feedback.delete,
        )
        self.submit = async_to_raw_response_wrapper(
            evaluation_feedback.submit,
        )


class EvaluationFeedbackResourceWithStreamingResponse:
    def __init__(self, evaluation_feedback: EvaluationFeedbackResource) -> None:
        self._evaluation_feedback = evaluation_feedback

        self.delete = to_streamed_response_wrapper(
            evaluation_feedback.delete,
        )
        self.submit = to_streamed_response_wrapper(
            evaluation_feedback.submit,
        )


class AsyncEvaluationFeedbackResourceWithStreamingResponse:
    def __init__(self, evaluation_feedback: AsyncEvaluationFeedbackResource) -> None:
        self._evaluation_feedback = evaluation_feedback

        self.delete = async_to_streamed_response_wrapper(
            evaluation_feedback.delete,
        )
        self.submit = async_to_streamed_response_wrapper(
            evaluation_feedback.submit,
        )

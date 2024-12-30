# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import feedback_give_params, feedback_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.list_feedback_response import ListFeedbackResponse
from ..types.create_feedback_response import CreateFeedbackResponse

__all__ = ["FeedbackResource", "AsyncFeedbackResource"]


class FeedbackResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return FeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return FeedbackResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        evaluation_result_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluation_run_candidate_input_id: Optional[int] | NotGiven = NOT_GIVEN,
        evaluation_run_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFeedbackResponse:
        """**This endpoint is deprecated.

        Please use
        [Search Evaluation Results](https://docs.patronus.ai/reference/search_evaluation_results_v1_evaluation_results_search_post)
        endpoint instead.**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/feedback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "evaluation_result_id": evaluation_result_id,
                        "evaluation_run_candidate_input_id": evaluation_run_candidate_input_id,
                        "evaluation_run_id": evaluation_run_id,
                        "evaluator_id": evaluator_id,
                        "limit": limit,
                        "offset": offset,
                        "profile_name": profile_name,
                    },
                    feedback_retrieve_params.FeedbackRetrieveParams,
                ),
            ),
            cast_to=ListFeedbackResponse,
        )

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
        """**This endpoint is deprecated.

        Please use
        [Delete Feedback](https://docs.patronus.ai/reference/delete-feedback) endpoint
        instead.**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/feedback/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def give(
        self,
        *,
        feedback_positive: bool,
        evaluation_result_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluation_run_candidate_input_id: Optional[int] | NotGiven = NOT_GIVEN,
        evaluation_run_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateFeedbackResponse:
        """**This endpoint is deprecated.

        Please use
        [Give Feedback](https://docs.patronus.ai/reference/give-feedback) endpoint
        instead.**

        ## Provide feedback for LLM Monitoring results and Evaluation Run results.

        Feedbacks are used by
        [Active Learning](https://docs.patronus.ai/docs/active-learning)

        ### Give feedback for a Evaluation Run result:

        To give feedback for evaluation run result, following fields has to be provided
        to identify the sample for which feedback is given:

        - evaluation_run_id
        - evaluator_id
        - evaluation_run_candidate_input_id

        example:

        ```bash
        curl --location 'https://api.patronus.ai/v1/feedback'       --header 'x-api-key: <your api key>'       --header 'Content-Type: application/json'       --data '{
              "feedback_positive": true,
              "evaluation_run_id": "1234567891234567890",
              "evaluator_id": "toxicity-v1",
              "evaluation_run_candidate_input_id": 1
        }'
        ```

        ### Give feedback for a LLM Monitoring result:

        To give feedback for LLM Monitoring result only `evaluation_result_id` to
        identify the record.

        example:

        ```bash
        curl --location 'https://api.patronus.ai/v1/feedback'       --header 'x-api-key: <your api key>'       --header 'Content-Type: application/json'         --data '{
            "feedback_positive": true,
            "evaluation_result_id": "1234567891234567890"
          }'
        ```

        Args:
          feedback_positive: Whether the feedback is positive or negative.

          evaluation_result_id: Evaluation Result ID for which feedback is given. Only applicable for LLM
              Monitoring results.

          evaluation_run_candidate_input_id: ID of the sample for which feedback is given. Only applicable for Evaluation Run
              results.

          evaluation_run_id: Evaluation Run ID associated with sample for which feedback is given. Only
              applicable for Evaluation Run results.

          evaluator_id: Evaluator ID associated with sample for which feedback is given. Only applicable
              for Evaluation Run results.

          profile_name: Evaluation run profile name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/feedback",
            body=maybe_transform(
                {
                    "feedback_positive": feedback_positive,
                    "evaluation_result_id": evaluation_result_id,
                    "evaluation_run_candidate_input_id": evaluation_run_candidate_input_id,
                    "evaluation_run_id": evaluation_run_id,
                    "evaluator_id": evaluator_id,
                    "profile_name": profile_name,
                },
                feedback_give_params.FeedbackGiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFeedbackResponse,
        )


class AsyncFeedbackResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbackResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFeedbackResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncFeedbackResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        evaluation_result_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluation_run_candidate_input_id: Optional[int] | NotGiven = NOT_GIVEN,
        evaluation_run_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListFeedbackResponse:
        """**This endpoint is deprecated.

        Please use
        [Search Evaluation Results](https://docs.patronus.ai/reference/search_evaluation_results_v1_evaluation_results_search_post)
        endpoint instead.**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/feedback",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "evaluation_result_id": evaluation_result_id,
                        "evaluation_run_candidate_input_id": evaluation_run_candidate_input_id,
                        "evaluation_run_id": evaluation_run_id,
                        "evaluator_id": evaluator_id,
                        "limit": limit,
                        "offset": offset,
                        "profile_name": profile_name,
                    },
                    feedback_retrieve_params.FeedbackRetrieveParams,
                ),
            ),
            cast_to=ListFeedbackResponse,
        )

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
        """**This endpoint is deprecated.

        Please use
        [Delete Feedback](https://docs.patronus.ai/reference/delete-feedback) endpoint
        instead.**

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/feedback/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def give(
        self,
        *,
        feedback_positive: bool,
        evaluation_result_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluation_run_candidate_input_id: Optional[int] | NotGiven = NOT_GIVEN,
        evaluation_run_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateFeedbackResponse:
        """**This endpoint is deprecated.

        Please use
        [Give Feedback](https://docs.patronus.ai/reference/give-feedback) endpoint
        instead.**

        ## Provide feedback for LLM Monitoring results and Evaluation Run results.

        Feedbacks are used by
        [Active Learning](https://docs.patronus.ai/docs/active-learning)

        ### Give feedback for a Evaluation Run result:

        To give feedback for evaluation run result, following fields has to be provided
        to identify the sample for which feedback is given:

        - evaluation_run_id
        - evaluator_id
        - evaluation_run_candidate_input_id

        example:

        ```bash
        curl --location 'https://api.patronus.ai/v1/feedback'       --header 'x-api-key: <your api key>'       --header 'Content-Type: application/json'       --data '{
              "feedback_positive": true,
              "evaluation_run_id": "1234567891234567890",
              "evaluator_id": "toxicity-v1",
              "evaluation_run_candidate_input_id": 1
        }'
        ```

        ### Give feedback for a LLM Monitoring result:

        To give feedback for LLM Monitoring result only `evaluation_result_id` to
        identify the record.

        example:

        ```bash
        curl --location 'https://api.patronus.ai/v1/feedback'       --header 'x-api-key: <your api key>'       --header 'Content-Type: application/json'         --data '{
            "feedback_positive": true,
            "evaluation_result_id": "1234567891234567890"
          }'
        ```

        Args:
          feedback_positive: Whether the feedback is positive or negative.

          evaluation_result_id: Evaluation Result ID for which feedback is given. Only applicable for LLM
              Monitoring results.

          evaluation_run_candidate_input_id: ID of the sample for which feedback is given. Only applicable for Evaluation Run
              results.

          evaluation_run_id: Evaluation Run ID associated with sample for which feedback is given. Only
              applicable for Evaluation Run results.

          evaluator_id: Evaluator ID associated with sample for which feedback is given. Only applicable
              for Evaluation Run results.

          profile_name: Evaluation run profile name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/feedback",
            body=await async_maybe_transform(
                {
                    "feedback_positive": feedback_positive,
                    "evaluation_result_id": evaluation_result_id,
                    "evaluation_run_candidate_input_id": evaluation_run_candidate_input_id,
                    "evaluation_run_id": evaluation_run_id,
                    "evaluator_id": evaluator_id,
                    "profile_name": profile_name,
                },
                feedback_give_params.FeedbackGiveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateFeedbackResponse,
        )


class FeedbackResourceWithRawResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.retrieve = to_raw_response_wrapper(
            feedback.retrieve,
        )
        self.delete = to_raw_response_wrapper(
            feedback.delete,
        )
        self.give = to_raw_response_wrapper(
            feedback.give,
        )


class AsyncFeedbackResourceWithRawResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.retrieve = async_to_raw_response_wrapper(
            feedback.retrieve,
        )
        self.delete = async_to_raw_response_wrapper(
            feedback.delete,
        )
        self.give = async_to_raw_response_wrapper(
            feedback.give,
        )


class FeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: FeedbackResource) -> None:
        self._feedback = feedback

        self.retrieve = to_streamed_response_wrapper(
            feedback.retrieve,
        )
        self.delete = to_streamed_response_wrapper(
            feedback.delete,
        )
        self.give = to_streamed_response_wrapper(
            feedback.give,
        )


class AsyncFeedbackResourceWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedbackResource) -> None:
        self._feedback = feedback

        self.retrieve = async_to_streamed_response_wrapper(
            feedback.retrieve,
        )
        self.delete = async_to_streamed_response_wrapper(
            feedback.delete,
        )
        self.give = async_to_streamed_response_wrapper(
            feedback.give,
        )

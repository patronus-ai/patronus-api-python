# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .tags import (
    TagsResource,
    AsyncTagsResource,
    TagsResourceWithRawResponse,
    AsyncTagsResourceWithRawResponse,
    TagsResourceWithStreamingResponse,
    AsyncTagsResourceWithStreamingResponse,
)
from ...types import (
    evaluation_result_search_params,
    evaluation_result_batch_create_params,
    evaluation_result_evaluation_feedback_params,
)
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
from ...types.get_evaluation_result import GetEvaluationResult
from ...types.evaluate_result_search_response import EvaluateResultSearchResponse
from ...types.create_evaluation_results_batch_response import CreateEvaluationResultsBatchResponse

__all__ = ["EvaluationResultsResource", "AsyncEvaluationResultsResource"]


class EvaluationResultsResource(SyncAPIResource):
    @cached_property
    def tags(self) -> TagsResource:
        return TagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EvaluationResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return EvaluationResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return EvaluationResultsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetEvaluationResult:
        """
        Get Evaluation Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/v1/evaluation-results/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetEvaluationResult,
        )

    def batch_create(
        self,
        *,
        evaluation_results: Iterable[evaluation_result_batch_create_params.EvaluationResult],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateEvaluationResultsBatchResponse:
        """
        The Batch Create Evaluation Results endpoint lets you import external
        evaluations into the Patronus platform.

        The order of input evaluations is preserved in the output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/evaluation-results/batch",
            body=maybe_transform(
                {"evaluation_results": evaluation_results},
                evaluation_result_batch_create_params.EvaluationResultBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEvaluationResultsBatchResponse,
        )

    def evaluation_feedback(
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
                {"feedback": feedback},
                evaluation_result_evaluation_feedback_params.EvaluationResultEvaluationFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def favorite(
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
        Mark Favorite Evaluation Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/v1/evaluation-results/{id}/favorite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_evaluation_feedback(
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

    def search(
        self,
        *,
        after_datetime: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        after_id: Optional[int] | NotGiven = NOT_GIVEN,
        app: Optional[str] | NotGiven = NOT_GIVEN,
        before_datetime: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        before_id: Optional[int] | NotGiven = NOT_GIVEN,
        criteria: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluation_feedback_status: Optional[Literal["given", "notgiven", "positive", "negative"]]
        | NotGiven = NOT_GIVEN,
        evaluation_run_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_family: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_profile_public_id: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        explain: Optional[bool] | NotGiven = NOT_GIVEN,
        explain_strategy: Optional[Literal["never", "on-fail", "on-success", "always"]] | NotGiven = NOT_GIVEN,
        favorite: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["created_at", "-created_at", "dataset_sample_id", "-dataset_sample_id"] | NotGiven = NOT_GIVEN,
        pass_: Optional[bool] | NotGiven = NOT_GIVEN,
        profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        score_raw_max: Optional[float] | NotGiven = NOT_GIVEN,
        score_raw_min: Optional[float] | NotGiven = NOT_GIVEN,
        tags: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResultSearchResponse:
        """
        Search Evaluation Results

        Args:
          after_datetime: Filter results to those recorded after this date and time.

          after_id: Filter results to those with an ID greater than this value.

          app: Filter by the application name related to the evaluation results.

          before_datetime: Filter results to those recorded before this date and time.

          before_id: Filter results to those with an ID less than this value.

          criteria: Filter by the name of the evaluator criteria associated with the evaluation
              results.

          dataset_id: Filter by the dataset ID related to the evaluation results.

          evaluation_run_id: Filter by the evaluation run ID related to the evaluation results.

          evaluator_family: Filter by the evaluator family associated with the evaluation results.

          evaluator_id: Filter by the ID of the evaluation criterion.

          evaluator_profile_public_id: Filter by public id of evaluator profile used in evaluation.

          experiment_id: Filter by the experiment ID related to the evaluation results.

          explain: Filter results by having explanation.

          explain_strategy: Filter results by explain strategy.

          limit: Maximum number of results to return.

          order: Ordering option for the search results.

          pass_: Filter results by those which pass or failed the evaluation.

          profile_name: Filter by the name of the evaluator profile associated with the evaluation
              results.

          project_id: Filter by the project ID related to the evaluation results.

          tags: Filter by given tags. Tags given in this filter are combined with the and
              clause. Example: {"model_version": "1.0.0", "next_tag": "1234"} Will return only
              those evaluation results which have both tags with given values. This is an
              exact match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/evaluation-results/search",
            body=maybe_transform(
                {
                    "after_datetime": after_datetime,
                    "after_id": after_id,
                    "app": app,
                    "before_datetime": before_datetime,
                    "before_id": before_id,
                    "criteria": criteria,
                    "dataset_id": dataset_id,
                    "evaluation_feedback_status": evaluation_feedback_status,
                    "evaluation_run_id": evaluation_run_id,
                    "evaluator_family": evaluator_family,
                    "evaluator_id": evaluator_id,
                    "evaluator_profile_public_id": evaluator_profile_public_id,
                    "experiment_id": experiment_id,
                    "explain": explain,
                    "explain_strategy": explain_strategy,
                    "favorite": favorite,
                    "limit": limit,
                    "order": order,
                    "pass_": pass_,
                    "profile_name": profile_name,
                    "project_id": project_id,
                    "score_raw_max": score_raw_max,
                    "score_raw_min": score_raw_min,
                    "tags": tags,
                },
                evaluation_result_search_params.EvaluationResultSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResultSearchResponse,
        )

    def unfavorite(
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
        Unmark Favorite Evaluation Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/evaluation-results/{id}/favorite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncEvaluationResultsResource(AsyncAPIResource):
    @cached_property
    def tags(self) -> AsyncTagsResource:
        return AsyncTagsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEvaluationResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluationResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncEvaluationResultsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetEvaluationResult:
        """
        Get Evaluation Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/v1/evaluation-results/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetEvaluationResult,
        )

    async def batch_create(
        self,
        *,
        evaluation_results: Iterable[evaluation_result_batch_create_params.EvaluationResult],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateEvaluationResultsBatchResponse:
        """
        The Batch Create Evaluation Results endpoint lets you import external
        evaluations into the Patronus platform.

        The order of input evaluations is preserved in the output.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/evaluation-results/batch",
            body=await async_maybe_transform(
                {"evaluation_results": evaluation_results},
                evaluation_result_batch_create_params.EvaluationResultBatchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEvaluationResultsBatchResponse,
        )

    async def evaluation_feedback(
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
                {"feedback": feedback},
                evaluation_result_evaluation_feedback_params.EvaluationResultEvaluationFeedbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def favorite(
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
        Mark Favorite Evaluation Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/v1/evaluation-results/{id}/favorite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_evaluation_feedback(
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

    async def search(
        self,
        *,
        after_datetime: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        after_id: Optional[int] | NotGiven = NOT_GIVEN,
        app: Optional[str] | NotGiven = NOT_GIVEN,
        before_datetime: Union[str, datetime, None] | NotGiven = NOT_GIVEN,
        before_id: Optional[int] | NotGiven = NOT_GIVEN,
        criteria: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluation_feedback_status: Optional[Literal["given", "notgiven", "positive", "negative"]]
        | NotGiven = NOT_GIVEN,
        evaluation_run_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_family: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_profile_public_id: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        explain: Optional[bool] | NotGiven = NOT_GIVEN,
        explain_strategy: Optional[Literal["never", "on-fail", "on-success", "always"]] | NotGiven = NOT_GIVEN,
        favorite: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        order: Literal["created_at", "-created_at", "dataset_sample_id", "-dataset_sample_id"] | NotGiven = NOT_GIVEN,
        pass_: Optional[bool] | NotGiven = NOT_GIVEN,
        profile_name: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        score_raw_max: Optional[float] | NotGiven = NOT_GIVEN,
        score_raw_min: Optional[float] | NotGiven = NOT_GIVEN,
        tags: Optional[Dict[str, str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResultSearchResponse:
        """
        Search Evaluation Results

        Args:
          after_datetime: Filter results to those recorded after this date and time.

          after_id: Filter results to those with an ID greater than this value.

          app: Filter by the application name related to the evaluation results.

          before_datetime: Filter results to those recorded before this date and time.

          before_id: Filter results to those with an ID less than this value.

          criteria: Filter by the name of the evaluator criteria associated with the evaluation
              results.

          dataset_id: Filter by the dataset ID related to the evaluation results.

          evaluation_run_id: Filter by the evaluation run ID related to the evaluation results.

          evaluator_family: Filter by the evaluator family associated with the evaluation results.

          evaluator_id: Filter by the ID of the evaluation criterion.

          evaluator_profile_public_id: Filter by public id of evaluator profile used in evaluation.

          experiment_id: Filter by the experiment ID related to the evaluation results.

          explain: Filter results by having explanation.

          explain_strategy: Filter results by explain strategy.

          limit: Maximum number of results to return.

          order: Ordering option for the search results.

          pass_: Filter results by those which pass or failed the evaluation.

          profile_name: Filter by the name of the evaluator profile associated with the evaluation
              results.

          project_id: Filter by the project ID related to the evaluation results.

          tags: Filter by given tags. Tags given in this filter are combined with the and
              clause. Example: {"model_version": "1.0.0", "next_tag": "1234"} Will return only
              those evaluation results which have both tags with given values. This is an
              exact match.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/evaluation-results/search",
            body=await async_maybe_transform(
                {
                    "after_datetime": after_datetime,
                    "after_id": after_id,
                    "app": app,
                    "before_datetime": before_datetime,
                    "before_id": before_id,
                    "criteria": criteria,
                    "dataset_id": dataset_id,
                    "evaluation_feedback_status": evaluation_feedback_status,
                    "evaluation_run_id": evaluation_run_id,
                    "evaluator_family": evaluator_family,
                    "evaluator_id": evaluator_id,
                    "evaluator_profile_public_id": evaluator_profile_public_id,
                    "experiment_id": experiment_id,
                    "explain": explain,
                    "explain_strategy": explain_strategy,
                    "favorite": favorite,
                    "limit": limit,
                    "order": order,
                    "pass_": pass_,
                    "profile_name": profile_name,
                    "project_id": project_id,
                    "score_raw_max": score_raw_max,
                    "score_raw_min": score_raw_min,
                    "tags": tags,
                },
                evaluation_result_search_params.EvaluationResultSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResultSearchResponse,
        )

    async def unfavorite(
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
        Unmark Favorite Evaluation Result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/evaluation-results/{id}/favorite",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class EvaluationResultsResourceWithRawResponse:
    def __init__(self, evaluation_results: EvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = to_raw_response_wrapper(
            evaluation_results.retrieve,
        )
        self.batch_create = to_raw_response_wrapper(
            evaluation_results.batch_create,
        )
        self.evaluation_feedback = to_raw_response_wrapper(
            evaluation_results.evaluation_feedback,
        )
        self.favorite = to_raw_response_wrapper(
            evaluation_results.favorite,
        )
        self.remove_evaluation_feedback = to_raw_response_wrapper(
            evaluation_results.remove_evaluation_feedback,
        )
        self.search = to_raw_response_wrapper(
            evaluation_results.search,
        )
        self.unfavorite = to_raw_response_wrapper(
            evaluation_results.unfavorite,
        )

    @cached_property
    def tags(self) -> TagsResourceWithRawResponse:
        return TagsResourceWithRawResponse(self._evaluation_results.tags)


class AsyncEvaluationResultsResourceWithRawResponse:
    def __init__(self, evaluation_results: AsyncEvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = async_to_raw_response_wrapper(
            evaluation_results.retrieve,
        )
        self.batch_create = async_to_raw_response_wrapper(
            evaluation_results.batch_create,
        )
        self.evaluation_feedback = async_to_raw_response_wrapper(
            evaluation_results.evaluation_feedback,
        )
        self.favorite = async_to_raw_response_wrapper(
            evaluation_results.favorite,
        )
        self.remove_evaluation_feedback = async_to_raw_response_wrapper(
            evaluation_results.remove_evaluation_feedback,
        )
        self.search = async_to_raw_response_wrapper(
            evaluation_results.search,
        )
        self.unfavorite = async_to_raw_response_wrapper(
            evaluation_results.unfavorite,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithRawResponse:
        return AsyncTagsResourceWithRawResponse(self._evaluation_results.tags)


class EvaluationResultsResourceWithStreamingResponse:
    def __init__(self, evaluation_results: EvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = to_streamed_response_wrapper(
            evaluation_results.retrieve,
        )
        self.batch_create = to_streamed_response_wrapper(
            evaluation_results.batch_create,
        )
        self.evaluation_feedback = to_streamed_response_wrapper(
            evaluation_results.evaluation_feedback,
        )
        self.favorite = to_streamed_response_wrapper(
            evaluation_results.favorite,
        )
        self.remove_evaluation_feedback = to_streamed_response_wrapper(
            evaluation_results.remove_evaluation_feedback,
        )
        self.search = to_streamed_response_wrapper(
            evaluation_results.search,
        )
        self.unfavorite = to_streamed_response_wrapper(
            evaluation_results.unfavorite,
        )

    @cached_property
    def tags(self) -> TagsResourceWithStreamingResponse:
        return TagsResourceWithStreamingResponse(self._evaluation_results.tags)


class AsyncEvaluationResultsResourceWithStreamingResponse:
    def __init__(self, evaluation_results: AsyncEvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_results.retrieve,
        )
        self.batch_create = async_to_streamed_response_wrapper(
            evaluation_results.batch_create,
        )
        self.evaluation_feedback = async_to_streamed_response_wrapper(
            evaluation_results.evaluation_feedback,
        )
        self.favorite = async_to_streamed_response_wrapper(
            evaluation_results.favorite,
        )
        self.remove_evaluation_feedback = async_to_streamed_response_wrapper(
            evaluation_results.remove_evaluation_feedback,
        )
        self.search = async_to_streamed_response_wrapper(
            evaluation_results.search,
        )
        self.unfavorite = async_to_streamed_response_wrapper(
            evaluation_results.unfavorite,
        )

    @cached_property
    def tags(self) -> AsyncTagsResourceWithStreamingResponse:
        return AsyncTagsResourceWithStreamingResponse(self._evaluation_results.tags)

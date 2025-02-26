# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import (
    EvaluationExplainStrategies,
    evaluation_result_search_params,
    evaluation_result_create_batch_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .favorite import (
    FavoriteResource,
    AsyncFavoriteResource,
    FavoriteResourceWithRawResponse,
    AsyncFavoriteResourceWithRawResponse,
    FavoriteResourceWithStreamingResponse,
    AsyncFavoriteResourceWithStreamingResponse,
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
from .evaluation_feedback import (
    EvaluationFeedbackResource,
    AsyncEvaluationFeedbackResource,
    EvaluationFeedbackResourceWithRawResponse,
    AsyncEvaluationFeedbackResourceWithRawResponse,
    EvaluationFeedbackResourceWithStreamingResponse,
    AsyncEvaluationFeedbackResourceWithStreamingResponse,
)
from ...types.evaluation_explain_strategies import EvaluationExplainStrategies
from ...types.evaluation_result_search_response import EvaluationResultSearchResponse
from ...types.evaluation_result_retrieve_response import EvaluationResultRetrieveResponse
from ...types.evaluation_result_list_tags_response import EvaluationResultListTagsResponse
from ...types.evaluation_result_create_batch_response import EvaluationResultCreateBatchResponse

__all__ = ["EvaluationResultsResource", "AsyncEvaluationResultsResource"]


class EvaluationResultsResource(SyncAPIResource):
    @cached_property
    def favorite(self) -> FavoriteResource:
        return FavoriteResource(self._client)

    @cached_property
    def evaluation_feedback(self) -> EvaluationFeedbackResource:
        return EvaluationFeedbackResource(self._client)

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
    ) -> EvaluationResultRetrieveResponse:
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
            cast_to=EvaluationResultRetrieveResponse,
        )

    def create_batch(
        self,
        *,
        evaluation_results: Iterable[evaluation_result_create_batch_params.EvaluationResult],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationResultCreateBatchResponse:
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
                evaluation_result_create_batch_params.EvaluationResultCreateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResultCreateBatchResponse,
        )

    def list_tags(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationResultListTagsResponse:
        """List Tags"""
        return self._get(
            "/v1/evaluation-results/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResultListTagsResponse,
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
        evaluation_type: Optional[Literal["patronus_evaluation", "client_evaluation", "annotation"]]
        | NotGiven = NOT_GIVEN,
        evaluator_family: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_profile_public_id: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        explain: Optional[bool] | NotGiven = NOT_GIVEN,
        explain_strategy: Optional[EvaluationExplainStrategies] | NotGiven = NOT_GIVEN,
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
    ) -> EvaluationResultSearchResponse:
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
                    "evaluation_type": evaluation_type,
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
            cast_to=EvaluationResultSearchResponse,
        )


class AsyncEvaluationResultsResource(AsyncAPIResource):
    @cached_property
    def favorite(self) -> AsyncFavoriteResource:
        return AsyncFavoriteResource(self._client)

    @cached_property
    def evaluation_feedback(self) -> AsyncEvaluationFeedbackResource:
        return AsyncEvaluationFeedbackResource(self._client)

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
    ) -> EvaluationResultRetrieveResponse:
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
            cast_to=EvaluationResultRetrieveResponse,
        )

    async def create_batch(
        self,
        *,
        evaluation_results: Iterable[evaluation_result_create_batch_params.EvaluationResult],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationResultCreateBatchResponse:
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
                evaluation_result_create_batch_params.EvaluationResultCreateBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResultCreateBatchResponse,
        )

    async def list_tags(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationResultListTagsResponse:
        """List Tags"""
        return await self._get(
            "/v1/evaluation-results/tags",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationResultListTagsResponse,
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
        evaluation_type: Optional[Literal["patronus_evaluation", "client_evaluation", "annotation"]]
        | NotGiven = NOT_GIVEN,
        evaluator_family: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluator_profile_public_id: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        explain: Optional[bool] | NotGiven = NOT_GIVEN,
        explain_strategy: Optional[EvaluationExplainStrategies] | NotGiven = NOT_GIVEN,
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
    ) -> EvaluationResultSearchResponse:
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
                    "evaluation_type": evaluation_type,
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
            cast_to=EvaluationResultSearchResponse,
        )


class EvaluationResultsResourceWithRawResponse:
    def __init__(self, evaluation_results: EvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = to_raw_response_wrapper(
            evaluation_results.retrieve,
        )
        self.create_batch = to_raw_response_wrapper(
            evaluation_results.create_batch,
        )
        self.list_tags = to_raw_response_wrapper(
            evaluation_results.list_tags,
        )
        self.search = to_raw_response_wrapper(
            evaluation_results.search,
        )

    @cached_property
    def favorite(self) -> FavoriteResourceWithRawResponse:
        return FavoriteResourceWithRawResponse(self._evaluation_results.favorite)

    @cached_property
    def evaluation_feedback(self) -> EvaluationFeedbackResourceWithRawResponse:
        return EvaluationFeedbackResourceWithRawResponse(self._evaluation_results.evaluation_feedback)


class AsyncEvaluationResultsResourceWithRawResponse:
    def __init__(self, evaluation_results: AsyncEvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = async_to_raw_response_wrapper(
            evaluation_results.retrieve,
        )
        self.create_batch = async_to_raw_response_wrapper(
            evaluation_results.create_batch,
        )
        self.list_tags = async_to_raw_response_wrapper(
            evaluation_results.list_tags,
        )
        self.search = async_to_raw_response_wrapper(
            evaluation_results.search,
        )

    @cached_property
    def favorite(self) -> AsyncFavoriteResourceWithRawResponse:
        return AsyncFavoriteResourceWithRawResponse(self._evaluation_results.favorite)

    @cached_property
    def evaluation_feedback(self) -> AsyncEvaluationFeedbackResourceWithRawResponse:
        return AsyncEvaluationFeedbackResourceWithRawResponse(self._evaluation_results.evaluation_feedback)


class EvaluationResultsResourceWithStreamingResponse:
    def __init__(self, evaluation_results: EvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = to_streamed_response_wrapper(
            evaluation_results.retrieve,
        )
        self.create_batch = to_streamed_response_wrapper(
            evaluation_results.create_batch,
        )
        self.list_tags = to_streamed_response_wrapper(
            evaluation_results.list_tags,
        )
        self.search = to_streamed_response_wrapper(
            evaluation_results.search,
        )

    @cached_property
    def favorite(self) -> FavoriteResourceWithStreamingResponse:
        return FavoriteResourceWithStreamingResponse(self._evaluation_results.favorite)

    @cached_property
    def evaluation_feedback(self) -> EvaluationFeedbackResourceWithStreamingResponse:
        return EvaluationFeedbackResourceWithStreamingResponse(self._evaluation_results.evaluation_feedback)


class AsyncEvaluationResultsResourceWithStreamingResponse:
    def __init__(self, evaluation_results: AsyncEvaluationResultsResource) -> None:
        self._evaluation_results = evaluation_results

        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_results.retrieve,
        )
        self.create_batch = async_to_streamed_response_wrapper(
            evaluation_results.create_batch,
        )
        self.list_tags = async_to_streamed_response_wrapper(
            evaluation_results.list_tags,
        )
        self.search = async_to_streamed_response_wrapper(
            evaluation_results.search,
        )

    @cached_property
    def favorite(self) -> AsyncFavoriteResourceWithStreamingResponse:
        return AsyncFavoriteResourceWithStreamingResponse(self._evaluation_results.favorite)

    @cached_property
    def evaluation_feedback(self) -> AsyncEvaluationFeedbackResourceWithStreamingResponse:
        return AsyncEvaluationFeedbackResourceWithStreamingResponse(self._evaluation_results.evaluation_feedback)

# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable, Optional

import httpx

from ..types import (
    pairwise_annotation_list_params,
    pairwise_annotation_create_params,
    pairwise_annotation_delete_params,
    pairwise_annotation_get_batch_params,
)
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
from ..types.pairwise_annotation_list_response import PairwiseAnnotationListResponse
from ..types.pairwise_annotation_create_response import PairwiseAnnotationCreateResponse
from ..types.pairwise_annotation_get_batch_response import PairwiseAnnotationGetBatchResponse

__all__ = ["PairwiseAnnotationsResource", "AsyncPairwiseAnnotationsResource"]


class PairwiseAnnotationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PairwiseAnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return PairwiseAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PairwiseAnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return PairwiseAnnotationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        log_a_id: str,
        log_a_score: float,
        log_b_id: str,
        log_b_score: float,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PairwiseAnnotationCreateResponse:
        """
        Create Pairwise Annotation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/pairwise-annotations",
            body=maybe_transform(
                {
                    "log_a_id": log_a_id,
                    "log_a_score": log_a_score,
                    "log_b_id": log_b_id,
                    "log_b_score": log_b_score,
                    "name": name,
                },
                pairwise_annotation_create_params.PairwiseAnnotationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairwiseAnnotationCreateResponse,
        )

    def list(
        self,
        *,
        experiment_id: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        log_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        project_id: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PairwiseAnnotationListResponse:
        """
        List Pairwise Annotations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/pairwise-annotations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "experiment_id": experiment_id,
                        "limit": limit,
                        "log_id": log_id,
                        "name": name,
                        "offset": offset,
                        "project_id": project_id,
                    },
                    pairwise_annotation_list_params.PairwiseAnnotationListParams,
                ),
            ),
            cast_to=PairwiseAnnotationListResponse,
        )

    def delete(
        self,
        *,
        log_a_id: str,
        log_b_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Pairwise Annotation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            "/v1/pairwise-annotations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "log_a_id": log_a_id,
                        "log_b_id": log_b_id,
                        "name": name,
                    },
                    pairwise_annotation_delete_params.PairwiseAnnotationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get_batch(
        self,
        *,
        pairwise_annotations: Iterable[pairwise_annotation_get_batch_params.PairwiseAnnotation],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PairwiseAnnotationGetBatchResponse:
        """
        Get Batch Pairwise Annotations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/pairwise-annotations/get-batch",
            body=maybe_transform(
                {"pairwise_annotations": pairwise_annotations},
                pairwise_annotation_get_batch_params.PairwiseAnnotationGetBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairwiseAnnotationGetBatchResponse,
        )


class AsyncPairwiseAnnotationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPairwiseAnnotationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPairwiseAnnotationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPairwiseAnnotationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncPairwiseAnnotationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        log_a_id: str,
        log_a_score: float,
        log_b_id: str,
        log_b_score: float,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PairwiseAnnotationCreateResponse:
        """
        Create Pairwise Annotation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/pairwise-annotations",
            body=await async_maybe_transform(
                {
                    "log_a_id": log_a_id,
                    "log_a_score": log_a_score,
                    "log_b_id": log_b_id,
                    "log_b_score": log_b_score,
                    "name": name,
                },
                pairwise_annotation_create_params.PairwiseAnnotationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairwiseAnnotationCreateResponse,
        )

    async def list(
        self,
        *,
        experiment_id: Optional[Iterable[int]] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        log_id: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        project_id: Optional[List[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PairwiseAnnotationListResponse:
        """
        List Pairwise Annotations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/pairwise-annotations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "experiment_id": experiment_id,
                        "limit": limit,
                        "log_id": log_id,
                        "name": name,
                        "offset": offset,
                        "project_id": project_id,
                    },
                    pairwise_annotation_list_params.PairwiseAnnotationListParams,
                ),
            ),
            cast_to=PairwiseAnnotationListResponse,
        )

    async def delete(
        self,
        *,
        log_a_id: str,
        log_b_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Pairwise Annotation

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            "/v1/pairwise-annotations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "log_a_id": log_a_id,
                        "log_b_id": log_b_id,
                        "name": name,
                    },
                    pairwise_annotation_delete_params.PairwiseAnnotationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get_batch(
        self,
        *,
        pairwise_annotations: Iterable[pairwise_annotation_get_batch_params.PairwiseAnnotation],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PairwiseAnnotationGetBatchResponse:
        """
        Get Batch Pairwise Annotations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/pairwise-annotations/get-batch",
            body=await async_maybe_transform(
                {"pairwise_annotations": pairwise_annotations},
                pairwise_annotation_get_batch_params.PairwiseAnnotationGetBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PairwiseAnnotationGetBatchResponse,
        )


class PairwiseAnnotationsResourceWithRawResponse:
    def __init__(self, pairwise_annotations: PairwiseAnnotationsResource) -> None:
        self._pairwise_annotations = pairwise_annotations

        self.create = to_raw_response_wrapper(
            pairwise_annotations.create,
        )
        self.list = to_raw_response_wrapper(
            pairwise_annotations.list,
        )
        self.delete = to_raw_response_wrapper(
            pairwise_annotations.delete,
        )
        self.get_batch = to_raw_response_wrapper(
            pairwise_annotations.get_batch,
        )


class AsyncPairwiseAnnotationsResourceWithRawResponse:
    def __init__(self, pairwise_annotations: AsyncPairwiseAnnotationsResource) -> None:
        self._pairwise_annotations = pairwise_annotations

        self.create = async_to_raw_response_wrapper(
            pairwise_annotations.create,
        )
        self.list = async_to_raw_response_wrapper(
            pairwise_annotations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pairwise_annotations.delete,
        )
        self.get_batch = async_to_raw_response_wrapper(
            pairwise_annotations.get_batch,
        )


class PairwiseAnnotationsResourceWithStreamingResponse:
    def __init__(self, pairwise_annotations: PairwiseAnnotationsResource) -> None:
        self._pairwise_annotations = pairwise_annotations

        self.create = to_streamed_response_wrapper(
            pairwise_annotations.create,
        )
        self.list = to_streamed_response_wrapper(
            pairwise_annotations.list,
        )
        self.delete = to_streamed_response_wrapper(
            pairwise_annotations.delete,
        )
        self.get_batch = to_streamed_response_wrapper(
            pairwise_annotations.get_batch,
        )


class AsyncPairwiseAnnotationsResourceWithStreamingResponse:
    def __init__(self, pairwise_annotations: AsyncPairwiseAnnotationsResource) -> None:
        self._pairwise_annotations = pairwise_annotations

        self.create = async_to_streamed_response_wrapper(
            pairwise_annotations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            pairwise_annotations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pairwise_annotations.delete,
        )
        self.get_batch = async_to_streamed_response_wrapper(
            pairwise_annotations.get_batch,
        )

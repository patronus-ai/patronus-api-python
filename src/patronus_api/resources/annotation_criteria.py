# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ..types import (
    annotation_criterion_list_params,
    annotation_criterion_create_params,
    annotation_criterion_update_params,
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
from ..types.get_annotation_criteria_response import GetAnnotationCriteriaResponse
from ..types.list_annotation_criteria_response import ListAnnotationCriteriaResponse
from ..types.create_annotation_criteria_response import CreateAnnotationCriteriaResponse
from ..types.update_annotation_criteria_response import UpdateAnnotationCriteriaResponse

__all__ = ["AnnotationCriteriaResource", "AsyncAnnotationCriteriaResource"]


class AnnotationCriteriaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnnotationCriteriaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AnnotationCriteriaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnnotationCriteriaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AnnotationCriteriaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        annotation_type: object,
        name: str,
        project_id: str,
        categories: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateAnnotationCriteriaResponse:
        """
        Create Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/annotation-criteria",
            body=maybe_transform(
                {
                    "annotation_type": annotation_type,
                    "name": name,
                    "project_id": project_id,
                    "categories": categories,
                    "description": description,
                },
                annotation_criterion_create_params.AnnotationCriterionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAnnotationCriteriaResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetAnnotationCriteriaResponse:
        """
        Get Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/annotation-criteria/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetAnnotationCriteriaResponse,
        )

    def update(
        self,
        id: str,
        *,
        annotation_type: object,
        name: str,
        categories: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateAnnotationCriteriaResponse:
        """
        Update Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/annotation-criteria/{id}",
            body=maybe_transform(
                {
                    "annotation_type": annotation_type,
                    "name": name,
                    "categories": categories,
                    "description": description,
                },
                annotation_criterion_update_params.AnnotationCriterionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateAnnotationCriteriaResponse,
        )

    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAnnotationCriteriaResponse:
        """
        List Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/annotation-criteria",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "project_id": project_id,
                    },
                    annotation_criterion_list_params.AnnotationCriterionListParams,
                ),
            ),
            cast_to=ListAnnotationCriteriaResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/annotation-criteria/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAnnotationCriteriaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnnotationCriteriaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnnotationCriteriaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnnotationCriteriaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncAnnotationCriteriaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        annotation_type: object,
        name: str,
        project_id: str,
        categories: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateAnnotationCriteriaResponse:
        """
        Create Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/annotation-criteria",
            body=await async_maybe_transform(
                {
                    "annotation_type": annotation_type,
                    "name": name,
                    "project_id": project_id,
                    "categories": categories,
                    "description": description,
                },
                annotation_criterion_create_params.AnnotationCriterionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateAnnotationCriteriaResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GetAnnotationCriteriaResponse:
        """
        Get Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/annotation-criteria/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetAnnotationCriteriaResponse,
        )

    async def update(
        self,
        id: str,
        *,
        annotation_type: object,
        name: str,
        categories: Optional[Iterable[object]] | NotGiven = NOT_GIVEN,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateAnnotationCriteriaResponse:
        """
        Update Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/annotation-criteria/{id}",
            body=await async_maybe_transform(
                {
                    "annotation_type": annotation_type,
                    "name": name,
                    "categories": categories,
                    "description": description,
                },
                annotation_criterion_update_params.AnnotationCriterionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateAnnotationCriteriaResponse,
        )

    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAnnotationCriteriaResponse:
        """
        List Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/annotation-criteria",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "project_id": project_id,
                    },
                    annotation_criterion_list_params.AnnotationCriterionListParams,
                ),
            ),
            cast_to=ListAnnotationCriteriaResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Delete Annotation Criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/annotation-criteria/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AnnotationCriteriaResourceWithRawResponse:
    def __init__(self, annotation_criteria: AnnotationCriteriaResource) -> None:
        self._annotation_criteria = annotation_criteria

        self.create = to_raw_response_wrapper(
            annotation_criteria.create,
        )
        self.retrieve = to_raw_response_wrapper(
            annotation_criteria.retrieve,
        )
        self.update = to_raw_response_wrapper(
            annotation_criteria.update,
        )
        self.list = to_raw_response_wrapper(
            annotation_criteria.list,
        )
        self.delete = to_raw_response_wrapper(
            annotation_criteria.delete,
        )


class AsyncAnnotationCriteriaResourceWithRawResponse:
    def __init__(self, annotation_criteria: AsyncAnnotationCriteriaResource) -> None:
        self._annotation_criteria = annotation_criteria

        self.create = async_to_raw_response_wrapper(
            annotation_criteria.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            annotation_criteria.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            annotation_criteria.update,
        )
        self.list = async_to_raw_response_wrapper(
            annotation_criteria.list,
        )
        self.delete = async_to_raw_response_wrapper(
            annotation_criteria.delete,
        )


class AnnotationCriteriaResourceWithStreamingResponse:
    def __init__(self, annotation_criteria: AnnotationCriteriaResource) -> None:
        self._annotation_criteria = annotation_criteria

        self.create = to_streamed_response_wrapper(
            annotation_criteria.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            annotation_criteria.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            annotation_criteria.update,
        )
        self.list = to_streamed_response_wrapper(
            annotation_criteria.list,
        )
        self.delete = to_streamed_response_wrapper(
            annotation_criteria.delete,
        )


class AsyncAnnotationCriteriaResourceWithStreamingResponse:
    def __init__(self, annotation_criteria: AsyncAnnotationCriteriaResource) -> None:
        self._annotation_criteria = annotation_criteria

        self.create = async_to_streamed_response_wrapper(
            annotation_criteria.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            annotation_criteria.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            annotation_criteria.update,
        )
        self.list = async_to_streamed_response_wrapper(
            annotation_criteria.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            annotation_criteria.delete,
        )

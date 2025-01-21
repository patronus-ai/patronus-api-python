# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import (
    evaluator_profile_list_params,
    evaluator_profile_create_params,
    evaluator_profile_revision_params,
)
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
from ..types.add_evaluator_profile_revision import AddEvaluatorProfileRevision
from ..types.list_evaluator_profiles_response import ListEvaluatorProfilesResponse
from ..types.create_evaluator_profile_response import CreateEvaluatorProfileResponse
from ..types.archive_evaluator_profile_response import ArchiveEvaluatorProfileResponse

__all__ = ["EvaluatorProfilesResource", "AsyncEvaluatorProfilesResource"]


class EvaluatorProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluatorProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return EvaluatorProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluatorProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return EvaluatorProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: object,
        evaluator_family: str,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateEvaluatorProfileResponse:
        """
        Create Evaluator Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/evaluator-profiles",
            body=maybe_transform(
                {
                    "config": config,
                    "evaluator_family": evaluator_family,
                    "name": name,
                    "description": description,
                },
                evaluator_profile_create_params.EvaluatorProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEvaluatorProfileResponse,
        )

    def list(
        self,
        *,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        evaluator_family: Optional[str] | NotGiven = NOT_GIVEN,
        get_last_revision: bool | NotGiven = NOT_GIVEN,
        is_patronus_managed: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        public_id: Optional[str] | NotGiven = NOT_GIVEN,
        revision: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorProfilesResponse:
        """
        List Evaluator Profiles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/evaluator-profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "enabled": enabled,
                        "evaluator_family": evaluator_family,
                        "get_last_revision": get_last_revision,
                        "is_patronus_managed": is_patronus_managed,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "public_id": public_id,
                        "revision": revision,
                    },
                    evaluator_profile_list_params.EvaluatorProfileListParams,
                ),
            ),
            cast_to=ListEvaluatorProfilesResponse,
        )

    def archive(
        self,
        public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArchiveEvaluatorProfileResponse:
        """
        Archive Evaluator Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        return self._patch(
            f"/v1/evaluator-profiles/{public_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArchiveEvaluatorProfileResponse,
        )

    def revision(
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
    ) -> AddEvaluatorProfileRevision:
        """
        Add Evaluator Profile Revision

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        return self._post(
            f"/v1/evaluator-profiles/{public_id}/revision",
            body=maybe_transform(
                {
                    "config": config,
                    "description": description,
                },
                evaluator_profile_revision_params.EvaluatorProfileRevisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddEvaluatorProfileRevision,
        )


class AsyncEvaluatorProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluatorProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEvaluatorProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluatorProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncEvaluatorProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: object,
        evaluator_family: str,
        name: str,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateEvaluatorProfileResponse:
        """
        Create Evaluator Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/evaluator-profiles",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "evaluator_family": evaluator_family,
                    "name": name,
                    "description": description,
                },
                evaluator_profile_create_params.EvaluatorProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateEvaluatorProfileResponse,
        )

    async def list(
        self,
        *,
        enabled: Optional[bool] | NotGiven = NOT_GIVEN,
        evaluator_family: Optional[str] | NotGiven = NOT_GIVEN,
        get_last_revision: bool | NotGiven = NOT_GIVEN,
        is_patronus_managed: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        public_id: Optional[str] | NotGiven = NOT_GIVEN,
        revision: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorProfilesResponse:
        """
        List Evaluator Profiles

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/evaluator-profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "enabled": enabled,
                        "evaluator_family": evaluator_family,
                        "get_last_revision": get_last_revision,
                        "is_patronus_managed": is_patronus_managed,
                        "limit": limit,
                        "name": name,
                        "offset": offset,
                        "public_id": public_id,
                        "revision": revision,
                    },
                    evaluator_profile_list_params.EvaluatorProfileListParams,
                ),
            ),
            cast_to=ListEvaluatorProfilesResponse,
        )

    async def archive(
        self,
        public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArchiveEvaluatorProfileResponse:
        """
        Archive Evaluator Profile

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        return await self._patch(
            f"/v1/evaluator-profiles/{public_id}/archive",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArchiveEvaluatorProfileResponse,
        )

    async def revision(
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
    ) -> AddEvaluatorProfileRevision:
        """
        Add Evaluator Profile Revision

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        return await self._post(
            f"/v1/evaluator-profiles/{public_id}/revision",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "description": description,
                },
                evaluator_profile_revision_params.EvaluatorProfileRevisionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AddEvaluatorProfileRevision,
        )


class EvaluatorProfilesResourceWithRawResponse:
    def __init__(self, evaluator_profiles: EvaluatorProfilesResource) -> None:
        self._evaluator_profiles = evaluator_profiles

        self.create = to_raw_response_wrapper(
            evaluator_profiles.create,
        )
        self.list = to_raw_response_wrapper(
            evaluator_profiles.list,
        )
        self.archive = to_raw_response_wrapper(
            evaluator_profiles.archive,
        )
        self.revision = to_raw_response_wrapper(
            evaluator_profiles.revision,
        )


class AsyncEvaluatorProfilesResourceWithRawResponse:
    def __init__(self, evaluator_profiles: AsyncEvaluatorProfilesResource) -> None:
        self._evaluator_profiles = evaluator_profiles

        self.create = async_to_raw_response_wrapper(
            evaluator_profiles.create,
        )
        self.list = async_to_raw_response_wrapper(
            evaluator_profiles.list,
        )
        self.archive = async_to_raw_response_wrapper(
            evaluator_profiles.archive,
        )
        self.revision = async_to_raw_response_wrapper(
            evaluator_profiles.revision,
        )


class EvaluatorProfilesResourceWithStreamingResponse:
    def __init__(self, evaluator_profiles: EvaluatorProfilesResource) -> None:
        self._evaluator_profiles = evaluator_profiles

        self.create = to_streamed_response_wrapper(
            evaluator_profiles.create,
        )
        self.list = to_streamed_response_wrapper(
            evaluator_profiles.list,
        )
        self.archive = to_streamed_response_wrapper(
            evaluator_profiles.archive,
        )
        self.revision = to_streamed_response_wrapper(
            evaluator_profiles.revision,
        )


class AsyncEvaluatorProfilesResourceWithStreamingResponse:
    def __init__(self, evaluator_profiles: AsyncEvaluatorProfilesResource) -> None:
        self._evaluator_profiles = evaluator_profiles

        self.create = async_to_streamed_response_wrapper(
            evaluator_profiles.create,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluator_profiles.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            evaluator_profiles.archive,
        )
        self.revision = async_to_streamed_response_wrapper(
            evaluator_profiles.revision,
        )

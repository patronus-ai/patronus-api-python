# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    apps,
    misc,
    feedback,
    projects,
    evaluators,
    annotations,
    evaluations,
    experiments,
    evaluator_families,
    evaluator_profiles,
    annotation_criteria,
    pairwise_annotations,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, PatronusAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.datasets import datasets
from .resources.evaluation_results import evaluation_results
from .resources.evaluator_criteria import evaluator_criteria

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "PatronusAPI",
    "AsyncPatronusAPI",
    "Client",
    "AsyncClient",
]


class PatronusAPI(SyncAPIClient):
    datasets: datasets.DatasetsResource
    evaluations: evaluations.EvaluationsResource
    evaluation_results: evaluation_results.EvaluationResultsResource
    evaluator_profiles: evaluator_profiles.EvaluatorProfilesResource
    evaluator_criteria: evaluator_criteria.EvaluatorCriteriaResource
    experiments: experiments.ExperimentsResource
    feedback: feedback.FeedbackResource
    projects: projects.ProjectsResource
    evaluators: evaluators.EvaluatorsResource
    misc: misc.MiscResource
    apps: apps.AppsResource
    evaluator_families: evaluator_families.EvaluatorFamiliesResource
    annotations: annotations.AnnotationsResource
    annotation_criteria: annotation_criteria.AnnotationCriteriaResource
    pairwise_annotations: pairwise_annotations.PairwiseAnnotationsResource
    with_raw_response: PatronusAPIWithRawResponse
    with_streaming_response: PatronusAPIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous patronus-api client instance.

        This automatically infers the `api_key` argument from the `PATRONUS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PATRONUS_API_KEY")
        if api_key is None:
            raise PatronusAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PATRONUS_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PATRONUS_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.patronus.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.datasets = datasets.DatasetsResource(self)
        self.evaluations = evaluations.EvaluationsResource(self)
        self.evaluation_results = evaluation_results.EvaluationResultsResource(self)
        self.evaluator_profiles = evaluator_profiles.EvaluatorProfilesResource(self)
        self.evaluator_criteria = evaluator_criteria.EvaluatorCriteriaResource(self)
        self.experiments = experiments.ExperimentsResource(self)
        self.feedback = feedback.FeedbackResource(self)
        self.projects = projects.ProjectsResource(self)
        self.evaluators = evaluators.EvaluatorsResource(self)
        self.misc = misc.MiscResource(self)
        self.apps = apps.AppsResource(self)
        self.evaluator_families = evaluator_families.EvaluatorFamiliesResource(self)
        self.annotations = annotations.AnnotationsResource(self)
        self.annotation_criteria = annotation_criteria.AnnotationCriteriaResource(self)
        self.pairwise_annotations = pairwise_annotations.PairwiseAnnotationsResource(self)
        self.with_raw_response = PatronusAPIWithRawResponse(self)
        self.with_streaming_response = PatronusAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-KEY": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPatronusAPI(AsyncAPIClient):
    datasets: datasets.AsyncDatasetsResource
    evaluations: evaluations.AsyncEvaluationsResource
    evaluation_results: evaluation_results.AsyncEvaluationResultsResource
    evaluator_profiles: evaluator_profiles.AsyncEvaluatorProfilesResource
    evaluator_criteria: evaluator_criteria.AsyncEvaluatorCriteriaResource
    experiments: experiments.AsyncExperimentsResource
    feedback: feedback.AsyncFeedbackResource
    projects: projects.AsyncProjectsResource
    evaluators: evaluators.AsyncEvaluatorsResource
    misc: misc.AsyncMiscResource
    apps: apps.AsyncAppsResource
    evaluator_families: evaluator_families.AsyncEvaluatorFamiliesResource
    annotations: annotations.AsyncAnnotationsResource
    annotation_criteria: annotation_criteria.AsyncAnnotationCriteriaResource
    pairwise_annotations: pairwise_annotations.AsyncPairwiseAnnotationsResource
    with_raw_response: AsyncPatronusAPIWithRawResponse
    with_streaming_response: AsyncPatronusAPIWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async patronus-api client instance.

        This automatically infers the `api_key` argument from the `PATRONUS_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PATRONUS_API_KEY")
        if api_key is None:
            raise PatronusAPIError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PATRONUS_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PATRONUS_API_BASE_URL")
        if base_url is None:
            base_url = f"https://api.patronus.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.datasets = datasets.AsyncDatasetsResource(self)
        self.evaluations = evaluations.AsyncEvaluationsResource(self)
        self.evaluation_results = evaluation_results.AsyncEvaluationResultsResource(self)
        self.evaluator_profiles = evaluator_profiles.AsyncEvaluatorProfilesResource(self)
        self.evaluator_criteria = evaluator_criteria.AsyncEvaluatorCriteriaResource(self)
        self.experiments = experiments.AsyncExperimentsResource(self)
        self.feedback = feedback.AsyncFeedbackResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.evaluators = evaluators.AsyncEvaluatorsResource(self)
        self.misc = misc.AsyncMiscResource(self)
        self.apps = apps.AsyncAppsResource(self)
        self.evaluator_families = evaluator_families.AsyncEvaluatorFamiliesResource(self)
        self.annotations = annotations.AsyncAnnotationsResource(self)
        self.annotation_criteria = annotation_criteria.AsyncAnnotationCriteriaResource(self)
        self.pairwise_annotations = pairwise_annotations.AsyncPairwiseAnnotationsResource(self)
        self.with_raw_response = AsyncPatronusAPIWithRawResponse(self)
        self.with_streaming_response = AsyncPatronusAPIWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-KEY": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PatronusAPIWithRawResponse:
    def __init__(self, client: PatronusAPI) -> None:
        self.datasets = datasets.DatasetsResourceWithRawResponse(client.datasets)
        self.evaluations = evaluations.EvaluationsResourceWithRawResponse(client.evaluations)
        self.evaluation_results = evaluation_results.EvaluationResultsResourceWithRawResponse(client.evaluation_results)
        self.evaluator_profiles = evaluator_profiles.EvaluatorProfilesResourceWithRawResponse(client.evaluator_profiles)
        self.evaluator_criteria = evaluator_criteria.EvaluatorCriteriaResourceWithRawResponse(client.evaluator_criteria)
        self.experiments = experiments.ExperimentsResourceWithRawResponse(client.experiments)
        self.feedback = feedback.FeedbackResourceWithRawResponse(client.feedback)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.evaluators = evaluators.EvaluatorsResourceWithRawResponse(client.evaluators)
        self.misc = misc.MiscResourceWithRawResponse(client.misc)
        self.apps = apps.AppsResourceWithRawResponse(client.apps)
        self.evaluator_families = evaluator_families.EvaluatorFamiliesResourceWithRawResponse(client.evaluator_families)
        self.annotations = annotations.AnnotationsResourceWithRawResponse(client.annotations)
        self.annotation_criteria = annotation_criteria.AnnotationCriteriaResourceWithRawResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.PairwiseAnnotationsResourceWithRawResponse(
            client.pairwise_annotations
        )


class AsyncPatronusAPIWithRawResponse:
    def __init__(self, client: AsyncPatronusAPI) -> None:
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithRawResponse(client.evaluations)
        self.evaluation_results = evaluation_results.AsyncEvaluationResultsResourceWithRawResponse(
            client.evaluation_results
        )
        self.evaluator_profiles = evaluator_profiles.AsyncEvaluatorProfilesResourceWithRawResponse(
            client.evaluator_profiles
        )
        self.evaluator_criteria = evaluator_criteria.AsyncEvaluatorCriteriaResourceWithRawResponse(
            client.evaluator_criteria
        )
        self.experiments = experiments.AsyncExperimentsResourceWithRawResponse(client.experiments)
        self.feedback = feedback.AsyncFeedbackResourceWithRawResponse(client.feedback)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.evaluators = evaluators.AsyncEvaluatorsResourceWithRawResponse(client.evaluators)
        self.misc = misc.AsyncMiscResourceWithRawResponse(client.misc)
        self.apps = apps.AsyncAppsResourceWithRawResponse(client.apps)
        self.evaluator_families = evaluator_families.AsyncEvaluatorFamiliesResourceWithRawResponse(
            client.evaluator_families
        )
        self.annotations = annotations.AsyncAnnotationsResourceWithRawResponse(client.annotations)
        self.annotation_criteria = annotation_criteria.AsyncAnnotationCriteriaResourceWithRawResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.AsyncPairwiseAnnotationsResourceWithRawResponse(
            client.pairwise_annotations
        )


class PatronusAPIWithStreamedResponse:
    def __init__(self, client: PatronusAPI) -> None:
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.evaluations = evaluations.EvaluationsResourceWithStreamingResponse(client.evaluations)
        self.evaluation_results = evaluation_results.EvaluationResultsResourceWithStreamingResponse(
            client.evaluation_results
        )
        self.evaluator_profiles = evaluator_profiles.EvaluatorProfilesResourceWithStreamingResponse(
            client.evaluator_profiles
        )
        self.evaluator_criteria = evaluator_criteria.EvaluatorCriteriaResourceWithStreamingResponse(
            client.evaluator_criteria
        )
        self.experiments = experiments.ExperimentsResourceWithStreamingResponse(client.experiments)
        self.feedback = feedback.FeedbackResourceWithStreamingResponse(client.feedback)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.evaluators = evaluators.EvaluatorsResourceWithStreamingResponse(client.evaluators)
        self.misc = misc.MiscResourceWithStreamingResponse(client.misc)
        self.apps = apps.AppsResourceWithStreamingResponse(client.apps)
        self.evaluator_families = evaluator_families.EvaluatorFamiliesResourceWithStreamingResponse(
            client.evaluator_families
        )
        self.annotations = annotations.AnnotationsResourceWithStreamingResponse(client.annotations)
        self.annotation_criteria = annotation_criteria.AnnotationCriteriaResourceWithStreamingResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.PairwiseAnnotationsResourceWithStreamingResponse(
            client.pairwise_annotations
        )


class AsyncPatronusAPIWithStreamedResponse:
    def __init__(self, client: AsyncPatronusAPI) -> None:
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.evaluations = evaluations.AsyncEvaluationsResourceWithStreamingResponse(client.evaluations)
        self.evaluation_results = evaluation_results.AsyncEvaluationResultsResourceWithStreamingResponse(
            client.evaluation_results
        )
        self.evaluator_profiles = evaluator_profiles.AsyncEvaluatorProfilesResourceWithStreamingResponse(
            client.evaluator_profiles
        )
        self.evaluator_criteria = evaluator_criteria.AsyncEvaluatorCriteriaResourceWithStreamingResponse(
            client.evaluator_criteria
        )
        self.experiments = experiments.AsyncExperimentsResourceWithStreamingResponse(client.experiments)
        self.feedback = feedback.AsyncFeedbackResourceWithStreamingResponse(client.feedback)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.evaluators = evaluators.AsyncEvaluatorsResourceWithStreamingResponse(client.evaluators)
        self.misc = misc.AsyncMiscResourceWithStreamingResponse(client.misc)
        self.apps = apps.AsyncAppsResourceWithStreamingResponse(client.apps)
        self.evaluator_families = evaluator_families.AsyncEvaluatorFamiliesResourceWithStreamingResponse(
            client.evaluator_families
        )
        self.annotations = annotations.AsyncAnnotationsResourceWithStreamingResponse(client.annotations)
        self.annotation_criteria = annotation_criteria.AsyncAnnotationCriteriaResourceWithStreamingResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.AsyncPairwiseAnnotationsResourceWithStreamingResponse(
            client.pairwise_annotations
        )


Client = PatronusAPI

AsyncClient = AsyncPatronusAPI

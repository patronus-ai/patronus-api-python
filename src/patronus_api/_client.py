# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, List, Union, Mapping, Iterable, Optional
from typing_extensions import Self, Literal, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .types import client_annotate_params, client_evaluate_params, client_list_apps_params
from ._types import (
    NOT_GIVEN,
    Body,
    Omit,
    Query,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    maybe_transform,
    get_async_library,
    async_maybe_transform,
)
from ._version import __version__
from ._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .resources import (
    datasets,
    projects,
    evaluations,
    experiments,
    evaluator_criteria,
    annotation_criteria,
    pairwise_annotations,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, PatronusAPIError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
    make_request_options,
)
from .types.whoami_response import WhoamiResponse
from .types.annotate_response import AnnotateResponse
from .types.evaluate_response import EvaluateResponse
from .types.list_apps_response import ListAppsResponse
from .resources.evaluation_results import evaluation_results
from .types.list_evaluators_response import ListEvaluatorsResponse
from .types.list_evaluator_families_response import ListEvaluatorFamiliesResponse

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
    evaluation_results: evaluation_results.EvaluationResultsResource
    evaluator_criteria: evaluator_criteria.EvaluatorCriteriaResource
    experiments: experiments.ExperimentsResource
    projects: projects.ProjectsResource
    annotation_criteria: annotation_criteria.AnnotationCriteriaResource
    pairwise_annotations: pairwise_annotations.PairwiseAnnotationsResource
    evaluations: evaluations.EvaluationsResource
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
        """Construct a new synchronous PatronusAPI client instance.

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
        self.evaluation_results = evaluation_results.EvaluationResultsResource(self)
        self.evaluator_criteria = evaluator_criteria.EvaluatorCriteriaResource(self)
        self.experiments = experiments.ExperimentsResource(self)
        self.projects = projects.ProjectsResource(self)
        self.annotation_criteria = annotation_criteria.AnnotationCriteriaResource(self)
        self.pairwise_annotations = pairwise_annotations.PairwiseAnnotationsResource(self)
        self.evaluations = evaluations.EvaluationsResource(self)
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
        return self.post(
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
                client_annotate_params.ClientAnnotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotateResponse,
        )

    def evaluate(
        self,
        *,
        evaluators: Iterable[client_evaluate_params.Evaluator],
        app: Optional[str] | NotGiven = NOT_GIVEN,
        capture: Literal["all", "fails-only", "none"] | NotGiven = NOT_GIVEN,
        confidence_interval_strategy: Literal["none", "full-history"] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_sample_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_attachments: Optional[Iterable[client_evaluate_params.EvaluatedModelAttachment]]
        | NotGiven = NOT_GIVEN,
        evaluated_model_gold_answer: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_input: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_output: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_retrieved_context: Union[List[str], str, None] | NotGiven = NOT_GIVEN,
        evaluated_model_system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        log_id: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        project_name: Optional[str] | NotGiven = NOT_GIVEN,
        span_id: Optional[str] | NotGiven = NOT_GIVEN,
        tags: object | NotGiven = NOT_GIVEN,
        trace_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """Requires either **input** or **output** field to be specified.

        Absence of both
        leads to an HTTP_422 (Unprocessable Entity) error.

        Args:
          evaluators: List of evaluators to evaluate against.

          app: Assigns evaluation results to the app.

              - `app` cannot be used together with `experiment_id`.
              - If `app` and `experiment_id` is omitted, `app` is set automatically to
                "default" on capture.
              - Automatically creates an app if it doesn't exist.
              - Only relevant for captured results. If will capture the results under given
                app.

          capture:
              Capture evaluation result based on given option, default is none:

              - `all` captures the result of all evaluations (pass + failed).
              - `fails-only` captures the evaluation result when evaluation failed.
              - `none` does not capture evaluation result

          confidence_interval_strategy:
              Create confidence intervals based on one of the following strategies:

              - 'none': returns None
              - 'full-history': calculates upper boundary, median, and lower boundary of
                confidence interval based on all available historic records.
              - 'generated': calculates upper boundary, median, and lower boundary of
                confidence interval based on on-flight generated sample of evaluations.

          dataset_id: The ID of the dataset from which the evaluated sample originates. This field
              serves as metadata for the evaluation. This endpoint does not ensure data
              consistency for this field. There is no guarantee that the dataset with the
              given ID is present in the Patronus AI platform, as this is a self-reported
              value.

          dataset_sample_id: The ID of the sample within the dataset. This field serves as metadata for the
              evaluation. This endpoint does not ensure data consistency for this field. There
              is no guarantee that the dataset and sample are present in the Patronus AI
              platform, as this is a self-reported value.

          evaluated_model_attachments: Optional list of attachments to be associated with the evaluation sample. This
              will be added to all evaluation results in this request. Each attachment is a
              dictionary with the following keys:

              - `url`: URL of the attachment.
              - `media_type`: Media type of the attachment (e.g., "image/jpeg", "image/png").
              - `usage_type`: Type of the attachment (e.g., "evaluated_model_system_prompt",
                "evaluated_model_input").

          evaluated_model_gold_answer: Gold answer for given evaluated model input

          evaluated_model_input: The input (prompt) provided to LLM.

          evaluated_model_output: LLM's response to the given input.

          evaluated_model_retrieved_context: Optional context retrieved from vector database. This is a list of strings, with
              the following restrictions:

              - Number of items must be less/equal than 50.
              - The sum of tokens in all elements must be less/equal than 120000, using
                o200k_base tiktoken encoding

          evaluated_model_system_prompt: The system prompt provided to the LLM.

          experiment_id: Assign evaluation results to the experiment.

              - `experiment_id` cannot be used together with `app`.
              - Only relevant for captured results. If will capture the results under
                experiment.

          project_id: Attach project with given ID to the evaluation.

              **Note**: This parameter is ignored in case project_name or experiment_id is
              provided.

          project_name: Attach project with given name to the evaluation. If project with given name
              doesn't exist, one will be created.

              **Note:** This parameter is ignored in case experiment_id is provided.

              **Note:** This parameter takes precedence over project_id.

          tags: Tags are key-value pairs used to label resources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.post(
            "/v1/evaluate",
            body=maybe_transform(
                {
                    "evaluators": evaluators,
                    "app": app,
                    "capture": capture,
                    "confidence_interval_strategy": confidence_interval_strategy,
                    "dataset_id": dataset_id,
                    "dataset_sample_id": dataset_sample_id,
                    "evaluated_model_attachments": evaluated_model_attachments,
                    "evaluated_model_gold_answer": evaluated_model_gold_answer,
                    "evaluated_model_input": evaluated_model_input,
                    "evaluated_model_output": evaluated_model_output,
                    "evaluated_model_retrieved_context": evaluated_model_retrieved_context,
                    "evaluated_model_system_prompt": evaluated_model_system_prompt,
                    "experiment_id": experiment_id,
                    "log_id": log_id,
                    "project_id": project_id,
                    "project_name": project_name,
                    "span_id": span_id,
                    "tags": tags,
                    "trace_id": trace_id,
                },
                client_evaluate_params.ClientEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    def list_apps(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAppsResponse:
        """
        List Apps

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self.get(
            "/v1/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    client_list_apps_params.ClientListAppsParams,
                ),
            ),
            cast_to=ListAppsResponse,
        )

    def list_evaluator_families(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorFamiliesResponse:
        """List Evaluator Families"""
        return self.get(
            "/v1/evaluator-families",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEvaluatorFamiliesResponse,
        )

    def list_evaluators(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorsResponse:
        """List of available evaluators for Evaluation Runs and LLM Monitoring."""
        return self.get(
            "/v1/evaluators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEvaluatorsResponse,
        )

    def whoami(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WhoamiResponse:
        """Whoami"""
        return self.get(
            "/v1/whoami",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhoamiResponse,
        )

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
    evaluation_results: evaluation_results.AsyncEvaluationResultsResource
    evaluator_criteria: evaluator_criteria.AsyncEvaluatorCriteriaResource
    experiments: experiments.AsyncExperimentsResource
    projects: projects.AsyncProjectsResource
    annotation_criteria: annotation_criteria.AsyncAnnotationCriteriaResource
    pairwise_annotations: pairwise_annotations.AsyncPairwiseAnnotationsResource
    evaluations: evaluations.AsyncEvaluationsResource
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
        """Construct a new async AsyncPatronusAPI client instance.

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
        self.evaluation_results = evaluation_results.AsyncEvaluationResultsResource(self)
        self.evaluator_criteria = evaluator_criteria.AsyncEvaluatorCriteriaResource(self)
        self.experiments = experiments.AsyncExperimentsResource(self)
        self.projects = projects.AsyncProjectsResource(self)
        self.annotation_criteria = annotation_criteria.AsyncAnnotationCriteriaResource(self)
        self.pairwise_annotations = pairwise_annotations.AsyncPairwiseAnnotationsResource(self)
        self.evaluations = evaluations.AsyncEvaluationsResource(self)
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
        return await self.post(
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
                client_annotate_params.ClientAnnotateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AnnotateResponse,
        )

    async def evaluate(
        self,
        *,
        evaluators: Iterable[client_evaluate_params.Evaluator],
        app: Optional[str] | NotGiven = NOT_GIVEN,
        capture: Literal["all", "fails-only", "none"] | NotGiven = NOT_GIVEN,
        confidence_interval_strategy: Literal["none", "full-history"] | NotGiven = NOT_GIVEN,
        dataset_id: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_sample_id: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_attachments: Optional[Iterable[client_evaluate_params.EvaluatedModelAttachment]]
        | NotGiven = NOT_GIVEN,
        evaluated_model_gold_answer: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_input: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_output: Optional[str] | NotGiven = NOT_GIVEN,
        evaluated_model_retrieved_context: Union[List[str], str, None] | NotGiven = NOT_GIVEN,
        evaluated_model_system_prompt: Optional[str] | NotGiven = NOT_GIVEN,
        experiment_id: Optional[str] | NotGiven = NOT_GIVEN,
        log_id: Optional[str] | NotGiven = NOT_GIVEN,
        project_id: Optional[str] | NotGiven = NOT_GIVEN,
        project_name: Optional[str] | NotGiven = NOT_GIVEN,
        span_id: Optional[str] | NotGiven = NOT_GIVEN,
        tags: object | NotGiven = NOT_GIVEN,
        trace_id: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluateResponse:
        """Requires either **input** or **output** field to be specified.

        Absence of both
        leads to an HTTP_422 (Unprocessable Entity) error.

        Args:
          evaluators: List of evaluators to evaluate against.

          app: Assigns evaluation results to the app.

              - `app` cannot be used together with `experiment_id`.
              - If `app` and `experiment_id` is omitted, `app` is set automatically to
                "default" on capture.
              - Automatically creates an app if it doesn't exist.
              - Only relevant for captured results. If will capture the results under given
                app.

          capture:
              Capture evaluation result based on given option, default is none:

              - `all` captures the result of all evaluations (pass + failed).
              - `fails-only` captures the evaluation result when evaluation failed.
              - `none` does not capture evaluation result

          confidence_interval_strategy:
              Create confidence intervals based on one of the following strategies:

              - 'none': returns None
              - 'full-history': calculates upper boundary, median, and lower boundary of
                confidence interval based on all available historic records.
              - 'generated': calculates upper boundary, median, and lower boundary of
                confidence interval based on on-flight generated sample of evaluations.

          dataset_id: The ID of the dataset from which the evaluated sample originates. This field
              serves as metadata for the evaluation. This endpoint does not ensure data
              consistency for this field. There is no guarantee that the dataset with the
              given ID is present in the Patronus AI platform, as this is a self-reported
              value.

          dataset_sample_id: The ID of the sample within the dataset. This field serves as metadata for the
              evaluation. This endpoint does not ensure data consistency for this field. There
              is no guarantee that the dataset and sample are present in the Patronus AI
              platform, as this is a self-reported value.

          evaluated_model_attachments: Optional list of attachments to be associated with the evaluation sample. This
              will be added to all evaluation results in this request. Each attachment is a
              dictionary with the following keys:

              - `url`: URL of the attachment.
              - `media_type`: Media type of the attachment (e.g., "image/jpeg", "image/png").
              - `usage_type`: Type of the attachment (e.g., "evaluated_model_system_prompt",
                "evaluated_model_input").

          evaluated_model_gold_answer: Gold answer for given evaluated model input

          evaluated_model_input: The input (prompt) provided to LLM.

          evaluated_model_output: LLM's response to the given input.

          evaluated_model_retrieved_context: Optional context retrieved from vector database. This is a list of strings, with
              the following restrictions:

              - Number of items must be less/equal than 50.
              - The sum of tokens in all elements must be less/equal than 120000, using
                o200k_base tiktoken encoding

          evaluated_model_system_prompt: The system prompt provided to the LLM.

          experiment_id: Assign evaluation results to the experiment.

              - `experiment_id` cannot be used together with `app`.
              - Only relevant for captured results. If will capture the results under
                experiment.

          project_id: Attach project with given ID to the evaluation.

              **Note**: This parameter is ignored in case project_name or experiment_id is
              provided.

          project_name: Attach project with given name to the evaluation. If project with given name
              doesn't exist, one will be created.

              **Note:** This parameter is ignored in case experiment_id is provided.

              **Note:** This parameter takes precedence over project_id.

          tags: Tags are key-value pairs used to label resources

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.post(
            "/v1/evaluate",
            body=await async_maybe_transform(
                {
                    "evaluators": evaluators,
                    "app": app,
                    "capture": capture,
                    "confidence_interval_strategy": confidence_interval_strategy,
                    "dataset_id": dataset_id,
                    "dataset_sample_id": dataset_sample_id,
                    "evaluated_model_attachments": evaluated_model_attachments,
                    "evaluated_model_gold_answer": evaluated_model_gold_answer,
                    "evaluated_model_input": evaluated_model_input,
                    "evaluated_model_output": evaluated_model_output,
                    "evaluated_model_retrieved_context": evaluated_model_retrieved_context,
                    "evaluated_model_system_prompt": evaluated_model_system_prompt,
                    "experiment_id": experiment_id,
                    "log_id": log_id,
                    "project_id": project_id,
                    "project_name": project_name,
                    "span_id": span_id,
                    "tags": tags,
                    "trace_id": trace_id,
                },
                client_evaluate_params.ClientEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluateResponse,
        )

    async def list_apps(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListAppsResponse:
        """
        List Apps

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self.get(
            "/v1/apps",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    client_list_apps_params.ClientListAppsParams,
                ),
            ),
            cast_to=ListAppsResponse,
        )

    async def list_evaluator_families(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorFamiliesResponse:
        """List Evaluator Families"""
        return await self.get(
            "/v1/evaluator-families",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEvaluatorFamiliesResponse,
        )

    async def list_evaluators(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListEvaluatorsResponse:
        """List of available evaluators for Evaluation Runs and LLM Monitoring."""
        return await self.get(
            "/v1/evaluators",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ListEvaluatorsResponse,
        )

    async def whoami(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WhoamiResponse:
        """Whoami"""
        return await self.get(
            "/v1/whoami",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WhoamiResponse,
        )

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
        self.evaluation_results = evaluation_results.EvaluationResultsResourceWithRawResponse(client.evaluation_results)
        self.evaluator_criteria = evaluator_criteria.EvaluatorCriteriaResourceWithRawResponse(client.evaluator_criteria)
        self.experiments = experiments.ExperimentsResourceWithRawResponse(client.experiments)
        self.projects = projects.ProjectsResourceWithRawResponse(client.projects)
        self.annotation_criteria = annotation_criteria.AnnotationCriteriaResourceWithRawResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.PairwiseAnnotationsResourceWithRawResponse(
            client.pairwise_annotations
        )
        self.evaluations = evaluations.EvaluationsResourceWithRawResponse(client.evaluations)

        self.annotate = to_raw_response_wrapper(
            client.annotate,
        )
        self.evaluate = to_raw_response_wrapper(
            client.evaluate,
        )
        self.list_apps = to_raw_response_wrapper(
            client.list_apps,
        )
        self.list_evaluator_families = to_raw_response_wrapper(
            client.list_evaluator_families,
        )
        self.list_evaluators = to_raw_response_wrapper(
            client.list_evaluators,
        )
        self.whoami = to_raw_response_wrapper(
            client.whoami,
        )


class AsyncPatronusAPIWithRawResponse:
    def __init__(self, client: AsyncPatronusAPI) -> None:
        self.datasets = datasets.AsyncDatasetsResourceWithRawResponse(client.datasets)
        self.evaluation_results = evaluation_results.AsyncEvaluationResultsResourceWithRawResponse(
            client.evaluation_results
        )
        self.evaluator_criteria = evaluator_criteria.AsyncEvaluatorCriteriaResourceWithRawResponse(
            client.evaluator_criteria
        )
        self.experiments = experiments.AsyncExperimentsResourceWithRawResponse(client.experiments)
        self.projects = projects.AsyncProjectsResourceWithRawResponse(client.projects)
        self.annotation_criteria = annotation_criteria.AsyncAnnotationCriteriaResourceWithRawResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.AsyncPairwiseAnnotationsResourceWithRawResponse(
            client.pairwise_annotations
        )
        self.evaluations = evaluations.AsyncEvaluationsResourceWithRawResponse(client.evaluations)

        self.annotate = async_to_raw_response_wrapper(
            client.annotate,
        )
        self.evaluate = async_to_raw_response_wrapper(
            client.evaluate,
        )
        self.list_apps = async_to_raw_response_wrapper(
            client.list_apps,
        )
        self.list_evaluator_families = async_to_raw_response_wrapper(
            client.list_evaluator_families,
        )
        self.list_evaluators = async_to_raw_response_wrapper(
            client.list_evaluators,
        )
        self.whoami = async_to_raw_response_wrapper(
            client.whoami,
        )


class PatronusAPIWithStreamedResponse:
    def __init__(self, client: PatronusAPI) -> None:
        self.datasets = datasets.DatasetsResourceWithStreamingResponse(client.datasets)
        self.evaluation_results = evaluation_results.EvaluationResultsResourceWithStreamingResponse(
            client.evaluation_results
        )
        self.evaluator_criteria = evaluator_criteria.EvaluatorCriteriaResourceWithStreamingResponse(
            client.evaluator_criteria
        )
        self.experiments = experiments.ExperimentsResourceWithStreamingResponse(client.experiments)
        self.projects = projects.ProjectsResourceWithStreamingResponse(client.projects)
        self.annotation_criteria = annotation_criteria.AnnotationCriteriaResourceWithStreamingResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.PairwiseAnnotationsResourceWithStreamingResponse(
            client.pairwise_annotations
        )
        self.evaluations = evaluations.EvaluationsResourceWithStreamingResponse(client.evaluations)

        self.annotate = to_streamed_response_wrapper(
            client.annotate,
        )
        self.evaluate = to_streamed_response_wrapper(
            client.evaluate,
        )
        self.list_apps = to_streamed_response_wrapper(
            client.list_apps,
        )
        self.list_evaluator_families = to_streamed_response_wrapper(
            client.list_evaluator_families,
        )
        self.list_evaluators = to_streamed_response_wrapper(
            client.list_evaluators,
        )
        self.whoami = to_streamed_response_wrapper(
            client.whoami,
        )


class AsyncPatronusAPIWithStreamedResponse:
    def __init__(self, client: AsyncPatronusAPI) -> None:
        self.datasets = datasets.AsyncDatasetsResourceWithStreamingResponse(client.datasets)
        self.evaluation_results = evaluation_results.AsyncEvaluationResultsResourceWithStreamingResponse(
            client.evaluation_results
        )
        self.evaluator_criteria = evaluator_criteria.AsyncEvaluatorCriteriaResourceWithStreamingResponse(
            client.evaluator_criteria
        )
        self.experiments = experiments.AsyncExperimentsResourceWithStreamingResponse(client.experiments)
        self.projects = projects.AsyncProjectsResourceWithStreamingResponse(client.projects)
        self.annotation_criteria = annotation_criteria.AsyncAnnotationCriteriaResourceWithStreamingResponse(
            client.annotation_criteria
        )
        self.pairwise_annotations = pairwise_annotations.AsyncPairwiseAnnotationsResourceWithStreamingResponse(
            client.pairwise_annotations
        )
        self.evaluations = evaluations.AsyncEvaluationsResourceWithStreamingResponse(client.evaluations)

        self.annotate = async_to_streamed_response_wrapper(
            client.annotate,
        )
        self.evaluate = async_to_streamed_response_wrapper(
            client.evaluate,
        )
        self.list_apps = async_to_streamed_response_wrapper(
            client.list_apps,
        )
        self.list_evaluator_families = async_to_streamed_response_wrapper(
            client.list_evaluator_families,
        )
        self.list_evaluators = async_to_streamed_response_wrapper(
            client.list_evaluators,
        )
        self.whoami = async_to_streamed_response_wrapper(
            client.whoami,
        )


Client = PatronusAPI

AsyncClient = AsyncPatronusAPI

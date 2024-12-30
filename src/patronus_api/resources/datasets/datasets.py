# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, Optional, cast
from typing_extensions import Literal

import httpx

from .csv import (
    CsvResource,
    AsyncCsvResource,
    CsvResourceWithRawResponse,
    AsyncCsvResourceWithRawResponse,
    CsvResourceWithStreamingResponse,
    AsyncCsvResourceWithStreamingResponse,
)
from .data import (
    DataResource,
    AsyncDataResource,
    DataResourceWithRawResponse,
    AsyncDataResourceWithRawResponse,
    DataResourceWithStreamingResponse,
    AsyncDataResourceWithStreamingResponse,
)
from .jsonl import (
    JsonlResource,
    AsyncJsonlResource,
    JsonlResourceWithRawResponse,
    AsyncJsonlResourceWithRawResponse,
    JsonlResourceWithStreamingResponse,
    AsyncJsonlResourceWithStreamingResponse,
)
from ...types import dataset_list_params, dataset_create_params, dataset_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven, FileTypes
from ..._utils import (
    extract_files,
    maybe_transform,
    deepcopy_minimal,
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
from ...types.get_datasets_response import GetDatasetsResponse
from ...types.list_datasets_response import ListDatasetsResponse
from ...types.create_dataset_response import CreateDatasetResponse
from ...types.update_dataset_response import UpdateDatasetResponse

__all__ = ["DatasetsResource", "AsyncDatasetsResource"]


class DatasetsResource(SyncAPIResource):
    @cached_property
    def data(self) -> DataResource:
        return DataResource(self._client)

    @cached_property
    def jsonl(self) -> JsonlResource:
        return JsonlResource(self._client)

    @cached_property
    def csv(self) -> CsvResource:
        return CsvResource(self._client)

    @cached_property
    def with_raw_response(self) -> DatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return DatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return DatasetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        dataset_name: str,
        file: FileTypes,
        custom_field_mapping: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatasetResponse:
        """
        This endpoint allows you to create a dataset with a given name from a provided
        file.

        The dataset can contain the following attributes:

        - `evaluated_model_system_prompt` - text
        - `evaluated_model_retrieved_context` - text array
        - `evaluated_model_input` - text
        - `evaluated_model_output` - text
        - `evaluated_model_gold_answer` - text
        - `meta_evaluated_model_name` - text
        - `meta_evaluated_model_provider` -text
        - `meta_evaluated_model_selected_model` - text
        - `meta_evaluated_model_params` - map (string -> text | number)

        All attributes are optional, but in principle, at least `evaluated_model_input`
        or `evaluated_model_output` should be provided.

        Whether other fields are required depends on the evaluations you plan to
        perform. Some evaluators require retrieved context, so
        `evaluated_model_retrieved_context` must be provided for them. For exact field
        requirements, see the evaluators' documentation.

        #### File Format

        The uploaded file should be in _CSV_ or _JSONL_ format.

        - **CSV** file should contain a header row with the attributes defined above.
          Fields `evaluated_model_retrieved_context` and `meta_evaluated_model_params`
          must be JSON encoded. The CSV should use commas as separators.

        - **JSONL** file should have JSON-encoded objects with keys set to the
          attributes defined above. JSON objects should be separated by a new line.

        ### Limits

        The file size cannot be larger than 20 MiB. The file cannot contain more than 30
        000 samples.

        ### Custom Field Mapping

        The `custom_field_mapping` field is optional. It should be a JSON-encoded string
        where the key is the standardized field name (as defined above) and the value is
        the custom field name present in the provided dataset file. This mapping allows
        for flexible field naming in your dataset. The mapping value can be also a list,
        in that way the fields will be concatenated depending on a field type.

        ### Example request

        ```
        curl -X POST https://api.patronus.ai/v1/datasets \\
             -H "x-api-key: <your_api_key>" \\
             -F "file=@<path_to_your_file>" \\
             -F "dataset_name=<name for created dataset>" \\
             -F 'custom_field_mapping={"evaluated_model_output": ["my-custom-field-name", "another-field"]}'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "dataset_name": dataset_name,
                "file": file,
                "custom_field_mapping": custom_field_mapping,
                "dataset_description": dataset_description,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/datasets",
            body=maybe_transform(body, dataset_create_params.DatasetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
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
    ) -> GetDatasetsResponse:
        """
        Get Dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/datasets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetDatasetsResponse,
        )

    def update(
        self,
        dataset_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateDatasetResponse:
        """
        Update Dataset

        Args:
          name: The name of the dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return self._patch(
            f"/v1/datasets/{dataset_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateDatasetResponse,
        )

    def list(
        self,
        *,
        type: Optional[Literal["Patronus Managed", "User Managed"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDatasetsResponse:
        """
        List Datasets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, dataset_list_params.DatasetListParams),
            ),
            cast_to=ListDatasetsResponse,
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
        Delete Dataset

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
            f"/v1/datasets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDatasetsResource(AsyncAPIResource):
    @cached_property
    def data(self) -> AsyncDataResource:
        return AsyncDataResource(self._client)

    @cached_property
    def jsonl(self) -> AsyncJsonlResource:
        return AsyncJsonlResource(self._client)

    @cached_property
    def csv(self) -> AsyncCsvResource:
        return AsyncCsvResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDatasetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDatasetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDatasetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/patronus-api-python#with_streaming_response
        """
        return AsyncDatasetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        dataset_name: str,
        file: FileTypes,
        custom_field_mapping: Optional[str] | NotGiven = NOT_GIVEN,
        dataset_description: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreateDatasetResponse:
        """
        This endpoint allows you to create a dataset with a given name from a provided
        file.

        The dataset can contain the following attributes:

        - `evaluated_model_system_prompt` - text
        - `evaluated_model_retrieved_context` - text array
        - `evaluated_model_input` - text
        - `evaluated_model_output` - text
        - `evaluated_model_gold_answer` - text
        - `meta_evaluated_model_name` - text
        - `meta_evaluated_model_provider` -text
        - `meta_evaluated_model_selected_model` - text
        - `meta_evaluated_model_params` - map (string -> text | number)

        All attributes are optional, but in principle, at least `evaluated_model_input`
        or `evaluated_model_output` should be provided.

        Whether other fields are required depends on the evaluations you plan to
        perform. Some evaluators require retrieved context, so
        `evaluated_model_retrieved_context` must be provided for them. For exact field
        requirements, see the evaluators' documentation.

        #### File Format

        The uploaded file should be in _CSV_ or _JSONL_ format.

        - **CSV** file should contain a header row with the attributes defined above.
          Fields `evaluated_model_retrieved_context` and `meta_evaluated_model_params`
          must be JSON encoded. The CSV should use commas as separators.

        - **JSONL** file should have JSON-encoded objects with keys set to the
          attributes defined above. JSON objects should be separated by a new line.

        ### Limits

        The file size cannot be larger than 20 MiB. The file cannot contain more than 30
        000 samples.

        ### Custom Field Mapping

        The `custom_field_mapping` field is optional. It should be a JSON-encoded string
        where the key is the standardized field name (as defined above) and the value is
        the custom field name present in the provided dataset file. This mapping allows
        for flexible field naming in your dataset. The mapping value can be also a list,
        in that way the fields will be concatenated depending on a field type.

        ### Example request

        ```
        curl -X POST https://api.patronus.ai/v1/datasets \\
             -H "x-api-key: <your_api_key>" \\
             -F "file=@<path_to_your_file>" \\
             -F "dataset_name=<name for created dataset>" \\
             -F 'custom_field_mapping={"evaluated_model_output": ["my-custom-field-name", "another-field"]}'
        ```

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "dataset_name": dataset_name,
                "file": file,
                "custom_field_mapping": custom_field_mapping,
                "dataset_description": dataset_description,
            }
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/datasets",
            body=await async_maybe_transform(body, dataset_create_params.DatasetCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateDatasetResponse,
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
    ) -> GetDatasetsResponse:
        """
        Get Dataset

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/datasets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GetDatasetsResponse,
        )

    async def update(
        self,
        dataset_id: str,
        *,
        description: Optional[str] | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpdateDatasetResponse:
        """
        Update Dataset

        Args:
          name: The name of the dataset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dataset_id:
            raise ValueError(f"Expected a non-empty value for `dataset_id` but received {dataset_id!r}")
        return await self._patch(
            f"/v1/datasets/{dataset_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                dataset_update_params.DatasetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UpdateDatasetResponse,
        )

    async def list(
        self,
        *,
        type: Optional[Literal["Patronus Managed", "User Managed"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ListDatasetsResponse:
        """
        List Datasets

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/datasets",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, dataset_list_params.DatasetListParams),
            ),
            cast_to=ListDatasetsResponse,
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
        Delete Dataset

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
            f"/v1/datasets/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DatasetsResourceWithRawResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            datasets.update,
        )
        self.list = to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = to_raw_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def data(self) -> DataResourceWithRawResponse:
        return DataResourceWithRawResponse(self._datasets.data)

    @cached_property
    def jsonl(self) -> JsonlResourceWithRawResponse:
        return JsonlResourceWithRawResponse(self._datasets.jsonl)

    @cached_property
    def csv(self) -> CsvResourceWithRawResponse:
        return CsvResourceWithRawResponse(self._datasets.csv)


class AsyncDatasetsResourceWithRawResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_raw_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            datasets.update,
        )
        self.list = async_to_raw_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def data(self) -> AsyncDataResourceWithRawResponse:
        return AsyncDataResourceWithRawResponse(self._datasets.data)

    @cached_property
    def jsonl(self) -> AsyncJsonlResourceWithRawResponse:
        return AsyncJsonlResourceWithRawResponse(self._datasets.jsonl)

    @cached_property
    def csv(self) -> AsyncCsvResourceWithRawResponse:
        return AsyncCsvResourceWithRawResponse(self._datasets.csv)


class DatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: DatasetsResource) -> None:
        self._datasets = datasets

        self.create = to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = to_streamed_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def data(self) -> DataResourceWithStreamingResponse:
        return DataResourceWithStreamingResponse(self._datasets.data)

    @cached_property
    def jsonl(self) -> JsonlResourceWithStreamingResponse:
        return JsonlResourceWithStreamingResponse(self._datasets.jsonl)

    @cached_property
    def csv(self) -> CsvResourceWithStreamingResponse:
        return CsvResourceWithStreamingResponse(self._datasets.csv)


class AsyncDatasetsResourceWithStreamingResponse:
    def __init__(self, datasets: AsyncDatasetsResource) -> None:
        self._datasets = datasets

        self.create = async_to_streamed_response_wrapper(
            datasets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            datasets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            datasets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            datasets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            datasets.delete,
        )

    @cached_property
    def data(self) -> AsyncDataResourceWithStreamingResponse:
        return AsyncDataResourceWithStreamingResponse(self._datasets.data)

    @cached_property
    def jsonl(self) -> AsyncJsonlResourceWithStreamingResponse:
        return AsyncJsonlResourceWithStreamingResponse(self._datasets.jsonl)

    @cached_property
    def csv(self) -> AsyncCsvResourceWithStreamingResponse:
        return AsyncCsvResourceWithStreamingResponse(self._datasets.csv)

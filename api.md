# PatronusAPI

Types:

```python
from patronus_api.types import (
    AnnotateResponse,
    EvaluateResponse,
    ListAppsResponse,
    ListEvaluatorFamiliesResponse,
    ListEvaluatorsResponse,
    WhoamiResponse,
)
```

Methods:

- <code title="post /v1/annotate">client.<a href="./src/patronus_api/_client.py">annotate</a>(\*\*<a href="src/patronus_api/types/client_annotate_params.py">params</a>) -> <a href="./src/patronus_api/types/annotate_response.py">AnnotateResponse</a></code>
- <code title="post /v1/evaluate">client.<a href="./src/patronus_api/_client.py">evaluate</a>(\*\*<a href="src/patronus_api/types/client_evaluate_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluate_response.py">EvaluateResponse</a></code>
- <code title="get /v1/apps">client.<a href="./src/patronus_api/_client.py">list_apps</a>(\*\*<a href="src/patronus_api/types/client_list_apps_params.py">params</a>) -> <a href="./src/patronus_api/types/list_apps_response.py">ListAppsResponse</a></code>
- <code title="get /v1/evaluator-families">client.<a href="./src/patronus_api/_client.py">list_evaluator_families</a>() -> <a href="./src/patronus_api/types/list_evaluator_families_response.py">ListEvaluatorFamiliesResponse</a></code>
- <code title="get /v1/evaluators">client.<a href="./src/patronus_api/_client.py">list_evaluators</a>() -> <a href="./src/patronus_api/types/list_evaluators_response.py">ListEvaluatorsResponse</a></code>
- <code title="get /v1/whoami">client.<a href="./src/patronus_api/_client.py">whoami</a>() -> <a href="./src/patronus_api/types/whoami_response.py">WhoamiResponse</a></code>

# Datasets

Types:

```python
from patronus_api.types import (
    Dataset,
    DatasetHasValues,
    DatasetType,
    DatasetRetrieveResponse,
    DatasetUpdateResponse,
    DatasetListResponse,
    DatasetListDataResponse,
    DatasetUploadResponse,
)
```

Methods:

- <code title="get /v1/datasets/{id}">client.datasets.<a href="./src/patronus_api/resources/datasets.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/dataset_retrieve_response.py">DatasetRetrieveResponse</a></code>
- <code title="patch /v1/datasets/{dataset_id}">client.datasets.<a href="./src/patronus_api/resources/datasets.py">update</a>(dataset_id, \*\*<a href="src/patronus_api/types/dataset_update_params.py">params</a>) -> <a href="./src/patronus_api/types/dataset_update_response.py">DatasetUpdateResponse</a></code>
- <code title="get /v1/datasets">client.datasets.<a href="./src/patronus_api/resources/datasets.py">list</a>(\*\*<a href="src/patronus_api/types/dataset_list_params.py">params</a>) -> <a href="./src/patronus_api/types/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="delete /v1/datasets/{id}">client.datasets.<a href="./src/patronus_api/resources/datasets.py">delete</a>(id) -> None</code>
- <code title="get /v1/datasets/{id}/csv">client.datasets.<a href="./src/patronus_api/resources/datasets.py">download_csv</a>(id) -> None</code>
- <code title="get /v1/datasets/{id}/jsonl">client.datasets.<a href="./src/patronus_api/resources/datasets.py">download_jsonl</a>(id) -> None</code>
- <code title="get /v1/datasets/{id}/data">client.datasets.<a href="./src/patronus_api/resources/datasets.py">list_data</a>(id) -> <a href="./src/patronus_api/types/dataset_list_data_response.py">DatasetListDataResponse</a></code>
- <code title="post /v1/datasets">client.datasets.<a href="./src/patronus_api/resources/datasets.py">upload</a>(\*\*<a href="src/patronus_api/types/dataset_upload_params.py">params</a>) -> <a href="./src/patronus_api/types/dataset_upload_response.py">DatasetUploadResponse</a></code>

# EvaluationResults

Types:

```python
from patronus_api.types import (
    EvaluationExplainStrategies,
    EvaluationResult,
    EvaluationResultRetrieveResponse,
    EvaluationResultCreateBatchResponse,
    EvaluationResultListTagsResponse,
    EvaluationResultSearchResponse,
)
```

Methods:

- <code title="get /v1/evaluation-results/{id}">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/evaluation_result_retrieve_response.py">EvaluationResultRetrieveResponse</a></code>
- <code title="post /v1/evaluation-results/batch">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">create_batch</a>(\*\*<a href="src/patronus_api/types/evaluation_result_create_batch_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluation_result_create_batch_response.py">EvaluationResultCreateBatchResponse</a></code>
- <code title="get /v1/evaluation-results/tags">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">list_tags</a>() -> <a href="./src/patronus_api/types/evaluation_result_list_tags_response.py">EvaluationResultListTagsResponse</a></code>
- <code title="post /v1/evaluation-results/search">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">search</a>(\*\*<a href="src/patronus_api/types/evaluation_result_search_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluation_result_search_response.py">EvaluationResultSearchResponse</a></code>

## Favorite

Methods:

- <code title="post /v1/evaluation-results/{id}/favorite">client.evaluation_results.favorite.<a href="./src/patronus_api/resources/evaluation_results/favorite.py">mark</a>(id) -> None</code>
- <code title="delete /v1/evaluation-results/{id}/favorite">client.evaluation_results.favorite.<a href="./src/patronus_api/resources/evaluation_results/favorite.py">unmark</a>(id) -> None</code>

## EvaluationFeedback

Methods:

- <code title="delete /v1/evaluation-results/{id}/evaluation-feedback">client.evaluation_results.evaluation_feedback.<a href="./src/patronus_api/resources/evaluation_results/evaluation_feedback.py">delete</a>(id) -> None</code>
- <code title="post /v1/evaluation-results/{id}/evaluation-feedback">client.evaluation_results.evaluation_feedback.<a href="./src/patronus_api/resources/evaluation_results/evaluation_feedback.py">submit</a>(id, \*\*<a href="src/patronus_api/types/evaluation_results/evaluation_feedback_submit_params.py">params</a>) -> None</code>

# EvaluatorCriteria

Types:

```python
from patronus_api.types import (
    EvaluatorCriteria,
    EvaluatorCriterionCreateResponse,
    EvaluatorCriterionListResponse,
    EvaluatorCriterionAddRevisionResponse,
    EvaluatorCriterionArchiveResponse,
)
```

Methods:

- <code title="post /v1/evaluator-criteria">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria.py">create</a>(\*\*<a href="src/patronus_api/types/evaluator_criterion_create_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluator_criterion_create_response.py">EvaluatorCriterionCreateResponse</a></code>
- <code title="get /v1/evaluator-criteria">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria.py">list</a>(\*\*<a href="src/patronus_api/types/evaluator_criterion_list_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluator_criterion_list_response.py">EvaluatorCriterionListResponse</a></code>
- <code title="post /v1/evaluator-criteria/{public_id}/revision">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria.py">add_revision</a>(public_id, \*\*<a href="src/patronus_api/types/evaluator_criterion_add_revision_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluator_criterion_add_revision_response.py">EvaluatorCriterionAddRevisionResponse</a></code>
- <code title="patch /v1/evaluator-criteria/{public_id}/archive">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria.py">archive</a>(public_id) -> <a href="./src/patronus_api/types/evaluator_criterion_archive_response.py">EvaluatorCriterionArchiveResponse</a></code>

# Experiments

Types:

```python
from patronus_api.types import (
    Experiment,
    ExperimentCreateResponse,
    ExperimentRetrieveResponse,
    ExperimentListResponse,
)
```

Methods:

- <code title="post /v1/experiments">client.experiments.<a href="./src/patronus_api/resources/experiments.py">create</a>(\*\*<a href="src/patronus_api/types/experiment_create_params.py">params</a>) -> <a href="./src/patronus_api/types/experiment_create_response.py">ExperimentCreateResponse</a></code>
- <code title="get /v1/experiments/{id}">client.experiments.<a href="./src/patronus_api/resources/experiments.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/experiment_retrieve_response.py">ExperimentRetrieveResponse</a></code>
- <code title="get /v1/experiments">client.experiments.<a href="./src/patronus_api/resources/experiments.py">list</a>(\*\*<a href="src/patronus_api/types/experiment_list_params.py">params</a>) -> <a href="./src/patronus_api/types/experiment_list_response.py">ExperimentListResponse</a></code>
- <code title="delete /v1/experiments/{id}">client.experiments.<a href="./src/patronus_api/resources/experiments.py">delete</a>(id) -> None</code>

# Projects

Types:

```python
from patronus_api.types import Project, ProjectRetrieveResponse, ProjectListResponse
```

Methods:

- <code title="post /v1/projects">client.projects.<a href="./src/patronus_api/resources/projects.py">create</a>(\*\*<a href="src/patronus_api/types/project_create_params.py">params</a>) -> <a href="./src/patronus_api/types/project.py">Project</a></code>
- <code title="get /v1/projects/{id}">client.projects.<a href="./src/patronus_api/resources/projects.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/project_retrieve_response.py">ProjectRetrieveResponse</a></code>
- <code title="get /v1/projects">client.projects.<a href="./src/patronus_api/resources/projects.py">list</a>(\*\*<a href="src/patronus_api/types/project_list_params.py">params</a>) -> <a href="./src/patronus_api/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="delete /v1/projects/{id}">client.projects.<a href="./src/patronus_api/resources/projects.py">delete</a>(id) -> None</code>

# AnnotationCriteria

Types:

```python
from patronus_api.types import (
    AnnotationCategory,
    AnnotationCriteria,
    AnnotationType,
    AnnotationCriterionCreateResponse,
    AnnotationCriterionRetrieveResponse,
    AnnotationCriterionUpdateResponse,
    AnnotationCriterionListResponse,
)
```

Methods:

- <code title="post /v1/annotation-criteria">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">create</a>(\*\*<a href="src/patronus_api/types/annotation_criterion_create_params.py">params</a>) -> <a href="./src/patronus_api/types/annotation_criterion_create_response.py">AnnotationCriterionCreateResponse</a></code>
- <code title="get /v1/annotation-criteria/{id}">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/annotation_criterion_retrieve_response.py">AnnotationCriterionRetrieveResponse</a></code>
- <code title="put /v1/annotation-criteria/{id}">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">update</a>(id, \*\*<a href="src/patronus_api/types/annotation_criterion_update_params.py">params</a>) -> <a href="./src/patronus_api/types/annotation_criterion_update_response.py">AnnotationCriterionUpdateResponse</a></code>
- <code title="get /v1/annotation-criteria">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">list</a>(\*\*<a href="src/patronus_api/types/annotation_criterion_list_params.py">params</a>) -> <a href="./src/patronus_api/types/annotation_criterion_list_response.py">AnnotationCriterionListResponse</a></code>
- <code title="delete /v1/annotation-criteria/{id}">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">delete</a>(id) -> None</code>

# PairwiseAnnotations

Types:

```python
from patronus_api.types import (
    PairwiseAnnotation,
    PairwiseAnnotationCreateResponse,
    PairwiseAnnotationListResponse,
    PairwiseAnnotationGetBatchResponse,
)
```

Methods:

- <code title="post /v1/pairwise-annotations">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">create</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_create_params.py">params</a>) -> <a href="./src/patronus_api/types/pairwise_annotation_create_response.py">PairwiseAnnotationCreateResponse</a></code>
- <code title="get /v1/pairwise-annotations">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">list</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_list_params.py">params</a>) -> <a href="./src/patronus_api/types/pairwise_annotation_list_response.py">PairwiseAnnotationListResponse</a></code>
- <code title="delete /v1/pairwise-annotations">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">delete</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_delete_params.py">params</a>) -> None</code>
- <code title="post /v1/pairwise-annotations/get-batch">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">get_batch</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_get_batch_params.py">params</a>) -> <a href="./src/patronus_api/types/pairwise_annotation_get_batch_response.py">PairwiseAnnotationGetBatchResponse</a></code>

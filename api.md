# Datasets

Types:

```python
from patronus_api.types import (
    CreateDatasetResponse,
    GetDatasetsResponse,
    ListDatasetsResponse,
    UpdateDatasetResponse,
)
```

Methods:

- <code title="post /v1/datasets">client.datasets.<a href="./src/patronus_api/resources/datasets/datasets.py">create</a>(\*\*<a href="src/patronus_api/types/dataset_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_dataset_response.py">CreateDatasetResponse</a></code>
- <code title="get /v1/datasets/{id}">client.datasets.<a href="./src/patronus_api/resources/datasets/datasets.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/get_datasets_response.py">GetDatasetsResponse</a></code>
- <code title="patch /v1/datasets/{dataset_id}">client.datasets.<a href="./src/patronus_api/resources/datasets/datasets.py">update</a>(dataset_id, \*\*<a href="src/patronus_api/types/dataset_update_params.py">params</a>) -> <a href="./src/patronus_api/types/update_dataset_response.py">UpdateDatasetResponse</a></code>
- <code title="get /v1/datasets">client.datasets.<a href="./src/patronus_api/resources/datasets/datasets.py">list</a>(\*\*<a href="src/patronus_api/types/dataset_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_datasets_response.py">ListDatasetsResponse</a></code>
- <code title="delete /v1/datasets/{id}">client.datasets.<a href="./src/patronus_api/resources/datasets/datasets.py">delete</a>(id) -> None</code>

## Data

Types:

```python
from patronus_api.types.datasets import ListDatasetDataResponse
```

Methods:

- <code title="get /v1/datasets/{id}/data">client.datasets.data.<a href="./src/patronus_api/resources/datasets/data.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/datasets/list_dataset_data_response.py">ListDatasetDataResponse</a></code>

## Jsonl

Types:

```python
from patronus_api.types.datasets import JsonlRetrieveResponse
```

Methods:

- <code title="get /v1/datasets/{id}/jsonl">client.datasets.jsonl.<a href="./src/patronus_api/resources/datasets/jsonl.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/datasets/jsonl_retrieve_response.py">object</a></code>

## Csv

Types:

```python
from patronus_api.types.datasets import CsvRetrieveResponse
```

Methods:

- <code title="get /v1/datasets/{id}/csv">client.datasets.csv.<a href="./src/patronus_api/resources/datasets/csv.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/datasets/csv_retrieve_response.py">object</a></code>

# Evaluations

Types:

```python
from patronus_api.types import EvaluateResponse
```

Methods:

- <code title="post /v1/evaluate">client.evaluations.<a href="./src/patronus_api/resources/evaluations.py">evaluate</a>(\*\*<a href="src/patronus_api/types/evaluation_evaluate_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluate_response.py">EvaluateResponse</a></code>

# EvaluationResults

Types:

```python
from patronus_api.types import (
    CreateEvaluationResultsBatchResponse,
    EvaluateResultSearchResponse,
    GetEvaluationResult,
)
```

Methods:

- <code title="get /v1/evaluation-results/{id}">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/get_evaluation_result.py">GetEvaluationResult</a></code>
- <code title="post /v1/evaluation-results/batch">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">batch_create</a>(\*\*<a href="src/patronus_api/types/evaluation_result_batch_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_evaluation_results_batch_response.py">CreateEvaluationResultsBatchResponse</a></code>
- <code title="post /v1/evaluation-results/{id}/evaluation-feedback">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">evaluation_feedback</a>(id, \*\*<a href="src/patronus_api/types/evaluation_result_evaluation_feedback_params.py">params</a>) -> None</code>
- <code title="post /v1/evaluation-results/{id}/favorite">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">favorite</a>(id) -> None</code>
- <code title="delete /v1/evaluation-results/{id}/evaluation-feedback">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">remove_evaluation_feedback</a>(id) -> None</code>
- <code title="post /v1/evaluation-results/search">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">search</a>(\*\*<a href="src/patronus_api/types/evaluation_result_search_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluate_result_search_response.py">EvaluateResultSearchResponse</a></code>
- <code title="delete /v1/evaluation-results/{id}/favorite">client.evaluation_results.<a href="./src/patronus_api/resources/evaluation_results/evaluation_results.py">unfavorite</a>(id) -> None</code>

## Tags

Types:

```python
from patronus_api.types.evaluation_results import ListTagsResponse
```

Methods:

- <code title="get /v1/evaluation-results/tags">client.evaluation_results.tags.<a href="./src/patronus_api/resources/evaluation_results/tags.py">list</a>() -> <a href="./src/patronus_api/types/evaluation_results/list_tags_response.py">ListTagsResponse</a></code>

# EvaluatorProfiles

Types:

```python
from patronus_api.types import (
    AddEvaluatorProfileRevision,
    ArchiveEvaluatorProfileResponse,
    CreateEvaluatorProfileResponse,
    ListEvaluatorProfilesResponse,
)
```

Methods:

- <code title="post /v1/evaluator-profiles">client.evaluator_profiles.<a href="./src/patronus_api/resources/evaluator_profiles.py">create</a>(\*\*<a href="src/patronus_api/types/evaluator_profile_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_evaluator_profile_response.py">CreateEvaluatorProfileResponse</a></code>
- <code title="get /v1/evaluator-profiles">client.evaluator_profiles.<a href="./src/patronus_api/resources/evaluator_profiles.py">list</a>(\*\*<a href="src/patronus_api/types/evaluator_profile_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_evaluator_profiles_response.py">ListEvaluatorProfilesResponse</a></code>
- <code title="patch /v1/evaluator-profiles/{public_id}/archive">client.evaluator_profiles.<a href="./src/patronus_api/resources/evaluator_profiles.py">archive</a>(public_id) -> <a href="./src/patronus_api/types/archive_evaluator_profile_response.py">ArchiveEvaluatorProfileResponse</a></code>
- <code title="post /v1/evaluator-profiles/{public_id}/revision">client.evaluator_profiles.<a href="./src/patronus_api/resources/evaluator_profiles.py">revision</a>(public_id, \*\*<a href="src/patronus_api/types/evaluator_profile_revision_params.py">params</a>) -> <a href="./src/patronus_api/types/add_evaluator_profile_revision.py">AddEvaluatorProfileRevision</a></code>

# EvaluatorCriteria

Types:

```python
from patronus_api.types import (
    ArchiveEvaluatorCriteriaResponse,
    CreateEvaluatorCriteriaResponse,
    ListEvaluatorCriteriaResponse,
)
```

Methods:

- <code title="post /v1/evaluator-criteria">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria/evaluator_criteria.py">create</a>(\*\*<a href="src/patronus_api/types/evaluator_criterion_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_evaluator_criteria_response.py">CreateEvaluatorCriteriaResponse</a></code>
- <code title="get /v1/evaluator-criteria">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria/evaluator_criteria.py">list</a>(\*\*<a href="src/patronus_api/types/evaluator_criterion_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_evaluator_criteria_response.py">ListEvaluatorCriteriaResponse</a></code>
- <code title="patch /v1/evaluator-criteria/{public_id}/archive">client.evaluator_criteria.<a href="./src/patronus_api/resources/evaluator_criteria/evaluator_criteria.py">archive</a>(public_id) -> <a href="./src/patronus_api/types/archive_evaluator_criteria_response.py">ArchiveEvaluatorCriteriaResponse</a></code>

## Revision

Types:

```python
from patronus_api.types.evaluator_criteria import AddEvaluatorCriteriaRevision
```

Methods:

- <code title="post /v1/evaluator-criteria/{public_id}/revision">client.evaluator_criteria.revision.<a href="./src/patronus_api/resources/evaluator_criteria/revision.py">create</a>(public_id, \*\*<a href="src/patronus_api/types/evaluator_criteria/revision_create_params.py">params</a>) -> <a href="./src/patronus_api/types/evaluator_criteria/add_evaluator_criteria_revision.py">AddEvaluatorCriteriaRevision</a></code>

# Experiments

Types:

```python
from patronus_api.types import (
    CreateExperimentResponse,
    GetExperimentResponse,
    ListExperimentResponse,
)
```

Methods:

- <code title="post /v1/experiments">client.experiments.<a href="./src/patronus_api/resources/experiments.py">create</a>(\*\*<a href="src/patronus_api/types/experiment_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_experiment_response.py">CreateExperimentResponse</a></code>
- <code title="get /v1/experiments/{id}">client.experiments.<a href="./src/patronus_api/resources/experiments.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/get_experiment_response.py">GetExperimentResponse</a></code>
- <code title="get /v1/experiments">client.experiments.<a href="./src/patronus_api/resources/experiments.py">list</a>(\*\*<a href="src/patronus_api/types/experiment_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_experiment_response.py">ListExperimentResponse</a></code>
- <code title="delete /v1/experiments/{id}">client.experiments.<a href="./src/patronus_api/resources/experiments.py">delete</a>(id) -> None</code>

# Feedback

Types:

```python
from patronus_api.types import CreateFeedbackResponse, ListFeedbackResponse
```

Methods:

- <code title="get /v1/feedback">client.feedback.<a href="./src/patronus_api/resources/feedback.py">retrieve</a>(\*\*<a href="src/patronus_api/types/feedback_retrieve_params.py">params</a>) -> <a href="./src/patronus_api/types/list_feedback_response.py">ListFeedbackResponse</a></code>
- <code title="delete /v1/feedback/{id}">client.feedback.<a href="./src/patronus_api/resources/feedback.py">delete</a>(id) -> None</code>
- <code title="post /v1/feedback">client.feedback.<a href="./src/patronus_api/resources/feedback.py">give</a>(\*\*<a href="src/patronus_api/types/feedback_give_params.py">params</a>) -> <a href="./src/patronus_api/types/create_feedback_response.py">CreateFeedbackResponse</a></code>

# Projects

Types:

```python
from patronus_api.types import GetProjectResponse, ListProjectsResponse, Project
```

Methods:

- <code title="post /v1/projects">client.projects.<a href="./src/patronus_api/resources/projects.py">create</a>(\*\*<a href="src/patronus_api/types/project_create_params.py">params</a>) -> <a href="./src/patronus_api/types/project.py">Project</a></code>
- <code title="get /v1/projects/{id}">client.projects.<a href="./src/patronus_api/resources/projects.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/get_project_response.py">GetProjectResponse</a></code>
- <code title="get /v1/projects">client.projects.<a href="./src/patronus_api/resources/projects.py">list</a>(\*\*<a href="src/patronus_api/types/project_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_projects_response.py">ListProjectsResponse</a></code>
- <code title="delete /v1/projects/{id}">client.projects.<a href="./src/patronus_api/resources/projects.py">delete</a>(id) -> None</code>

# Evaluators

Types:

```python
from patronus_api.types import ListEvaluatorsResponse
```

Methods:

- <code title="get /v1/evaluators">client.evaluators.<a href="./src/patronus_api/resources/evaluators.py">list</a>() -> <a href="./src/patronus_api/types/list_evaluators_response.py">ListEvaluatorsResponse</a></code>

# Misc

Types:

```python
from patronus_api.types import WhoAmIResponse
```

Methods:

- <code title="get /v1/whoami">client.misc.<a href="./src/patronus_api/resources/misc.py">whoami</a>() -> <a href="./src/patronus_api/types/who_am_i_response.py">WhoAmIResponse</a></code>

# Apps

Types:

```python
from patronus_api.types import AppResponse
```

Methods:

- <code title="get /v1/apps">client.apps.<a href="./src/patronus_api/resources/apps.py">list</a>(\*\*<a href="src/patronus_api/types/app_list_params.py">params</a>) -> <a href="./src/patronus_api/types/app_response.py">AppResponse</a></code>

# EvaluatorFamilies

Types:

```python
from patronus_api.types import ListEvaluatorFamilyResponse
```

Methods:

- <code title="get /v1/evaluator-families">client.evaluator_families.<a href="./src/patronus_api/resources/evaluator_families.py">list</a>() -> <a href="./src/patronus_api/types/list_evaluator_family_response.py">ListEvaluatorFamilyResponse</a></code>

# Annotations

Types:

```python
from patronus_api.types import AnnotateResponse
```

Methods:

- <code title="post /v1/annotate">client.annotations.<a href="./src/patronus_api/resources/annotations.py">annotate</a>(\*\*<a href="src/patronus_api/types/annotation_annotate_params.py">params</a>) -> <a href="./src/patronus_api/types/annotate_response.py">AnnotateResponse</a></code>

# AnnotationCriteria

Types:

```python
from patronus_api.types import (
    CreateAnnotationCriteriaResponse,
    GetAnnotationCriteriaResponse,
    ListAnnotationCriteriaResponse,
    UpdateAnnotationCriteriaResponse,
)
```

Methods:

- <code title="post /v1/annotation-criteria">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">create</a>(\*\*<a href="src/patronus_api/types/annotation_criterion_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_annotation_criteria_response.py">CreateAnnotationCriteriaResponse</a></code>
- <code title="get /v1/annotation-criteria/{id}">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">retrieve</a>(id) -> <a href="./src/patronus_api/types/get_annotation_criteria_response.py">GetAnnotationCriteriaResponse</a></code>
- <code title="put /v1/annotation-criteria/{id}">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">update</a>(id, \*\*<a href="src/patronus_api/types/annotation_criterion_update_params.py">params</a>) -> <a href="./src/patronus_api/types/update_annotation_criteria_response.py">UpdateAnnotationCriteriaResponse</a></code>
- <code title="get /v1/annotation-criteria">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">list</a>(\*\*<a href="src/patronus_api/types/annotation_criterion_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_annotation_criteria_response.py">ListAnnotationCriteriaResponse</a></code>
- <code title="delete /v1/annotation-criteria/{id}">client.annotation_criteria.<a href="./src/patronus_api/resources/annotation_criteria.py">delete</a>(id) -> None</code>

# PairwiseAnnotations

Types:

```python
from patronus_api.types import (
    CreatePairwiseAnnotationResponse,
    GetBatchPairwiseAnnotationsResponse,
    ListPairwiseAnnotationsResponse,
)
```

Methods:

- <code title="post /v1/pairwise-annotations">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">create</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_create_params.py">params</a>) -> <a href="./src/patronus_api/types/create_pairwise_annotation_response.py">CreatePairwiseAnnotationResponse</a></code>
- <code title="get /v1/pairwise-annotations">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">list</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_list_params.py">params</a>) -> <a href="./src/patronus_api/types/list_pairwise_annotations_response.py">ListPairwiseAnnotationsResponse</a></code>
- <code title="delete /v1/pairwise-annotations">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">delete</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_delete_params.py">params</a>) -> None</code>
- <code title="post /v1/pairwise-annotations/get-batch">client.pairwise_annotations.<a href="./src/patronus_api/resources/pairwise_annotations.py">get_batch</a>(\*\*<a href="src/patronus_api/types/pairwise_annotation_get_batch_params.py">params</a>) -> <a href="./src/patronus_api/types/get_batch_pairwise_annotations_response.py">GetBatchPairwiseAnnotationsResponse</a></code>

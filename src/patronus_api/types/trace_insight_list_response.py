# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "TraceInsightListResponse",
    "TraceInsight",
    "TraceInsightInsight",
    "TraceInsightInsightOutputAnalysis",
    "TraceInsightInsightOutputAnalysisErrorClassification",
    "TraceInsightInsightOutputAnalysisPerformanceMetrics",
    "TraceInsightInsightOutputAnalysisPerformanceMetricsAggregateScores",
]


class TraceInsightInsightOutputAnalysisErrorClassification(BaseModel):
    description: Optional[str] = None

    evidence: Optional[str] = None

    explanation: Optional[str] = None

    immediate_fix: Optional[str] = None

    impact_details: Optional[str] = None

    impact_level: Optional[Literal["LOW", "MEDIUM", "MEDIUM-HIGH", "HIGH", "UNKNOWN"]] = None

    spans: Optional[List[str]] = None

    suggested_prompt_fix: Optional[str] = None

    type: str


class TraceInsightInsightOutputAnalysisPerformanceMetricsAggregateScores(BaseModel):
    instruction_adherence_score: Optional[str] = None

    overall_score: Optional[str] = None

    plan_optimality_score: Optional[str] = None

    reliability_score: Optional[str] = None

    security_score: Optional[str] = None


class TraceInsightInsightOutputAnalysisPerformanceMetrics(BaseModel):
    aggregate_scores: Optional[TraceInsightInsightOutputAnalysisPerformanceMetricsAggregateScores] = None


class TraceInsightInsightOutputAnalysis(BaseModel):
    error_classification: List[TraceInsightInsightOutputAnalysisErrorClassification]

    overall_evaluation_analysis: str

    performance_metrics: TraceInsightInsightOutputAnalysisPerformanceMetrics

    span_error_rate: str


class TraceInsightInsight(BaseModel):
    input_analysis: str

    output_analysis: TraceInsightInsightOutputAnalysis


class TraceInsight(BaseModel):
    account_id: str

    error_message: Optional[str] = None

    insights: List[TraceInsightInsight]

    job_id: str

    processing_status: str

    trace_id: str


class TraceInsightListResponse(BaseModel):
    trace_insights: List[TraceInsight]

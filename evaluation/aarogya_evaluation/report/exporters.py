"""Export EvaluationReport to JSON, CSV, Markdown, console."""

from __future__ import annotations

import csv
import json
from io import StringIO
from pathlib import Path

from aarogya_core.types.evaluation import EvaluationReport
from aarogya_evaluation.report.serializers import report_to_dict
from aarogya_evaluation.report.templates import MARKDOWN_TEMPLATE


def export_json(report: EvaluationReport, path: Path | None = None) -> str:
    text = json.dumps(report_to_dict(report), indent=2, default=str)
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return text


def export_csv(report: EvaluationReport, path: Path | None = None) -> str:
    buf = StringIO()
    writer = csv.writer(buf)
    writer.writerow(["sample_id", "metric", "value", "normalization", "implemented"])
    for sample in report.samples:
        for result in sample.results:
            writer.writerow(
                [
                    sample.sample_id,
                    result.name,
                    result.value if result.value is not None else "",
                    result.normalization or "",
                    result.implemented,
                ]
            )
    text = buf.getvalue()
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return text


def export_markdown(report: EvaluationReport, path: Path | None = None) -> str:
    summary_lines = [
        f"| {k} | {v:.6f} |" if isinstance(v, float) else f"| {k} | {v} |"
        for k, v in sorted(report.summary.metrics.items())
    ]
    summary_table = "| Metric | Value |\n|--------|-------|\n" + "\n".join(
        summary_lines
    )
    timing_table = (
        "\n".join(f"- {k}: {v:.4f}s" for k, v in report.timing.items()) or "- n/a"
    )
    fail_counts: dict[str, int] = {}
    for case in report.failures:
        fail_counts[case.category] = fail_counts.get(case.category, 0) + 1
    failure_summary = (
        "\n".join(f"- {k}: {v}" for k, v in sorted(fail_counts.items())) or "- none"
    )
    text = MARKDOWN_TEMPLATE.format(
        report_id=report.report_id,
        created_at=report.created_at.isoformat() if report.created_at else "",
        dataset_id=report.dataset_id or "",
        dataset_version=report.dataset_version or "",
        pipeline_id=report.pipeline_id or "",
        experiment_id=report.experiment_id or "",
        primary_metric=report.summary.primary_metric,
        summary_table=summary_table,
        timing_table=timing_table,
        failure_count=len(report.failures),
        failure_summary=failure_summary,
        config_json=json.dumps(report.config.model_dump(mode="json"), indent=2),
    )
    if path is not None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    return text


def export_console(report: EvaluationReport) -> str:
    lines = [
        f"Report {report.report_id}",
        f"Samples: {report.summary.sample_count}",
        f"Duration: {report.summary.duration_seconds:.4f}s",
        "Metrics:",
    ]
    for name, value in sorted(report.summary.metrics.items()):
        lines.append(f"  {name}: {value:.6f}")
    lines.append(f"Failures: {len(report.failures)}")
    text = "\n".join(lines)
    print(text)
    return text


def export_report(
    report: EvaluationReport,
    directory: Path,
    *,
    formats: list[str] | None = None,
) -> dict[str, Path]:
    formats = formats or ["json", "csv", "markdown"]
    directory.mkdir(parents=True, exist_ok=True)
    written: dict[str, Path] = {}
    if "json" in formats:
        p = directory / f"{report.report_id}.json"
        export_json(report, p)
        written["json"] = p
    if "csv" in formats:
        p = directory / f"{report.report_id}.csv"
        export_csv(report, p)
        written["csv"] = p
    if "markdown" in formats or "md" in formats:
        p = directory / f"{report.report_id}.md"
        export_markdown(report, p)
        written["markdown"] = p
    if "console" in formats:
        export_console(report)
    return written

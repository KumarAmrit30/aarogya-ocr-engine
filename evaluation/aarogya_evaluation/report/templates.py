"""Markdown report template."""

MARKDOWN_TEMPLATE = """# Evaluation Report: {report_id}

- Created: {created_at}
- Dataset: {dataset_id}@{dataset_version}
- Pipeline: {pipeline_id}
- Experiment: {experiment_id}
- Primary metric: {primary_metric}

## Summary

{summary_table}

## Timing

{timing_table}

## Failures ({failure_count})

{failure_summary}

## Configuration

```json
{config_json}
```
"""

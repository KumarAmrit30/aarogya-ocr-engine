"""Build leaderboard rows from benchmark runs."""

from __future__ import annotations

from aarogya_core.types.evaluation import BenchmarkRun


def build_leaderboard(
    runs: list[BenchmarkRun],
    *,
    primary_metric: str = "cer",
    lower_is_better: bool = True,
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for run in runs:
        metrics = run.summary.metrics if run.summary else {}
        rows.append(
            {
                "run_id": run.run_id,
                "pipeline_id": run.pipeline_id,
                "dataset": f"{run.dataset_id}@{run.dataset_version}",
                "primary_metric": primary_metric,
                "primary_value": metrics.get(primary_metric),
                **metrics,
                "status": run.status,
            }
        )

    def sort_key(row: dict[str, object]) -> tuple[int, float]:
        val = row.get("primary_value")
        if val is None or not isinstance(val, (int, float)):
            return (1, 0.0)
        return (0, float(val) if lower_is_better else -float(val))

    rows.sort(key=sort_key)
    for i, row in enumerate(rows, start=1):
        row["rank"] = i
    return rows

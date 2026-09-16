"use client";

import { useMutation, useQuery } from "@tanstack/react-query";

import { Button, EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

function MetricBars({ metrics }: { metrics: Record<string, number> }) {
  const entries = Object.entries(metrics);
  if (entries.length === 0) return null;
  const max = Math.max(...entries.map(([, v]) => Math.abs(v)), 1);
  return (
    <div className="mt-4 space-y-2">
      {entries.map(([name, value]) => (
        <div key={name} className="text-sm">
          <div className="mb-0.5 flex justify-between font-mono">
            <span>{name}</span>
            <span>{value.toFixed(4)}</span>
          </div>
          <div className="h-2 w-full bg-surface">
            <div
              className="h-2 bg-accent"
              style={{ width: `${Math.min(100, (Math.abs(value) / max) * 100)}%` }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}

export default function EvaluationPage() {
  const reports = useQuery({
    queryKey: ["evaluation-reports"],
    queryFn: apiClient.evaluationReports,
  });

  const demo = useMutation({
    mutationFn: () =>
      apiClient.evaluate({
        references: [{ sample_id: "demo-1", text: "aspirin 75 mg" }],
        predictions: [{ sample_id: "demo-1", text: "aspirin 75 mg" }],
        config: {
          metrics: ["cer", "wer", "exact_match"],
          primary_metric: "cer",
        },
      }),
  });

  return (
    <div>
      <PageHeader
        title="Evaluation"
        description="Model-agnostic metrics engine. Submit GT/prediction pairs — no OCR."
      />
      <Panel className="mb-4">
        <Button type="button" onClick={() => demo.mutate()} disabled={demo.isPending}>
          {demo.isPending ? "Running…" : "Run demo evaluation (identical strings)"}
        </Button>
        {demo.data ? (
          <div className="mt-4">
            <div className="text-sm text-ink-muted">Report {demo.data.report_id}</div>
            <MetricBars metrics={demo.data.summary.metrics} />
          </div>
        ) : null}
        {demo.error ? (
          <p className="mt-3 text-sm text-red-700">{(demo.error as Error).message}</p>
        ) : null}
      </Panel>
      <Panel>
        <EmptyTable
          columns={["report_id", "path"]}
          message={
            reports.data?.reports.length
              ? `${reports.data.reports.length} report(s) on disk`
              : "No saved reports yet (evaluation/reports)."
          }
        />
        {reports.data?.reports.length ? (
          <ul className="mt-2 text-sm font-mono space-y-1">
            {reports.data.reports.map((r) => (
              <li key={r.report_id}>
                {r.report_id} — {r.path}
              </li>
            ))}
          </ul>
        ) : null}
      </Panel>
    </div>
  );
}

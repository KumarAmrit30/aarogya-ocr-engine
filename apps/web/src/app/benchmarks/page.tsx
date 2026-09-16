"use client";

import { useQuery } from "@tanstack/react-query";

import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

export default function BenchmarksPage() {
  const suites = useQuery({ queryKey: ["benchmarks"], queryFn: apiClient.benchmarks });

  return (
    <div>
      <PageHeader
        title="Benchmarks"
        description="Comparative suites keyed by PIPELINE-##### × DATASET-#####@vN."
      />
      <Panel>
        <EmptyTable
          columns={["suite", "status"]}
          message={
            suites.isLoading
              ? "Loading…"
              : suites.data?.suites.length
                ? ""
                : "No benchmark suites found."
          }
        />
        {suites.data?.suites.length ? (
          <table className="w-full text-left text-sm mt-2">
            <thead>
              <tr className="border-b border-surface-border text-ink-muted">
                <th className="py-2 pr-4">suite</th>
                <th className="py-2">status</th>
              </tr>
            </thead>
            <tbody>
              {suites.data.suites.map((s) => (
                <tr key={s.suite} className="border-b border-surface-border">
                  <td className="py-2 pr-4 font-mono">{s.suite}</td>
                  <td className="py-2">{s.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : null}
      </Panel>
    </div>
  );
}

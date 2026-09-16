"use client";

import { useQuery } from "@tanstack/react-query";
import Link from "next/link";

import { PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

export default function DashboardPage() {
  const health = useQuery({ queryKey: ["health"], queryFn: apiClient.health });
  const version = useQuery({ queryKey: ["version"], queryFn: apiClient.version });

  return (
    <div>
      <PageHeader
        title="Dashboard"
        description="Internal research console for the Aarogya AI Research Platform."
      />
      <div className="grid gap-4 sm:grid-cols-2">
        <Panel>
          <div className="text-xs uppercase text-ink-muted">API health</div>
          <div className="mt-2 font-mono text-sm">
            {health.isLoading && "Loading…"}
            {health.isError && "Unreachable — start inference-api"}
            {health.data && (
              <span>
                {health.data.status} · {health.data.service}
              </span>
            )}
          </div>
        </Panel>
        <Panel>
          <div className="text-xs uppercase text-ink-muted">Version</div>
          <div className="mt-2 font-mono text-sm">
            {version.data
              ? `${version.data.version} (schema ${version.data.api_schema_version})`
              : "—"}
          </div>
        </Panel>
      </div>
      <Panel className="mt-4">
        <div className="text-sm font-medium mb-2">Quick links</div>
        <ul className="list-disc pl-5 text-sm space-y-1">
          <li>
            <Link className="underline" href="/playground">
              Playground
            </Link>{" "}
            — exercise OCR placeholder
          </li>
          <li>
            <Link className="underline" href="/registry">
              Registry
            </Link>{" "}
            — EXP / DATASET / MODEL IDs
          </li>
          <li>
            <Link className="underline" href="/benchmarks">
              Benchmarks
            </Link>{" "}
            — comparative suites
          </li>
        </ul>
      </Panel>
    </div>
  );
}

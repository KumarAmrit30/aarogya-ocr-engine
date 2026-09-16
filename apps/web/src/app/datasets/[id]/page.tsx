"use client";

import Link from "next/link";
import { useQuery } from "@tanstack/react-query";
import { use } from "react";

import { PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

export default function DatasetDetailPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = use(params);
  const dataset = useQuery({
    queryKey: ["dataset", id],
    queryFn: () => apiClient.dataset(id),
  });

  const latest = dataset.data?.versions?.[dataset.data.versions.length - 1];
  const versionKey = latest?.version_id || latest?.version;

  const detail = useQuery({
    queryKey: ["dataset-version", id, versionKey],
    queryFn: () => apiClient.datasetVersion(id, versionKey!),
    enabled: Boolean(versionKey),
  });

  return (
    <div>
      <PageHeader
        title={dataset.data?.name || id}
        description="Version detail: fingerprint, PII, lineage, validation, quality, card."
      />
      <p className="mb-4 text-sm">
        <Link className="underline text-ink-muted" href="/datasets">
          ← Dataset Explorer
        </Link>
      </p>
      {dataset.error ? (
        <Panel>
          <p className="text-sm text-red-700">{(dataset.error as Error).message}</p>
        </Panel>
      ) : null}
      <Panel className="mb-4 space-y-2 text-sm font-mono">
        <div>dataset_id: {dataset.data?.dataset_id}</div>
        <div>task: {dataset.data?.task || "—"}</div>
        <div>domain: {dataset.data?.domain || "—"}</div>
        <div>license: {dataset.data?.license || "—"}</div>
        <div>language: {(dataset.data?.language || []).join(", ") || "—"}</div>
        <div>tags: {(dataset.data?.tags || []).join(", ") || "—"}</div>
        <div>
          versions:{" "}
          {(dataset.data?.versions || [])
            .map((v) => `${v.version}${v.version_id ? ` (${v.version_id})` : ""}`)
            .join(", ") || "—"}
        </div>
      </Panel>
      {detail.data ? (
        <>
          <Panel className="mb-4 space-y-2 text-sm font-mono">
            <div>version: {detail.data.version.version}</div>
            <div>version_id: {detail.data.version.version_id || "—"}</div>
            <div>fingerprint: {detail.data.fingerprint || "—"}</div>
            <div>status: {detail.data.version.status}</div>
            <div>sample_count: {detail.data.version.sample_count ?? "—"}</div>
            <div>
              validation:{" "}
              {detail.data.validation
                ? String((detail.data.validation as { passed?: boolean }).passed)
                : "—"}
            </div>
            <div>
              quality_score:{" "}
              {detail.data.quality &&
              typeof (detail.data.quality as { overall_score?: number }).overall_score === "number"
                ? (detail.data.quality as { overall_score: number }).overall_score.toFixed(3)
                : "—"}
            </div>
            <div>
              lineage_nodes:{" "}
              {detail.data.lineage && Array.isArray((detail.data.lineage as { nodes?: string[] }).nodes)
                ? (detail.data.lineage as { nodes: string[] }).nodes.join(" → ")
                : "—"}
            </div>
          </Panel>
          {detail.data.card_markdown ? (
            <Panel>
              <pre className="whitespace-pre-wrap text-sm">{detail.data.card_markdown}</pre>
            </Panel>
          ) : null}
        </>
      ) : null}
    </div>
  );
}

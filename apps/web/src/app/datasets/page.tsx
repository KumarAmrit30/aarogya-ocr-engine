"use client";

import Link from "next/link";
import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { useMemo, useState } from "react";

import { Button, EmptyTable, Input, PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

export default function DatasetsPage() {
  const queryClient = useQueryClient();
  const [language, setLanguage] = useState("");
  const [license, setLicense] = useState("");
  const [task, setTask] = useState("");
  const [domain, setDomain] = useState("");
  const [minQuality, setMinQuality] = useState("");
  const [tags, setTags] = useState("");
  const [nameContains, setNameContains] = useState("");

  const filters = useMemo(
    () => ({
      language: language || undefined,
      license: license || undefined,
      task: task || undefined,
      domain: domain || undefined,
      min_quality: minQuality ? Number(minQuality) : undefined,
      tags: tags
        ? tags
            .split(",")
            .map((t) => t.trim())
            .filter(Boolean)
        : [],
      name_contains: nameContains || undefined,
    }),
    [language, license, task, domain, minQuality, tags, nameContains],
  );

  const list = useQuery({
    queryKey: ["datasets", filters],
    queryFn: () => apiClient.datasets(filters),
  });

  const publish = useMutation({
    mutationFn: () =>
      apiClient.runDatasetPipeline({
        name: "synthetic-demo",
        dataset_id: "DATASET-00001",
        version: "v1",
        task: "HTR",
        domain: "medical",
        language: ["en"],
        license: "research-only",
        tags: ["synthetic", "demo"],
      }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["datasets"] }),
  });

  const rows = list.data?.datasets ?? [];

  return (
    <div>
      <PageHeader
        title="Dataset Explorer"
        description="Catalog search over datasets/registry.yaml — language, license, task, domain, quality, tags."
      />
      <Panel className="mb-4 space-y-3">
        <div className="grid gap-2 sm:grid-cols-2 lg:grid-cols-3">
          <label className="text-xs text-ink-muted">
            language
            <Input className="mt-1" value={language} onChange={(e) => setLanguage(e.target.value)} />
          </label>
          <label className="text-xs text-ink-muted">
            license
            <Input className="mt-1" value={license} onChange={(e) => setLicense(e.target.value)} />
          </label>
          <label className="text-xs text-ink-muted">
            task
            <Input className="mt-1" value={task} onChange={(e) => setTask(e.target.value)} />
          </label>
          <label className="text-xs text-ink-muted">
            domain
            <Input className="mt-1" value={domain} onChange={(e) => setDomain(e.target.value)} />
          </label>
          <label className="text-xs text-ink-muted">
            min_quality
            <Input
              className="mt-1"
              value={minQuality}
              onChange={(e) => setMinQuality(e.target.value)}
              placeholder="0–1"
            />
          </label>
          <label className="text-xs text-ink-muted">
            tags (comma)
            <Input className="mt-1" value={tags} onChange={(e) => setTags(e.target.value)} />
          </label>
          <label className="text-xs text-ink-muted sm:col-span-2">
            name_contains
            <Input
              className="mt-1"
              value={nameContains}
              onChange={(e) => setNameContains(e.target.value)}
            />
          </label>
        </div>
        <Button type="button" onClick={() => publish.mutate()} disabled={publish.isPending}>
          {publish.isPending ? "Publishing…" : "Run synthetic pipeline (demo)"}
        </Button>
        {publish.data ? (
          <p className="text-sm font-mono text-ink-muted">
            Published {publish.data.dataset_id} / {publish.data.version_id} fp=
            {publish.data.fingerprint?.slice(0, 12)}…
          </p>
        ) : null}
        {publish.error ? (
          <p className="text-sm text-red-700">{(publish.error as Error).message}</p>
        ) : null}
      </Panel>
      <Panel>
        {rows.length === 0 ? (
          <EmptyTable
            columns={["dataset_id", "name", "task", "domain", "quality_score", "versions"]}
            message={list.isLoading ? "Loading…" : "No datasets match filters."}
          />
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead>
                <tr className="border-b border-surface-border text-ink-muted">
                  {["dataset_id", "name", "task", "domain", "quality_score", "versions"].map(
                    (col) => (
                      <th key={col} className="py-2 pr-4 font-medium">
                        {col}
                      </th>
                    ),
                  )}
                </tr>
              </thead>
              <tbody>
                {rows.map((d) => (
                  <tr key={d.dataset_id} className="border-b border-surface-border/60">
                    <td className="py-2 pr-4 font-mono">
                      <Link className="underline" href={`/datasets/${d.dataset_id}`}>
                        {d.dataset_id}
                      </Link>
                    </td>
                    <td className="py-2 pr-4">{d.name}</td>
                    <td className="py-2 pr-4">{d.task || "—"}</td>
                    <td className="py-2 pr-4">{d.domain || "—"}</td>
                    <td className="py-2 pr-4 font-mono">
                      {d.quality_score != null ? d.quality_score.toFixed(3) : "—"}
                    </td>
                    <td className="py-2 pr-4 font-mono">{d.versions.length}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </Panel>
    </div>
  );
}

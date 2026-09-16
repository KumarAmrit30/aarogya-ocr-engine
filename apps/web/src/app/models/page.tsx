"use client";

import { useQuery } from "@tanstack/react-query";

import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

export default function ModelsPage() {
  const models = useQuery({ queryKey: ["models"], queryFn: apiClient.models });

  return (
    <div>
      <PageHeader title="Models" description="Registered models (MODEL-#####). Empty until registry is populated." />
      <Panel>
        <EmptyTable
          columns={["model_id", "name", "engine_id", "role"]}
          message={
            models.data?.message ||
            (models.data?.models.length === 0 ? "No models registered." : "Loading…")
          }
        />
      </Panel>
    </div>
  );
}

import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function RegistryPage() {
  return (
    <div>
      <PageHeader
        title="Registry"
        description="Stable IDs for experiments, datasets, models, assets, and pipelines."
      />
      <div className="grid gap-4">
        <Panel>
          <h2 className="mb-2 text-sm font-medium">ID scheme</h2>
          <ul className="text-sm text-ink-muted space-y-1 font-mono">
            <li>EXP-##### — immutable experiment dirs</li>
            <li>DATASET-#####@vN — versioned datasets</li>
            <li>MODEL-##### — logical models</li>
            <li>ASSET-##### — checkpoints, tokenizers, exports…</li>
            <li>PIPELINE-##### — composed adapters (benchmark unit)</li>
          </ul>
        </Panel>
        <Panel>
          <EmptyTable
            columns={["id", "type", "name", "updated"]}
            message="Registry index empty — allocate IDs via aarogya_core.registry.next_id."
          />
        </Panel>
      </div>
    </div>
  );
}

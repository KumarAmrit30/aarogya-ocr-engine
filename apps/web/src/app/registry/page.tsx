import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function RegistryPage() {
  return (
    <div>
      <PageHeader
        title="Registry"
        description="Stable IDs: EXP-##### · DATASET-##### · MODEL-#####"
      />
      <div className="grid gap-4">
        <Panel>
          <h2 className="mb-2 text-sm font-medium">ID scheme</h2>
          <ul className="text-sm text-ink-muted space-y-1">
            <li>Experiments → registry/experiments/EXP-00001.yaml</li>
            <li>Datasets catalog → datasets/registry.yaml</li>
            <li>Models → registry/models/MODEL-00001.yaml</li>
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

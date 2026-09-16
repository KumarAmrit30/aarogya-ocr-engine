import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function ExperimentsPage() {
  return (
    <div>
      <PageHeader
        title="Experiments"
        description="Immutable EXP-##### records under registry/experiments/. Never overwrite — allocate a new ID to rerun."
      />
      <Panel className="mb-4 text-sm text-ink-muted">
        Layout: <code>EXP-#####.yaml</code>, <code>config/</code>, <code>results/</code>,{" "}
        <code>report/</code>, <code>artifacts/</code>. See ADR-0004.
      </Panel>
      <Panel>
        <EmptyTable
          columns={["experiment_id", "name", "status", "pipeline_id", "dataset_version"]}
          message="No experiments registered yet."
        />
      </Panel>
    </div>
  );
}

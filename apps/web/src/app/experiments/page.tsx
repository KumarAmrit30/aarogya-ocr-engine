import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function ExperimentsPage() {
  return (
    <div>
      <PageHeader
        title="Experiments"
        description="Experiment history from registry/experiments (EXP-#####)."
      />
      <Panel>
        <EmptyTable
          columns={["experiment_id", "name", "status", "engine_id"]}
          message="No experiments registered yet."
        />
      </Panel>
    </div>
  );
}

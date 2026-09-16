import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function EvaluationPage() {
  return (
    <div>
      <PageHeader
        title="Evaluation"
        description="Single-run metrics. Comparative work lives under Benchmarks."
      />
      <Panel>
        <EmptyTable
          columns={["run", "dataset_id", "model_id", "metric", "value"]}
          message="No evaluation runs yet."
        />
      </Panel>
    </div>
  );
}

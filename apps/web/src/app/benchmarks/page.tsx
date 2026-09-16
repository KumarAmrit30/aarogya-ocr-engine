import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function BenchmarksPage() {
  return (
    <div>
      <PageHeader
        title="Benchmarks"
        description="Comparative suites: handwritten, printed, mixed, robustness, latency."
      />
      <Panel>
        <EmptyTable
          columns={["suite", "engines", "dataset_ids", "status"]}
          message="No benchmark suites configured yet. See benchmarks/ and configs/benchmarks/."
        />
      </Panel>
    </div>
  );
}

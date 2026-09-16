import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function DatasetsPage() {
  return (
    <div>
      <PageHeader
        title="Datasets"
        description="Catalog from datasets/registry.yaml (DATASET-#####)."
      />
      <Panel>
        <EmptyTable
          columns={["dataset_id", "name", "language", "quality", "license"]}
          message="No datasets in registry.yaml yet."
        />
      </Panel>
    </div>
  );
}

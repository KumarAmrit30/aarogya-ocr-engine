import { EmptyTable, PageHeader, Panel } from "@/components/ui/primitives";

export default function ErrorsPage() {
  return (
    <div>
      <PageHeader
        title="Errors"
        description="Error analysis placeholder for OCR failure modes."
      />
      <Panel>
        <EmptyTable
          columns={["error_id", "type", "engine_id", "count", "example"]}
          message="No error analysis data yet."
        />
      </Panel>
    </div>
  );
}

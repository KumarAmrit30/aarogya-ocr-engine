"use client";

import { useState } from "react";

import { Button, Input, PageHeader, Panel } from "@/components/ui/primitives";

export default function UploadPage() {
  const [fileName, setFileName] = useState<string | null>(null);

  return (
    <div>
      <PageHeader
        title="Upload"
        description="Single image upload for research. OCR is not implemented yet."
      />
      <Panel>
        <Input
          type="file"
          accept="image/*"
          onChange={(e) => setFileName(e.target.files?.[0]?.name ?? null)}
        />
        <p className="mt-3 text-sm text-ink-muted">
          {fileName ? `Selected: ${fileName}` : "No file selected."}
        </p>
        <Button className="mt-4" type="button" disabled>
          Run OCR (not implemented)
        </Button>
      </Panel>
    </div>
  );
}

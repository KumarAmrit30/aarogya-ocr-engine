"use client";

import { useState } from "react";

import { Button, Input, PageHeader, Panel } from "@/components/ui/primitives";
import { useSettingsStore } from "@/stores/settings";

export default function SettingsPage() {
  const { apiBaseUrl, setApiBaseUrl } = useSettingsStore();
  const [value, setValue] = useState(apiBaseUrl);

  return (
    <div>
      <PageHeader title="Settings" description="Developer settings for the research console." />
      <Panel>
        <label className="block text-sm">
          API base URL
          <Input className="mt-1" value={value} onChange={(e) => setValue(e.target.value)} />
        </label>
        <Button
          className="mt-3"
          type="button"
          onClick={() => setApiBaseUrl(value.replace(/\/$/, ""))}
        >
          Save
        </Button>
      </Panel>
    </div>
  );
}

"use client";

import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";

import { Button, Input, PageHeader, Panel } from "@/components/ui/primitives";
import { apiClient } from "@/lib/api-client";

type FormValues = {
  engine_id: string;
  image_path: string;
};

export default function PlaygroundPage() {
  const { register, handleSubmit } = useForm<FormValues>({
    defaultValues: { engine_id: "stub", image_path: "" },
  });

  const mutation = useMutation({
    mutationFn: apiClient.ocr,
  });

  return (
    <div>
      <PageHeader
        title="Playground"
        description="Manually POST /api/v1/ocr. Expects status=not_implemented until engines are wired."
      />
      <Panel>
        <form
          className="space-y-3"
          onSubmit={handleSubmit((values) =>
            mutation.mutate({
              engine_id: values.engine_id || "stub",
              image_path: values.image_path || null,
              metadata: {},
            }),
          )}
        >
          <label className="block text-sm">
            Engine ID
            <Input className="mt-1" {...register("engine_id")} />
          </label>
          <label className="block text-sm">
            Image path (optional)
            <Input className="mt-1" {...register("image_path")} placeholder="datasets/raw/…" />
          </label>
          <Button type="submit" disabled={mutation.isPending}>
            {mutation.isPending ? "Running…" : "Run OCR"}
          </Button>
        </form>
        {mutation.data ? (
          <pre className="mt-4 overflow-auto rounded bg-zinc-950 p-3 text-xs text-zinc-100">
            {JSON.stringify(mutation.data, null, 2)}
          </pre>
        ) : null}
        {mutation.error ? (
          <p className="mt-3 text-sm text-red-700">{(mutation.error as Error).message}</p>
        ) : null}
      </Panel>
    </div>
  );
}

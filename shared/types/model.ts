import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";
import { experimentIdSchema, modelIdSchema } from "./experiment";

export const modelRecordSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).default(SCHEMA_VERSION),
  model_id: modelIdSchema,
  name: z.string(),
  engine_id: z.string(),
  role: z
    .enum(["detector", "recognizer", "layout", "vlm", "pipeline", "other"])
    .default("other"),
  checkpoint_path: z.string().nullable().optional(),
  experiment_id: experimentIdSchema.nullable().optional(),
  metrics: z.record(z.number()).default({}),
});

export type ModelRecord = z.infer<typeof modelRecordSchema>;

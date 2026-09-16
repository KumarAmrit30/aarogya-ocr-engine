import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";

export const experimentIdSchema = z.string().regex(/^EXP-\d{5}$/);
export const datasetIdSchema = z.string().regex(/^DATASET-\d{5}$/);
export const modelIdSchema = z.string().regex(/^MODEL-\d{5}$/);

export const experimentSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).default(SCHEMA_VERSION),
  experiment_id: experimentIdSchema,
  name: z.string(),
  status: z.enum(["planned", "running", "completed", "failed", "abandoned"]).default("planned"),
  hypothesis: z.string().nullable().optional(),
  engine_id: z.string().nullable().optional(),
  model_id: modelIdSchema.nullable().optional(),
  dataset_ids: z.array(datasetIdSchema).default([]),
  metrics: z.record(z.number()).default({}),
  artifact_path: z.string().nullable().optional(),
  notes_path: z.string().nullable().optional(),
});

export type Experiment = z.infer<typeof experimentSchema>;
export type ExperimentId = z.infer<typeof experimentIdSchema>;
export type DatasetId = z.infer<typeof datasetIdSchema>;
export type ModelId = z.infer<typeof modelIdSchema>;

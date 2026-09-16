import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";
import { datasetIdSchema } from "./experiment";

export const datasetRecordSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).default(SCHEMA_VERSION),
  dataset_id: datasetIdSchema,
  name: z.string(),
  version: z.string().default("0.1.0"),
  license: z.string().nullable().optional(),
  language: z.array(z.string()).default([]),
  writer_count: z.number().int().nullable().optional(),
  source: z.string().nullable().optional(),
  quality: z.enum(["unknown", "low", "medium", "high"]).default("unknown"),
  path: z.string().nullable().optional(),
  card: z.string().nullable().optional(),
});

export type DatasetRecord = z.infer<typeof datasetRecordSchema>;

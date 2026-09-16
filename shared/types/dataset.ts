import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";
import { datasetIdSchema } from "./experiment";

export const datasetVersionSchema = z.object({
  version: z.string(),
  path: z.string().nullable().optional(),
  card: z.string().nullable().optional(),
  split: z.record(z.union([z.number(), z.string()])).nullable().optional(),
  parent_version: z.string().nullable().optional(),
  change_notes: z.string().nullable().optional(),
});

export const datasetRecordSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  dataset_id: datasetIdSchema,
  name: z.string(),
  license: z.string().nullable().optional(),
  language: z.array(z.string()).default([]),
  writer_count: z.number().int().nullable().optional(),
  source: z.string().nullable().optional(),
  quality: z.enum(["unknown", "low", "medium", "high"]).default("unknown"),
  versions: z.array(datasetVersionSchema).default([]),
  path: z.string().nullable().optional(),
  card: z.string().nullable().optional(),
});

export type DatasetVersion = z.infer<typeof datasetVersionSchema>;
export type DatasetRecord = z.infer<typeof datasetRecordSchema>;

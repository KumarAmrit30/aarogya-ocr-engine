import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";
import {
  assetIdSchema,
  datasetIdSchema,
  versionIdSchema,
} from "./experiment";

export const piiStatusSchema = z.enum([
  "unknown",
  "contains_phi",
  "redacted",
  "verified_safe",
]);

export const assetSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  asset_id: z.union([assetIdSchema, z.string()]),
  uri: z.string(),
  checksum: z.string().nullable().optional(),
  mime: z.string().nullable().optional(),
  size: z.number().int().nullable().optional(),
  backend: z.string().default("local"),
});

export const datasetVersionSchema = z.object({
  version_id: versionIdSchema.nullable().optional(),
  version: z.string(),
  path: z.string().nullable().optional(),
  card: z.string().nullable().optional(),
  manifest_path: z.string().nullable().optional(),
  statistics_path: z.string().nullable().optional(),
  quality_path: z.string().nullable().optional(),
  validation_path: z.string().nullable().optional(),
  lineage_path: z.string().nullable().optional(),
  fingerprint: z.string().nullable().optional(),
  split: z.record(z.union([z.number(), z.string()])).nullable().optional(),
  parent_version: z.string().nullable().optional(),
  change_notes: z.string().nullable().optional(),
  status: z.enum(["draft", "validated", "published", "deprecated"]).default("draft"),
  sample_count: z.number().int().nullable().optional(),
});

export const datasetRecordSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  dataset_id: datasetIdSchema,
  name: z.string(),
  license: z.string().nullable().optional(),
  language: z.array(z.string()).default([]),
  script: z.array(z.string()).default([]),
  writer_count: z.number().int().nullable().optional(),
  source: z.string().nullable().optional(),
  homepage: z.string().nullable().optional(),
  paper: z.string().nullable().optional(),
  task: z.string().nullable().optional(),
  domain: z.string().nullable().optional(),
  quality: z.enum(["unknown", "low", "medium", "high"]).default("unknown"),
  quality_score: z.number().nullable().optional(),
  status: z.enum(["registered", "ingesting", "ready", "deprecated"]).default("registered"),
  tags: z.array(z.string()).default([]),
  versions: z.array(datasetVersionSchema).default([]),
  path: z.string().nullable().optional(),
  card: z.string().nullable().optional(),
});

export const datasetSearchQuerySchema = z.object({
  language: z.string().nullable().optional(),
  license: z.string().nullable().optional(),
  task: z.string().nullable().optional(),
  script: z.string().nullable().optional(),
  domain: z.string().nullable().optional(),
  min_quality: z.number().nullable().optional(),
  tags: z.array(z.string()).default([]),
  pii_status: piiStatusSchema.nullable().optional(),
  name_contains: z.string().nullable().optional(),
});

export const datasetListResponseSchema = z.object({
  datasets: z.array(datasetRecordSchema),
});

export const publishedVersionResultSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  dataset_id: datasetIdSchema,
  version_id: versionIdSchema.nullable().optional(),
  version: z.string(),
  path: z.string().nullable().optional(),
  fingerprint: z.string().nullable().optional(),
  card_path: z.string().nullable().optional(),
  manifest_path: z.string().nullable().optional(),
});

export const datasetVersionDetailSchema = z.object({
  dataset: datasetRecordSchema,
  version: datasetVersionSchema,
  fingerprint: z.string().nullable().optional(),
  card_markdown: z.string().nullable().optional(),
  validation: z.record(z.unknown()).nullable().optional(),
  quality: z.record(z.unknown()).nullable().optional(),
  statistics: z.record(z.unknown()).nullable().optional(),
  lineage: z.record(z.unknown()).nullable().optional(),
});

export type DatasetVersion = z.infer<typeof datasetVersionSchema>;
export type DatasetRecord = z.infer<typeof datasetRecordSchema>;
export type DatasetSearchQuery = z.infer<typeof datasetSearchQuerySchema>;
export type DatasetListResponse = z.infer<typeof datasetListResponseSchema>;
export type PublishedVersionResult = z.infer<typeof publishedVersionResultSchema>;
export type DatasetVersionDetail = z.infer<typeof datasetVersionDetailSchema>;
export type Asset = z.infer<typeof assetSchema>;

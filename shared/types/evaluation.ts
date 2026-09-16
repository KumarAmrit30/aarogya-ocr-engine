import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";
import { datasetIdSchema, experimentIdSchema, pipelineIdSchema } from "./experiment";

export const groundTruthSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  sample_id: z.string(),
  text: z.string().default(""),
  lines: z.array(z.string()).default([]),
  words: z.array(z.string()).default([]),
  metadata: z.record(z.unknown()).optional().default({}),
});

export const predictionSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  sample_id: z.string(),
  text: z.string().default(""),
  lines: z.array(z.string()).default([]),
  words: z.array(z.string()).default([]),
  pipeline_id: pipelineIdSchema.nullable().optional(),
  engine_id: z.string().nullable().optional(),
  metadata: z.record(z.unknown()).optional().default({}),
});

export const evaluationSummarySchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  metrics: z.record(z.number()).default({}),
  sample_count: z.number().default(0),
  duration_seconds: z.number().default(0),
  primary_metric: z.string().default("cer"),
});

export const evaluationReportSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  report_id: z.string(),
  created_at: z.string().nullable().optional(),
  dataset_id: datasetIdSchema.nullable().optional(),
  dataset_version: z.string().nullable().optional(),
  pipeline_id: pipelineIdSchema.nullable().optional(),
  experiment_id: experimentIdSchema.nullable().optional(),
  summary: evaluationSummarySchema,
  failures: z.array(z.record(z.unknown())).default([]),
  timing: z.record(z.number()).default({}),
});

export type GroundTruth = z.input<typeof groundTruthSchema>;
export type Prediction = z.input<typeof predictionSchema>;
export type EvaluationSummary = z.infer<typeof evaluationSummarySchema>;
export type EvaluationReport = z.infer<typeof evaluationReportSchema>;

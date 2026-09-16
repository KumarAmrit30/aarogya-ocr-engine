import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";
import { boundingBoxSchema } from "./common";

export const pipelineStatusSchema = z.enum(["ok", "not_implemented", "error"]);

export const ocrWordSchema = z.object({
  text: z.string(),
  bbox: boundingBoxSchema.nullable().optional(),
  confidence: z.number().min(0).max(1).nullable().optional(),
});

export const ocrLineSchema = z.object({
  text: z.string(),
  words: z.array(ocrWordSchema).default([]),
  bbox: boundingBoxSchema.nullable().optional(),
  confidence: z.number().min(0).max(1).nullable().optional(),
});

export const ocrRequestSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  image_path: z.string().nullable().optional(),
  image_base64: z.string().nullable().optional(),
  engine_id: z.string().nullable().optional(),
  config_ref: z.string().nullable().optional(),
  metadata: z.record(z.unknown()).optional().default({}),
});

export const ocrResultSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).optional().default(SCHEMA_VERSION),
  status: pipelineStatusSchema,
  message: z.string().nullable().optional(),
  full_text: z.string().optional().default(""),
  lines: z.array(ocrLineSchema).optional().default([]),
  engine_id: z.string().nullable().optional(),
  config_hash: z.string().nullable().optional(),
  metadata: z.record(z.unknown()).optional().default({}),
});

export type OCRWord = z.infer<typeof ocrWordSchema>;
export type OCRLine = z.infer<typeof ocrLineSchema>;
export type OCRRequest = z.input<typeof ocrRequestSchema>;
export type OCRResult = z.infer<typeof ocrResultSchema>;
export type PipelineStatus = z.infer<typeof pipelineStatusSchema>;

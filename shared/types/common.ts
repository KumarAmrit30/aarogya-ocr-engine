import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";

export const schemaVersionSchema = z.literal(SCHEMA_VERSION);

export const boundingBoxSchema = z.object({
  x1: z.number(),
  y1: z.number(),
  x2: z.number(),
  y2: z.number(),
  confidence: z.number().min(0).max(1).nullable().optional(),
});

export type BoundingBox = z.infer<typeof boundingBoxSchema>;

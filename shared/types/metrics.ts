import { z } from "zod";

import { SCHEMA_VERSION } from "../constants/api";

export const metricsSchema = z.object({
  schema_version: z.literal(SCHEMA_VERSION).default(SCHEMA_VERSION),
  name: z.string(),
  values: z.record(z.number()).default({}),
  extras: z.record(z.unknown()).default({}),
});

export type Metrics = z.infer<typeof metricsSchema>;

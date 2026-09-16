import { z } from "zod";

export const healthResponseSchema = z.object({
  status: z.string(),
  service: z.string(),
  time: z.string(),
});

export const versionResponseSchema = z.object({
  version: z.string(),
  api_schema_version: z.string(),
  git_sha: z.string().nullable().optional(),
  platform: z.string().optional(),
});

export const placeholderResponseSchema = z.object({
  status: z.string(),
  message: z.string(),
});

export const modelListResponseSchema = z.object({
  models: z.array(
    z.object({
      model_id: z.string().nullable().optional(),
      name: z.string(),
      engine_id: z.string().nullable().optional(),
      role: z.string().nullable().optional(),
    }),
  ),
  message: z.string().optional(),
});

export type HealthResponse = z.infer<typeof healthResponseSchema>;
export type VersionResponse = z.infer<typeof versionResponseSchema>;
export type PlaceholderResponse = z.infer<typeof placeholderResponseSchema>;
export type ModelListResponse = z.infer<typeof modelListResponseSchema>;

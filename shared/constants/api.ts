/** API route constants — mirror FastAPI /api/v1 */

export const API_V1_PREFIX = "/api/v1" as const;

export const API_ROUTES = {
  health: `${API_V1_PREFIX}/health`,
  version: `${API_V1_PREFIX}/version`,
  ocr: `${API_V1_PREFIX}/ocr`,
  train: `${API_V1_PREFIX}/train`,
  evaluate: `${API_V1_PREFIX}/evaluate`,
  evaluationReports: `${API_V1_PREFIX}/evaluation/reports`,
  benchmarks: `${API_V1_PREFIX}/benchmarks`,
  models: `${API_V1_PREFIX}/models`,
  datasets: `${API_V1_PREFIX}/datasets`,
  datasetPipelineRun: `${API_V1_PREFIX}/datasets/pipeline/run`,
} as const;

export const SCHEMA_VERSION = "1.0" as const;

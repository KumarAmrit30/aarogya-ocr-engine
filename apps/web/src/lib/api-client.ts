import {
  API_ROUTES,
  type BenchmarkListResponse,
  type DatasetListResponse,
  type DatasetRecord,
  type DatasetSearchQuery,
  type DatasetVersionDetail,
  type EvaluationReport,
  type HealthResponse,
  type ModelListResponse,
  type OCRRequest,
  type OCRResult,
  type PlaceholderResponse,
  type PublishedVersionResult,
  type ReportListResponse,
  type VersionResponse,
} from "@aarogya/shared";

function baseUrl(): string {
  if (typeof window !== "undefined") {
    return (
      window.localStorage.getItem("aarogya.apiBaseUrl") ||
      process.env.NEXT_PUBLIC_API_BASE_URL ||
      "http://localhost:8000"
    );
  }
  return process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";
}

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const response = await fetch(`${baseUrl()}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers || {}),
    },
  });
  if (!response.ok) {
    const text = await response.text();
    throw new Error(`${response.status} ${response.statusText}: ${text}`);
  }
  return response.json() as Promise<T>;
}

function datasetsQuery(params?: DatasetSearchQuery): string {
  if (!params) return API_ROUTES.datasets;
  const qs = new URLSearchParams();
  if (params.language) qs.set("language", params.language);
  if (params.license) qs.set("license", params.license);
  if (params.task) qs.set("task", params.task);
  if (params.script) qs.set("script", params.script);
  if (params.domain) qs.set("domain", params.domain);
  if (params.min_quality != null) qs.set("min_quality", String(params.min_quality));
  if (params.tags?.length) qs.set("tags", params.tags.join(","));
  if (params.pii_status) qs.set("pii_status", params.pii_status);
  if (params.name_contains) qs.set("name_contains", params.name_contains);
  const s = qs.toString();
  return s ? `${API_ROUTES.datasets}?${s}` : API_ROUTES.datasets;
}

export const apiClient = {
  health: () => request<HealthResponse>(API_ROUTES.health),
  version: () => request<VersionResponse>(API_ROUTES.version),
  ocr: (body: OCRRequest) =>
    request<OCRResult>(API_ROUTES.ocr, { method: "POST", body: JSON.stringify(body) }),
  train: (body: Record<string, unknown> = {}) =>
    request<PlaceholderResponse>(API_ROUTES.train, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  evaluate: (body: Record<string, unknown>) =>
    request<EvaluationReport>(API_ROUTES.evaluate, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  evaluationReports: () => request<ReportListResponse>(API_ROUTES.evaluationReports),
  benchmarks: () => request<BenchmarkListResponse>(API_ROUTES.benchmarks),
  models: () => request<ModelListResponse>(API_ROUTES.models),
  datasets: (params?: DatasetSearchQuery) => request<DatasetListResponse>(datasetsQuery(params)),
  dataset: (id: string) => request<DatasetRecord>(`${API_ROUTES.datasets}/${id}`),
  datasetVersion: (id: string, version: string) =>
    request<DatasetVersionDetail>(`${API_ROUTES.datasets}/${id}/versions/${version}`),
  runDatasetPipeline: (body: Record<string, unknown> = {}) =>
    request<PublishedVersionResult>(API_ROUTES.datasetPipelineRun, {
      method: "POST",
      body: JSON.stringify(body),
    }),
};

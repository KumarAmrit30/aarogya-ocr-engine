import {
  API_ROUTES,
  type HealthResponse,
  type ModelListResponse,
  type OCRRequest,
  type OCRResult,
  type PlaceholderResponse,
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
  evaluate: (body: Record<string, unknown> = {}) =>
    request<PlaceholderResponse>(API_ROUTES.evaluate, {
      method: "POST",
      body: JSON.stringify(body),
    }),
  models: () => request<ModelListResponse>(API_ROUTES.models),
};

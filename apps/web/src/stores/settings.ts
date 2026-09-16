"use client";

import { create } from "zustand";
import { persist } from "zustand/middleware";

type SettingsState = {
  apiBaseUrl: string;
  setApiBaseUrl: (url: string) => void;
};

export const useSettingsStore = create<SettingsState>()(
  persist(
    (set) => ({
      apiBaseUrl: process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000",
      setApiBaseUrl: (apiBaseUrl) => {
        if (typeof window !== "undefined") {
          window.localStorage.setItem("aarogya.apiBaseUrl", apiBaseUrl);
        }
        set({ apiBaseUrl });
      },
    }),
    { name: "aarogya-settings" },
  ),
);

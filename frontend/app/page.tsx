"use client";

import { useEffect, useState } from "react";

type HealthResponse = {
  status: string;
  service: string;
};

const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export default function HomePage() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(`${API_URL}/health`)
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        return response.json() as Promise<HealthResponse>;
      })
      .then(setHealth)
      .catch(() => setError("Backend is unavailable. Start FastAPI on port 8000."));
  }, []);

  return (
    <main style={{ minHeight: "100vh", fontFamily: "system-ui, sans-serif", padding: 40 }}>
      <section style={{ maxWidth: 900, margin: "0 auto" }}>
        <p style={{ letterSpacing: 2, textTransform: "uppercase", fontSize: 12 }}>LectureSync</p>
        <h1 style={{ fontSize: 48, margin: "12px 0" }}>
          Synchronize what the professor says with what the professor shows.
        </h1>
        <p style={{ fontSize: 18, lineHeight: 1.6, maxWidth: 720 }}>
          The application shell is now connected to the FastAPI backend.
        </p>
        <div style={{ marginTop: 32, padding: 24, border: "1px solid #ddd", borderRadius: 16 }}>
          <strong>Backend connection</strong>
          <p style={{ marginBottom: 0 }}>
            {health ? `✓ ${health.service} is healthy` : error ?? "Checking backend…"}
          </p>
        </div>
      </section>
    </main>
  );
}

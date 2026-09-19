export default function HomePage() {
  return (
    <main style={{ minHeight: "100vh", fontFamily: "system-ui, sans-serif", padding: 40 }}>
      <section style={{ maxWidth: 900, margin: "0 auto" }}>
        <p style={{ letterSpacing: 2, textTransform: "uppercase", fontSize: 12 }}>LectureSync</p>
        <h1 style={{ fontSize: 48, margin: "12px 0" }}>
          Synchronize what the professor says with what the professor shows.
        </h1>
        <p style={{ fontSize: 18, lineHeight: 1.6, maxWidth: 720 }}>
          The first milestone establishes the real application shell. Media processing,
          transcription, slide detection, and grounded AI will be added behind verified APIs.
        </p>
        <div style={{ marginTop: 32, padding: 24, border: "1px solid #ddd", borderRadius: 16 }}>
          <strong>Milestone 1</strong>
          <p style={{ marginBottom: 0 }}>Frontend scaffold is ready for the backend integration.</p>
        </div>
      </section>
    </main>
  );
}

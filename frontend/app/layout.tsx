import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "LectureSync",
  description: "Synchronize what the professor says with what the professor shows.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}

import Link from "next/link";

const NAV = [
  { href: "/", label: "Dashboard" },
  { href: "/upload", label: "Upload" },
  { href: "/playground", label: "Playground" },
  { href: "/models", label: "Models" },
  { href: "/experiments", label: "Experiments" },
  { href: "/datasets", label: "Datasets" },
  { href: "/evaluation", label: "Evaluation" },
  { href: "/benchmarks", label: "Benchmarks" },
  { href: "/registry", label: "Registry" },
  { href: "/errors", label: "Errors" },
  { href: "/settings", label: "Settings" },
];

export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen flex">
      <aside className="w-56 shrink-0 border-r border-surface-border bg-surface-card px-3 py-4">
        <div className="mb-6 px-2">
          <div className="text-xs uppercase tracking-wide text-ink-muted">Aarogya</div>
          <div className="font-semibold text-sm">AI Research Platform</div>
        </div>
        <nav className="flex flex-col gap-0.5">
          {NAV.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="rounded px-2 py-1.5 text-sm text-ink hover:bg-surface"
            >
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="flex-1 p-6 max-w-5xl">{children}</main>
    </div>
  );
}

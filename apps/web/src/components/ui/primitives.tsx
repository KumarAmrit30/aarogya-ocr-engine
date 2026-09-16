import * as React from "react";

import { cn } from "@/lib/utils";

export function PageHeader({
  title,
  description,
}: {
  title: string;
  description?: string;
}) {
  return (
    <header className="mb-6">
      <h1 className="text-xl font-semibold">{title}</h1>
      {description ? <p className="mt-1 text-sm text-ink-muted">{description}</p> : null}
    </header>
  );
}

export function Panel({
  children,
  className,
}: {
  children: React.ReactNode;
  className?: string;
}) {
  return (
    <div className={cn("rounded border border-surface-border bg-surface-card p-4", className)}>
      {children}
    </div>
  );
}

export function Button({
  children,
  className,
  ...props
}: React.ButtonHTMLAttributes<HTMLButtonElement>) {
  return (
    <button
      className={cn(
        "inline-flex items-center rounded bg-accent px-3 py-1.5 text-sm text-accent-fg disabled:opacity-50",
        className,
      )}
      {...props}
    >
      {children}
    </button>
  );
}

export const Input = React.forwardRef<HTMLInputElement, React.InputHTMLAttributes<HTMLInputElement>>(
  function Input({ className, ...props }, ref) {
    return (
      <input
        ref={ref}
        className={cn(
          "w-full rounded border border-surface-border bg-white px-2 py-1.5 text-sm",
          className,
        )}
        {...props}
      />
    );
  },
);

export function EmptyTable({ columns, message }: { columns: string[]; message: string }) {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-left text-sm">
        <thead>
          <tr className="border-b border-surface-border text-ink-muted">
            {columns.map((col) => (
              <th key={col} className="py-2 pr-4 font-medium">
                {col}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          <tr>
            <td colSpan={columns.length} className="py-6 text-ink-muted">
              {message}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}

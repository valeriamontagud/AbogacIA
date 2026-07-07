import { ReactNode } from "react";
import { Sidebar } from "@/shared/components/navigation/sidebar";

interface DashboardLayoutProps {
  children: ReactNode;
}

export function DashboardLayout({
  children,
}: DashboardLayoutProps) {
  return (
    <div className="flex min-h-screen">
      <Sidebar />

    <main className="ml-64 flex-1 bg-zinc-100 p-6">        {children}
      </main>
    </div>
  );
}
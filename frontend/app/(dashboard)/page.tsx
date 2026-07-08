"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

import { Topbar } from "@/shared/components/dashboard/topbar";
import { StatsCard } from "@/shared/components/dashboard/stats-card";
import { RecentActivity } from "@/shared/components/dashboard/recent-activity";

export default function HomePage() {
  const router = useRouter();
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    if (typeof window === "undefined") {
      return;
    }

    const token = window.localStorage.getItem("auth_token");

    if (!token) {
      router.replace("/login");
      return;
    }

    setIsAuthenticated(true);
  }, [router]);

  if (!isAuthenticated) {
    return null;
  }

  return (
    <>
      <Topbar />

      <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatsCard title="Clientes activos" value="18" />

        <StatsCard title="Expedientes abiertos" value="42" />

        <StatsCard title="Recordatorios" value="5" />

        <StatsCard title="Emails nuevos" value="12" />
      </section>

      <section className="mt-6">
        <RecentActivity />
      </section>
    </>
  );
}
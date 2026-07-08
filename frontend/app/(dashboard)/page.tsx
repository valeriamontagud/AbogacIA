"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

import { useAuthStore } from "@/features/auth/store/auth.store";

import { Topbar } from "@/shared/components/dashboard/topbar";
import { StatsCard } from "@/shared/components/dashboard/stats-card";
import { RecentActivity } from "@/shared/components/dashboard/recent-activity";

export default function HomePage() {

  const router = useRouter();

  const token =
    useAuthStore(
      (state) => state.token
    );

  useEffect(() => {

    if (!token) {

      router.replace("/login");

    }

  }, [token, router]);

  if (!token) {

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
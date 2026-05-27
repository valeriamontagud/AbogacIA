import { DashboardLayout } from "@/layouts/dashboard-layout";

import { Topbar } from "@/shared/components/dashboard/topbar";
import { StatsCard } from "@/shared/components/dashboard/stats-card";
import { RecentActivity } from "@/shared/components/dashboard/recent-activity";

export default function HomePage() {
  return (
    <DashboardLayout>
      <Topbar />

      <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-4">
        <StatsCard
          title="Clientes activos"
          value="18"
        />

        <StatsCard
          title="Expedientes abiertos"
          value="42"
        />

        <StatsCard
          title="Recordatorios"
          value="5"
        />

        <StatsCard
          title="Emails nuevos"
          value="12"
        />
      </section>

      <section className="mt-6">
        <RecentActivity />
      </section>
    </DashboardLayout>
  );
}
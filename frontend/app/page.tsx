import { DashboardLayout } from "@/layouts/dashboard-layout";

export default function HomePage() {
  return (
    <DashboardLayout>
      <div>
        <h1 className="text-4xl font-bold">
          Dashboard
        </h1>

        <p className="mt-2 text-zinc-600">
          Bienvenido a AbogacIA
        </p>
      </div>
    </DashboardLayout>
  );
}
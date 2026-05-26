import { DashboardLayout } from "@/layouts/dashboard-layout";

import { ClientCard } from "@/features/clients/components/client-card";

import { clients } from "@/features/clients/mock/clients.mock";

export default function ClientsPage() {
  return (
    <DashboardLayout>
      <div className="mb-8 flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold">
            Clientes
          </h1>

          <p className="mt-2 text-zinc-500">
            Gestiona clientes y expedientes
          </p>
        </div>

        <button className="rounded-xl bg-black px-5 py-3 text-white transition hover:bg-zinc-800">
          + Nuevo cliente
        </button>
      </div>

      <div className="mb-6 flex items-center gap-4">
        <input
          placeholder="Buscar cliente o expediente..."
          className="w-full rounded-xl border bg-white px-4 py-3 outline-none"
        />

        <select className="rounded-xl border bg-white px-4 py-3 outline-none">
          <option>
            Última modificación
          </option>

          <option>
            Nombre
          </option>
        </select>
      </div>

      <section className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        {clients.map((client) => (
          <ClientCard
            key={client.id}
            client={client}
          />
        ))}
      </section>
    </DashboardLayout>
  );
}
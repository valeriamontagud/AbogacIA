import { ClientsTable } from "@/features/clients/components/clients-table";

export default function ClientsPage() {
  return (
    <>
      <div className="mb-8 flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold">
            Clientes
          </h1>

          <p className="mt-2 text-zinc-500">
            Gestiona clientes y expedientes
          </p>
        </div>

        <button className="rounded-xl bg-black px-5 py-3 text-white">
          + Nuevo cliente
        </button>
      </div>

      <ClientsTable />
    </>
  );
}
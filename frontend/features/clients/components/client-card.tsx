import { Client } from "../types/client.types";

interface ClientCardProps {
  client: Client;
}

export function ClientCard({
  client,
}: ClientCardProps) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm transition hover:shadow-md">
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-xl font-bold">
            {client.name}
          </h2>

          <p className="mt-1 text-sm text-zinc-500">
            {client.expediente}
          </p>
        </div>

        <span
          className={`rounded-full px-3 py-1 text-xs font-medium ${
            client.status === "ACTIVE"
              ? "bg-green-100 text-green-700"
              : "bg-yellow-100 text-yellow-700"
          }`}
        >
          {client.status}
        </span>
      </div>

      <div className="mt-6 space-y-2 text-sm text-zinc-600">
        <p>
          {client.cases} expedientes activos
        </p>

        <p>
          Modificado {client.updatedAt}
        </p>
      </div>
    </div>
  );
}
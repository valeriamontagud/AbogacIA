
/* Ací creem la tabla de clientes, el estil i tot això. Agafa els datos de mock */
"use client";

import { useRouter } from "next/navigation";
import { clientsMock } from "../mock/clients.mock";

export function ClientsTable() {
  const router = useRouter();

  return (
    <div className="overflow-hidden rounded-xl border bg-white">
      <table className="w-full">
        <thead className="border-b bg-zinc-50">
          <tr>
            <th className="px-4 py-3 text-left text-sm font-semibold">
              Cliente
            </th>

            <th className="px-4 py-3 text-left text-sm font-semibold">
              Expediente
            </th>

            <th className="px-4 py-3 text-left text-sm font-semibold">
            Estado
            </th>

            <th className="px-4 py-3 text-left text-sm font-semibold">
              Documentos
            </th>

            <th className="px-4 py-3 text-left text-sm font-semibold">
              Última actuación
            </th>
          </tr>
        </thead>

        <tbody>
          {clientsMock.map((client) => (
          <tr
            key={client.id}
            onClick={() =>
              router.push(`/clients/${client.id}`)
            } /* Ací es on fem que quan cliquem a una fila ens porti a la pàgina de detall del client, que encara no hem creat però ja tenim el mock preparat per a això. */
            className="cursor-pointer border-b transition hover:bg-zinc-50"
          >
              <td className="px-4 py-4">
                {client.fullName}
              </td>

              <td className="px-4 py-4">
                {client.caseNumber}
              </td>

                <td className="px-4 py-4">
                <span
                    className={`inline-flex w-28 justify-center rounded-full px-3 py-1 text-xs font-medium ${
                    client.status === "Apertura"
                        ? "bg-blue-100 text-blue-700"
                        : client.status === "Tramitación"
                        ? "bg-yellow-100 text-yellow-700"
                        : client.status === "Judicial"
                        ? "bg-orange-100 text-orange-700"
                        : "bg-green-100 text-green-700"
                    }`}
                >
                    {client.status}
                </span>
                </td>

              <td className="px-4 py-4">
                {client.documentsCount}
              </td>

              <td className="px-4 py-4">
                {client.lastActivity}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

console.log("🔥 useClients");
import { useEffect, useState } from "react";

import { clientsService } from "../api/clients.service";
import { ClientMapper } from "../mappers/client.mapper";
import { ClientTableRow } from "../types/client.view";

console.log("📡 llamando al backend");
export function useClients() {
  const [clients, setClients] = useState<ClientTableRow[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  async function loadClients() {
    try {
      setLoading(true);

      const data = await clientsService.getClients();

      setClients(
        data.map((client) =>
          ClientMapper.toTableRow(client)
        )
      );

      setError(null);
    } catch (err) {
      setError(
        err instanceof Error
          ? err.message
          : "Ha ocurrido un error"
      );
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadClients();
  }, []);

  return {
    clients,
    loading,
    error,
    refresh: loadClients,
  };
}
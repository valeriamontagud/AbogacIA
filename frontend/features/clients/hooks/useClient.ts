"use client";

import { useEffect, useState } from "react";

import { clientsService } from "../api/clients.service";
import { ClientMapper } from "../mappers/client.mapper";

import { ClientDetailView } from "../types/client.view";

export function useClient(
  id: string
) {
  const [client, setClient] =
    useState<ClientDetailView | null>(
      null
    );

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState<string | null>(null);

  async function loadClient() {
    try {
      setLoading(true);

      const data =
        await clientsService.getClient(id);

      setClient(
        ClientMapper.toDetail(data)
      );

      setError(null);

    } catch (err) {

      setError(
        err instanceof Error
          ? err.message
          : "Error cargando cliente"
      );

    } finally {

      setLoading(false);

    }
  }

  useEffect(() => {

    if (id) {

      loadClient();

    }

  }, [id]);

  return {
    client,
    loading,
    error,
    refresh: loadClient,
  };
}
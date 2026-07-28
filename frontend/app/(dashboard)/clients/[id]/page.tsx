"use client";

import { useParams } from "next/navigation";

import { ClientDetailContent } from "@/features/clients/components/client-detail/client-detail-content";
import { useClient } from "@/features/clients/hooks/useClient";

export default function ClientDetailPage() {

  const params = useParams();

  const id = params.id as string;

  const {
    client,
    loading,
    error,
  } = useClient(id);

  if (loading) {
    return (
      <div className="p-6">
        Cargando cliente...
      </div>
    );
  }

  if (error) {
    return (
      <div className="p-6 text-red-500">
        {error}
      </div>
    );
  }

  if (!client) {
    return (
      <div className="p-6">
        Cliente no encontrado
      </div>
    );
  }

  return (
    <ClientDetailContent
      client={client}
    />
  );
}
import { clientsMock } from "@/features/clients/mock/clients.mock";
import { ClientInfoTab } from "@/features/clients/components/client-info/client-info-tab";
import { ClientDetailContent } from "@/features/clients/components/client-detail/client-detail-content"
// ======================================================
// Types
// ======================================================

interface ClientDetailPageProps {
  params: Promise<{
    id: string;
  }>;
}

// ======================================================
// Client Detail Page
// ======================================================

export default async function ClientDetailPage({
  params,
}: ClientDetailPageProps) {
  // Obtener ID desde la URL
  const { id } = await params;

  // Buscar cliente en mock
  const client = clientsMock.find(
    (c) => c.id === id
  );

  // Cliente no encontrado
  if (!client) {
    return (
      <div className="text-center">
        <h1 className="text-4xl font-bold">
          Cliente no encontrado
        </h1>
      </div>
    );
  }

    return (
    <ClientDetailContent
        client={client}
    />
    );
}
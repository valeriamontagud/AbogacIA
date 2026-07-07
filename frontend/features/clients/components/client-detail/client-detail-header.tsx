// ======================================================
// Client Detail Header
// ======================================================

interface ClientDetailHeaderProps {
  client: {
    id: string;
    fullName: string;
    caseNumber: string;
    status: string;
    documentsCount: number;
    lastActivity: string;
  };
}

export function ClientDetailHeader({
  client,
}: ClientDetailHeaderProps) {
  return (
    <div className="mb-8">

      <h1 className="text-4xl font-bold">
        Expediente {client.caseNumber}
      </h1>

      <p className="mt-2 text-zinc-500">
        Cliente {client.fullName}
      </p>

    </div>
  );
}
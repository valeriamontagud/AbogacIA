"use client";

// ======================================================
// Client Detail Content
// ======================================================

interface ClientDetailContentProps {
  client: {
    id: string;
    fullName: string;
    caseNumber: string;
    status: string;
    documentsCount: number;
    lastActivity: string;
  };
}

export function ClientDetailContent({
  client,
}: ClientDetailContentProps) {
  return (
    <>
      {/* ==================================================
          Header expediente
      ================================================== */}

      <div className="mb-8">
        <h1 className="text-4xl font-bold">
          Expediente {client.caseNumber}
        </h1>

        <p className="mt-2 text-zinc-500">
          Cliente {client.fullName}
        </p>
      </div>

      {/* ==================================================
          Navegación expediente
      ================================================== */}

      <div className="border-b">
        <nav className="flex gap-8">
          <button className="border-b-2 border-black pb-3 text-sm font-medium">
            Ficha
          </button>

          <button className="pb-3 text-sm text-zinc-500">
            Apertura
          </button>

          <button className="pb-3 text-sm text-zinc-500">
            Tramitación
          </button>

          <button className="pb-3 text-sm text-zinc-500">
            Judicial
          </button>

          <button className="pb-3 text-sm text-zinc-500">
            Contabilidad
          </button>
        </nav>
      </div>

      {/* ==================================================
          Contenido activo
      ================================================== */}

      <div className="mt-8">
        Aquí irá la pestaña activa
      </div>
    </>
  );
}
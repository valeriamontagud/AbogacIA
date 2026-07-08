// ======================================================
// Opening Summary
//
// Estado general del expediente.
//
// En el futuro estos datos vendrán del backend
// y se actualizarán automáticamente mediante la IA.
// ======================================================

export function OpeningSummary() {
  return (
    <div className="rounded-xl border bg-white p-6">

      {/* ==============================================
          Cabecera
      ============================================== */}

      <div className="flex items-center justify-between">

        <div>
          <h2 className="text-xl font-semibold">
            Estado del expediente
          </h2>

          <p className="mt-1 text-sm text-zinc-500">
            La IA actualizará automáticamente el estado conforme se
            incorporen documentos y se completen acciones.
          </p>
        </div>

        <span className="rounded-full bg-zinc-100 px-3 py-1 text-sm text-zinc-600">
          Última actualización · Hace 2 horas
        </span>

      </div>

      {/* ==============================================
          Resumen
      ============================================== */}

      <div className="mt-8 grid gap-4 md:grid-cols-3">

        <StatusCard
          title="Documentación"
          value="2 / 4"
          description="Documentos recibidos"
        />

        <StatusCard
          title="Contratación"
          value="1 / 3"
          description="Documentos generados"
        />

        <StatusCard
          title="Asistente IA"
          value="Pendiente"
          description="Esperando documentación"
        />

      </div>

    </div>
  );
}

// ======================================================
// Types
// ======================================================

interface StatusCardProps {
  title: string;
  value: string;
  description: string;
}

// ======================================================
// Status Card
// ======================================================

function StatusCard({
  title,
  value,
  description,
}: StatusCardProps) {
  return (
    <div className="rounded-xl border bg-zinc-50 p-5">

      <p className="text-sm font-medium text-zinc-500">
        {title}
      </p>

      <h3 className="mt-3 text-3xl font-bold">
        {value}
      </h3>

      <p className="mt-2 text-sm text-zinc-500">
        {description}
      </p>

    </div>
  );
}
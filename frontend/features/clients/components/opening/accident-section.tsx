// ======================================================
// Accident Section
//
// La IA completará automáticamente estos datos
// cuando analice la documentación del expediente.
// ======================================================

export function AccidentSection() {
  return (
    <div className="rounded-xl border bg-white p-6">

      <h2 className="text-xl font-semibold">
        Datos del accidente
      </h2>

      <p className="mt-2 text-sm text-zinc-500">
        Estos datos se completarán automáticamente cuando la IA analice el
        atestado, el parte amistoso y el resto de la documentación aportada.
        Mientras tanto, también podrán rellenarse manualmente.
      </p>

      {/* ==============================================
          Información detectada
      ============================================== */}

      <div className="mt-8 grid gap-6 md:grid-cols-2">

        <DetectedField
          label="Fecha del accidente"
        />

        <DetectedField
          label="Hora del accidente"
        />

        <DetectedField
          label="Lugar del accidente"
        />

        <DetectedField
          label="Descripción"
        />

      </div>

    </div>
  );
}

// ======================================================
// Campo detectado por IA
// ======================================================

interface DetectedFieldProps {
  label: string;
}

function DetectedField({
  label,
}: DetectedFieldProps) {
  return (
    <div>

      <label className="mb-2 block text-sm font-medium">
        {label}
      </label>

      <div className="rounded-lg border bg-zinc-50 px-4 py-3">

        <p className="text-sm text-zinc-400">
          Pendiente de analizar
        </p>

      </div>

      <p className="mt-2 text-xs text-zinc-500">
        La IA completará este campo automáticamente cuando disponga de la
        documentación necesaria.
      </p>

    </div>
  );
}
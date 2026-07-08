// ======================================================
// Vehicles Section
//
// Información de los vehículos implicados.
//
// La IA completará estos datos automáticamente
// cuando analice el atestado o el parte amistoso.
// ======================================================

export function VehiclesSection() {
  return (
    <div className="rounded-xl border bg-white p-6">

      <h2 className="text-xl font-semibold">
        Vehículos implicados
      </h2>

      <p className="mt-2 text-sm text-zinc-500">
        La IA identificará automáticamente las matrículas,
        aseguradoras y demás datos de los vehículos cuando
        analice la documentación aportada.
      </p>

      <div className="mt-8 grid gap-6 lg:grid-cols-2">

        {/* ==============================================
            Vehículo cliente
        ============================================== */}

        <VehicleCard
          title="Vehículo del cliente"
        />

        {/* ==============================================
            Vehículo contrario
        ============================================== */}

        <VehicleCard
          title="Vehículo contrario"
        />

      </div>

    </div>
  );
}

// ======================================================
// Types
// ======================================================

interface VehicleCardProps {
  title: string;
}

// ======================================================
// Vehicle Card
// ======================================================

function VehicleCard({
  title,
}: VehicleCardProps) {
  return (
    <div className="rounded-xl border bg-zinc-50 p-5">

      <h3 className="mb-5 font-semibold">
        {title}
      </h3>

      <VehicleField label="Matrícula" />

      <VehicleField label="Marca" />

      <VehicleField label="Modelo" />

      <VehicleField label="Aseguradora" />

    </div>
  );
}

// ======================================================
// Vehicle Field
// ======================================================

interface VehicleFieldProps {
  label: string;
}

function VehicleField({
  label,
}: VehicleFieldProps) {
  return (
    <div className="mb-4">

      <label className="mb-1 block text-sm font-medium">
        {label}
      </label>

      <div className="rounded-lg border bg-white px-4 py-3">

        <span className="text-sm text-zinc-400">
          Pendiente de analizar
        </span>

      </div>

    </div>
  );
}
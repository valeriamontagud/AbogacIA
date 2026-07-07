// ======================================================
// Client Info Tab
// ======================================================

export function ClientInfoTab() {
  return (
    <section className="mt-8 space-y-8">

      {/* ==============================================
          Datos personales
      ============================================== */}

      <div className="rounded-xl border bg-white p-6">
        <h2 className="mb-6 text-xl font-semibold">
          Datos personales
        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <div>
            <label className="mb-2 block text-sm font-medium">
              Nombre
            </label>

            <input
              className="w-full rounded-lg border px-4 py-3"
              placeholder="Nombre"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Apellidos
            </label>

            <input
              className="w-full rounded-lg border px-4 py-3"
              placeholder="Apellidos"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              DNI
            </label>

            <input
              className="w-full rounded-lg border px-4 py-3"
              placeholder="12345678A"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Teléfono
            </label>

            <input
              className="w-full rounded-lg border px-4 py-3"
              placeholder="600123123"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Correo electrónico
            </label>

            <input
              className="w-full rounded-lg border px-4 py-3"
              placeholder="cliente@email.com"
            />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Dirección
            </label>

            <input
              className="w-full rounded-lg border px-4 py-3"
              placeholder="Dirección completa"
            />
          </div>

        </div>
      </div>

      {/* ==============================================
          Datos bancarios
      ============================================== */}

      <div className="rounded-xl border bg-white p-6">
        <h2 className="mb-6 text-xl font-semibold">
          Datos bancarios
        </h2>

        <input
          className="w-full rounded-lg border px-4 py-3"
          placeholder="IBAN"
        />
      </div>

      {/* ==============================================
          Documentación
      ============================================== */}

      <div className="rounded-xl border bg-white p-6">
        <h2 className="mb-6 text-xl font-semibold">
          Documentación
        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <div>
            <label className="mb-2 block text-sm font-medium">
              DNI
            </label>

            <input type="file" />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Certificado digital
            </label>

            <input type="file" />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Póliza vehículo
            </label>

            <input type="file" />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Condiciones generales
            </label>

            <input type="file" />
          </div>

          <div>
            <label className="mb-2 block text-sm font-medium">
              Condiciones particulares
            </label>

            <input type="file" />
          </div>

        </div>
      </div>

      {/* ==============================================
          IA futura
      ============================================== */}

      <div className="rounded-xl border border-dashed bg-zinc-50 p-6">
        <h2 className="mb-3 text-xl font-semibold">
          Asistente IA
        </h2>

        <p className="text-zinc-600">
          La IA extraerá automáticamente los datos del
          DNI, pólizas y demás documentación.
        </p>
      </div>

    </section>
  );
}
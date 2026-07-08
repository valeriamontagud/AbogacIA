// ======================================================
// Document Import
//
// Componente reutilizable para importar documentación.
//
// Se utilizará en:
// - Ficha del cliente
// - Apertura
// - Judicial
// - Contabilidad
// ======================================================

interface DocumentImportProps {
  title: string;
  description: string;
  requiredDocuments: string[];
}

export function DocumentImport({
  title,
  description,
  requiredDocuments,
}: DocumentImportProps) {
  return (
    <section className="rounded-xl border bg-white p-6">

      {/* ==============================================
          Cabecera
      ============================================== */}

      <h2 className="text-2xl font-semibold">
        {title}
      </h2>

      <p className="mt-2 text-sm text-zinc-500">
        {description}
      </p>

      {/* ==============================================
          Contenido
      ============================================== */}

      <div className="mt-8 grid gap-6 lg:grid-cols-[2fr_1fr]">

        {/* ==========================================
            Zona de subida
        ========================================== */}

        <div className="rounded-xl border-2 border-dashed border-zinc-300 bg-zinc-50 p-8 transition hover:border-black hover:bg-zinc-100">

          <div className="flex h-full flex-col items-center justify-center text-center">

            <div className="text-5xl">
              📄
            </div>

            <h3 className="mt-4 text-lg font-semibold">
              Arrastra la documentación aquí
            </h3>

            <p className="mt-2 max-w-md text-sm text-zinc-500">
              Puedes importar uno o varios documentos.
              La IA los clasificará automáticamente.
            </p>

            <button className="mt-6 rounded-lg bg-black px-5 py-3 text-sm font-medium text-white transition hover:bg-zinc-800">
              Añadir documentación
            </button>

          </div>

        </div>

        {/* ==========================================
            Documentación esperada
        ========================================== */}

        <div className="rounded-xl border bg-zinc-50 p-6">

          <h3 className="text-lg font-semibold">
            Documentación esperada
          </h3>

          <p className="mt-2 text-sm text-zinc-500">
            La IA localizará automáticamente cada documento.
          </p>

          <div className="mt-6 space-y-3">

            {requiredDocuments.map((document) => (

              <div
                key={document}
                className="flex items-center justify-between rounded-lg bg-white px-4 py-3"
              >

                <span className="text-sm">
                  {document}
                </span>

                <span className="rounded-full bg-orange-100 px-3 py-1 text-xs font-medium text-orange-700">
                  Pendiente
                </span>

              </div>

            ))}

          </div>

        </div>

      </div>

    </section>
  );
}
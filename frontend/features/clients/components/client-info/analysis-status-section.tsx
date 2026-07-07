const documents = [
  "DNI",
  "Certificado digital",
  "Cuenta bancaria",
  "Póliza",
  "Condiciones particulares",
];

export function AnalysisStatusSection() {
  return (
    <section className="rounded-xl border bg-white p-6">

      <h2 className="text-xl font-semibold">
        Estado del análisis
      </h2>

      <div className="mt-6 h-3 overflow-hidden rounded-full bg-zinc-200">

        <div
          className="h-full rounded-full bg-black"
          style={{ width: "60%" }}
        />

      </div>

      <p className="mt-3 text-sm text-zinc-500">
        3 de 5 documentos detectados
      </p>

      <div className="mt-6 space-y-3">

        {documents.map((document, index) => (

          <div
            key={document}
            className="flex items-center justify-between rounded-lg bg-zinc-50 px-4 py-3"
          >

            <span>{document}</span>

            {index < 3 ? (
              <span className="text-green-600">
                ✔ Detectado
              </span>
            ) : (
              <span className="text-orange-500">
                Pendiente
              </span>
            )}

          </div>

        ))}

      </div>

    </section>
  );
}
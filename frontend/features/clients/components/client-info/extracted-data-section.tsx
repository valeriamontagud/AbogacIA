import { DetectedInput } from "./detected-input";

export function ExtractedDataSection() {
  return (
    <>
      <section className="rounded-xl border bg-white p-6">

        <h2 className="mb-6 text-xl font-semibold">
          Información extraída por IA
        </h2>

        <div className="grid gap-6 md:grid-cols-2">

          <DetectedInput label="Nombre" />
          <DetectedInput label="Apellidos" />
          <DetectedInput label="DNI" />
          <DetectedInput label="Teléfono" />
          <DetectedInput label="Correo electrónico" />
          <DetectedInput label="Dirección" />
          <DetectedInput label="Cuenta bancaria (IBAN)" />

        </div>

      </section>
    </>
  );
}
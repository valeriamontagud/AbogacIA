import { DocumentImport } from "@/shared/components/document-import";
import { AnalysisStatusSection } from "./analysis-status-section";
import { ExtractedDataSection } from "./extracted-data-section";

export function ClientInfoTab() {
  return (
    <section className="mt-8 space-y-8">

      <DocumentImport
        title="Documentación del cliente"
        description="Importa toda la documentación disponible del cliente. La IA clasificará automáticamente los archivos y completará la ficha."
        requiredDocuments={[
          "DNI",
          "Cuenta bancaria",
          "Certificado digital",
          "Póliza del vehículo",
          "Condiciones particulares",
  ]}
/>

      <AnalysisStatusSection />

      <ExtractedDataSection />


    </section>
  );
}
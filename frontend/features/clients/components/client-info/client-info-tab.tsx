import { DocumentImport } from "@/shared/components/document-import";
import { ExtractedDataSection } from "./extracted-data-section";
import { AnalysisStatus } from "@/shared/components/ai-analysis/analysis-status";

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

      <AnalysisStatus
        detected={3}
        documents={[
          "DNI",
          "Certificado digital",
          "Cuenta bancaria",
          "Póliza",
          "Condiciones particulares",
  ]}
/>

      <ExtractedDataSection />


    </section>
  );
}
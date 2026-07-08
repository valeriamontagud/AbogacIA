import {DocumentImport} from "@/shared/components/document-import";  
import { OpeningSummary } from "./opening-summary";
import { AccidentSection } from "./accident-section";
import { VehiclesSection } from "./vehicles-section";

export function OpeningTab() {
  return (
    <section className="mt-8 space-y-8">

      <DocumentImport
        title="Documentación del siniestro"
        description="Importa toda la documentación relacionada con el accidente. La IA analizará los documentos y completará automáticamente los datos del siniestro."
        requiredDocuments={[
          "Parte amistoso",
          "Atestado policial",
          "Permiso de circulación",
          "Ficha técnica",
          "Fotografías",
          "Informe pericial",
          "Presupuesto / factura",
        ]}
      />


      <AccidentSection />

      <VehiclesSection />

      <OpeningSummary />

    </section>
  );
}

/* Ací creem un mock de clients per a la taula de clients. */
import { Client } from "../types/client.types";

export const clientsMock: Client[] = [
  {
    id: "1",
    fullName: "Juan Pérez",
    caseNumber: "TRF-2026-001",
    status: "Apertura",
    documentsCount: 24,
    lastActivity: "Hace 2 días",
  },
  {
    id: "2",
    fullName: "María López",
    caseNumber: "TRF-2026-002",
    status: "Tramitación",
    documentsCount: 12,
    lastActivity: "Hoy",
  },
  {
    id: "3",
    fullName: "Antonio Ruiz",
    caseNumber: "TRF-2026-003",
    status: "Judicial",
    documentsCount: 37,
    lastActivity: "Hace 5 días",
  },
  {
    id: "4",
    fullName: "Laura García",
    caseNumber: "TRF-2026-004",
    status: "Contabilidad",
    documentsCount: 18,
    lastActivity: "Hace 1 día",
  },
];
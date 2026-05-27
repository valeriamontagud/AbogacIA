import { Client } from "../types/client.types";

export const clients: Client[] = [
  {
    id: "1",
    name: "Juan Pérez",
    expediente: "EXP-2026-0142",
    cases: 2,
    updatedAt: "hace 2 horas",
    status: "ACTIVE",
  },
  {
    id: "2",
    name: "Marta López",
    expediente: "EXP-2026-0201",
    cases: 1,
    updatedAt: "ayer",
    status: "ACTIVE",
  },
  {
    id: "3",
    name: "Carlos Ruiz",
    expediente: "EXP-2026-0188",
    cases: 3,
    updatedAt: "hace 5 minutos",
    status: "PENDING",
  },
];
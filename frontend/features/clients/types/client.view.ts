export interface ClientTableRow {
  id: string;

  fullName: string;

  caseNumber: string;

  status: string;

  documentsCount: number;

  lastActivity: string;
}

export interface ClientDetailView {
  id: string;

  fullName: string;

  caseNumber: string;

  status: string;

  documentsCount: number;

  lastActivity: string;

  dni: string;

  birthDate: string;

  accidentDate: string;

  address: string;

  phone: string;

  email: string;

  notes: string;
}
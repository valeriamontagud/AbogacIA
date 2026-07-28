import { Client } from "../types/client.types";
import {
  ClientTableRow,
  ClientDetailView,
} from "../types/client.view";

export class ClientMapper {
  static toTableRow(
    client: Client
  ): ClientTableRow {
    return {
      id: client.id,

      fullName: client.full_name,

      caseNumber: "Pendiente",

      status: "Apertura",

      documentsCount: 0,

      lastActivity: new Date(
        client.updated_at
      ).toLocaleDateString("es-ES"),
    };
  }

  static toDetail(
    client: Client
  ): ClientDetailView {
    return {
      id: client.id,

      fullName: client.full_name,

      caseNumber: "Pendiente",

      status: "Apertura",

      documentsCount: 0,

      lastActivity: new Date(
        client.updated_at
      ).toLocaleDateString("es-ES"),

      dni: client.dni ?? "",

      birthDate: client.birth_date ?? "",

      accidentDate: client.accident_date ?? "",

      address: client.address ?? "",

      phone: client.phone ?? "",

      email: client.email ?? "",

      notes: client.notes ?? "",
      
    };
  }
}
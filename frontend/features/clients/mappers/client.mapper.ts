//Cuando mas adelante añadimos los otros campos simplemente tendremos que cambiar el ClientMapper y ya funcionara sin tocar nada mas 

import { Client } from "../types/client.types";
import { ClientTableRow } from "../types/client.view";

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

      lastActivity:
        new Date(client.updated_at)
          .toLocaleDateString("es-ES"),
    };
  }
}
//UNica clase que conocera las URLS del backend y los tipos de datos que se utilizan en el frontend, si cambiamos algo en el backend solo tendremos que cambiarlo aqui y no tocar nada mas en el frontend

/**import { http } from "@/lib/http";

import {
  Client,
} from "../types/client.types";

import {
  CreateClientDto,
  UpdateClientDto,
} from "../types/client.dto";

export class ClientsService {

  async getClients(): Promise<Client[]> {

    return http.get<Client[]>(
      "/clients"
    );
  }

  async getClient(
    id: string
  ): Promise<Client> {

    return http.get<Client>(
      `/clients/${id}`
    );
  }

  async createClient(
    data: CreateClientDto
  ): Promise<Client> {

    return http.post<Client>(
      "/clients",
      data
    );
  }

  async updateClient(
    id: string,
    data: UpdateClientDto
  ): Promise<Client> {

    return http.patch<Client>(
      `/clients/${id}`,
      data
    );
  }
}

export const clientsService =
  new ClientsService(); */

  import { http } from "@/lib/http";

import { Client } from "../types/client.types";
import {
  CreateClientDto,
  UpdateClientDto,
} from "../types/client.dto";

export class ClientsService {
  async getClients(): Promise<Client[]> {
    console.log("➡️ GET /clients");

    return http.get<Client[]>("/clients");
  }

  async getClient(id: string): Promise<Client> {
    return http.get<Client>(`/clients/${id}`);
  }

  async createClient(
    data: CreateClientDto
  ): Promise<Client> {
    return http.post<Client>("/clients", data);
  }

  async updateClient(
    id: string,
    data: UpdateClientDto
  ): Promise<Client> {
    return http.patch<Client>(
      `/clients/${id}`,
      data
    );
  }
}

export const clientsService =
  new ClientsService();
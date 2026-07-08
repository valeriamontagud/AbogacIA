export interface CreateClientDto {

  full_name: string;

  dni?: string;

  birth_date?: string;

  accident_date?: string;

  address?: string;

  phone?: string;

  email?: string;

  notes?: string;
}

export interface UpdateClientDto {

  full_name?: string;

  dni?: string;

  birth_date?: string;

  accident_date?: string;

  address?: string;

  phone?: string;

  email?: string;

  notes?: string;
}
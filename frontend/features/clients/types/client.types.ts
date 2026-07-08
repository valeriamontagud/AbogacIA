/*Açò son els tipos de datos que utilitzem per a la taula de clients. Posteriormente añadiremos los otros campos acutalmente solo tenemos estos */
export interface Client {

  id: string;

  full_name: string;

  dni: string | null;

  birth_date: string | null;

  accident_date: string | null;

  address: string | null;

  phone: string | null;

  email: string | null;

  notes: string | null;

  data_source: string;

  created_by_user_id: string;

  created_at: string;

  updated_at: string;
}
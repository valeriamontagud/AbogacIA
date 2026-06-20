/*Açò son els tipos de datos que utilitzem per a la taula de clients. */
export interface Client {
  id: string;

  fullName: string;

  caseNumber: string;

  status: string;

  documentsCount: number;

  lastActivity: string;
}
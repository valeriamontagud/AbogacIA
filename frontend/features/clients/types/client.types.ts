export interface Client {
  id: string;
  name: string;
  expediente: string;
  cases: number;
  updatedAt: string;
  status: "ACTIVE" | "PENDING";
}
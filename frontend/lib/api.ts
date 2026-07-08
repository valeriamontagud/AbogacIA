import { API_URL } from "./config";
import { useAuthStore } from "@/features/auth/store/auth.store";

type HttpMethod =
  | "GET"
  | "POST"
  | "PATCH"
  | "PUT"
  | "DELETE";

interface RequestOptions {
  method?: HttpMethod;
  body?: unknown;
  headers?: HeadersInit;
}

export async function api<T>(
  endpoint: string,
  options: RequestOptions = {}
): Promise<T> {

  const token =
    useAuthStore.getState().token;
    console.log("TOKEN =", token);
    console.log("URL =", `${API_URL}${endpoint}`);
  const response = await fetch(
    `${API_URL}${endpoint}`,
    {
      method:
        options.method ?? "GET",

      headers: {

        ...(token
          ? {
              Authorization:
                `Bearer ${token}`,
            }
          : {}),

        "Content-Type":
          "application/json",

        ...options.headers,
      },

      body:
        options.body !== undefined
          ? JSON.stringify(
              options.body
            )
          : undefined,
    }
  );

  if (!response.ok) {

    throw new Error(
      await response.text()
    );
  }

  return response.json();
}
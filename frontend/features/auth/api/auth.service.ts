import {
  LoginCredentials,
  LoginResponse,
  User,
} from "../types/auth.types";

import { API_URL } from "@/lib/config";


export async function login(
  credentials: LoginCredentials
): Promise<LoginResponse> {
  const formData = new URLSearchParams();

  formData.append(
    "username",
    credentials.email
  );

  formData.append(
    "password",
    credentials.password
  );
console.log("API_URL:", API_URL);
console.log("LOGIN URL =", `${API_URL}/auth/login`);
  const response = await fetch(
    `${API_URL}/auth/login`,
    {
      method: "POST",
      headers: {
        "Content-Type":
          "application/x-www-form-urlencoded",
      },
      body: formData,
    }
  );

  if (!response.ok) {
    throw new Error(
      "Credenciales incorrectas"
    );
  }

  return response.json();
}

export async function getCurrentUser(
  token: string
): Promise<User> {
  const response = await fetch(
    `${API_URL}/auth/me`,
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  if (!response.ok) {
    throw new Error(
      "No se pudo obtener el usuario"
    );
  }

  return response.json();
}
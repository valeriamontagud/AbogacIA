"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

import {
  login,
  getCurrentUser,
} from "@/features/auth/api/auth.service";

import { useAuthStore } from "@/features/auth/store/auth.store";

export function LoginForm() {
  const router = useRouter();

  const [email, setEmail] =
    useState("");

  const [password, setPassword] =
    useState("");

  const [loading, setLoading] =
    useState(false);

  const handleSubmit = async (
    e: React.FormEvent
  ) => {
    e.preventDefault();

    try {
      setLoading(true);

      const response =
        await login({
          email,
          password,
        });

      console.log("LOGIN OK", response);

      const authStore = useAuthStore.getState();

      authStore.setToken(response.access_token);

      console.log("TOKEN EN STORE", useAuthStore.getState().token);

      const user = await getCurrentUser(response.access_token);

      console.log("USER", user);

      authStore.setUser(user);

      console.log("ANTES DEL REDIRECT");

      router.replace("/");

    } catch (error) {

      console.error(
        "Error login:",
        error
      );

    } finally {

      setLoading(false);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="space-y-4"
    >
      <Input
        type="email"
        placeholder="Correo electrónico"
        value={email}
        onChange={(e) =>
          setEmail(e.target.value)
        }
      />

      <Input
        type="password"
        placeholder="Contraseña"
        value={password}
        onChange={(e) =>
          setPassword(e.target.value)
        }
      />

      <Button
        type="submit"
        className="w-full"
        disabled={loading}
      >
        {loading
          ? "Iniciando sesión..."
          : "Iniciar sesión"}
      </Button>
    </form>
  );
}


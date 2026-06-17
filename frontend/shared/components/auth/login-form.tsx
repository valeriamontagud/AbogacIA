"use client";

import { useState } from "react";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { login } from "@/features/auth/api/auth.service";

export function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

const handleSubmit = async (
  e: React.FormEvent
) => {
  e.preventDefault();

  try {
    const response = await login({
      email,
      password,
    });

    console.log(
      "JWT recibido:",
      response
    );
  } catch (error) {
    console.error(
      "Error login:",
      error
    );
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
      >
        Iniciar sesión
      </Button>
    </form>
  );
}
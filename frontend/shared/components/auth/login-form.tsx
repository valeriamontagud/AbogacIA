"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";

import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { login } from "@/features/auth/api/auth.service";

export function LoginForm() {
  const router = useRouter();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const response = await login({
        email,
        password,
      });

      if (typeof window !== "undefined") {
        window.localStorage.setItem("auth_token", response.access_token);
        window.localStorage.setItem("auth_token_type", response.token_type);
      }

      router.replace("/");
    } catch (error) {
      console.error("Error login:", error);
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
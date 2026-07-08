"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

import { LoginForm } from "@/shared/components/auth/login-form";

import { useAuthStore } from "@/features/auth/store/auth.store";

export default function LoginPage() {
  const router = useRouter();

  const token =
    useAuthStore(
      (state) => state.token
    );

  return (
    <div className="flex min-h-screen items-center justify-center bg-zinc-100">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-lg">

        <h1 className="text-3xl font-bold">
          AbogacIA
        </h1>

        <p className="mt-2 text-zinc-500">
          Accede a tu plataforma legal
        </p>

        <div className="mt-8">
          <LoginForm />
        </div>

      </div>
    </div>
  );
}
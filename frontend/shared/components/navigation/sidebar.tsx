"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

const menuItems = [
  {
    title: "Dashboard",
    href: "/",
  },
  {
    title: "Clientes",
    href: "/clients",
  },
  {
    title: "Calendario",
    href: "/calendar",
  },
  {
    title: "Recordatorios",
    href: "/reminders",
  },
  {
    title: "Plantillas",
    href: "/templates",
  },
  {
    title: "Email",
    href: "/email",
  },
  {
    title: "Configuración",
    href: "/settings",
  },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="fixed left-0 top-0 flex h-screen w-64 flex-col border-r bg-zinc-950 p-4 text-white">      <div className="mb-10">
        <h2 className="text-3xl font-bold">
          AbogacIA
        </h2>

        <p className="text-sm text-zinc-400">
          Legal AI Platform
        </p>
      </div>

      <nav className="flex flex-col gap-2">
        {menuItems.map((item) => (
          <Link
            key={item.href}
            href={item.href}
            className={`rounded-xl px-4 py-3 text-left transition hover:bg-zinc-800 ${
              pathname === item.href
                ? "bg-zinc-800"
                : ""
            }`}
          >
            {item.title}
          </Link>
        ))}
      </nav>

      <div className="mt-auto rounded-xl bg-zinc-900 p-4">
        <p className="text-sm text-zinc-400">
          Usuario conectado
        </p>

        <p className="mt-1 font-medium">
          Josep
        </p>
      </div>
    </aside>
  );
}
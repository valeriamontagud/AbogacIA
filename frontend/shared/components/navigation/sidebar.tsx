export function Sidebar() {
  return (
    <aside className="flex h-screen w-64 flex-col border-r bg-zinc-950 p-4 text-white">
      <h2 className="mb-8 text-2xl font-bold">
        AbogacIA
      </h2>

      <nav className="flex flex-col gap-2">
        <button className="rounded-lg px-4 py-2 text-left hover:bg-zinc-800">
          Dashboard
        </button>

        <button className="rounded-lg px-4 py-2 text-left hover:bg-zinc-800">
          Clientes
        </button>

        <button className="rounded-lg px-4 py-2 text-left hover:bg-zinc-800">
          Documentos
        </button>

        <button className="rounded-lg px-4 py-2 text-left hover:bg-zinc-800">
          Recordatorios
        </button>

        <button className="rounded-lg px-4 py-2 text-left hover:bg-zinc-800">
          IA Jurídica
        </button>
      </nav>
    </aside>
  );
}
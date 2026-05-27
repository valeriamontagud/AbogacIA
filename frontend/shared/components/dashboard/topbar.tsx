export function Topbar() {
  return (
    <header className="mb-6 flex items-center justify-between">
      <div>
        <h1 className="text-3xl font-bold">
          Dashboard
        </h1>

        <p className="text-zinc-500">
          Bienvenido a AbogacIA
        </p>
      </div>

      <div className="flex items-center gap-4">
        <input
          placeholder="Buscar..."
          className="rounded-xl border bg-white px-4 py-2 outline-none"
        />

        <div className="flex h-10 w-10 items-center justify-center rounded-full bg-black text-white">
          J
        </div>
      </div>
    </header>
  );
}
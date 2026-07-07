interface DocumentCardProps {
  title: string;
}

export function DocumentCard({
  title,
}: DocumentCardProps) {
  return (
    <div className="rounded-xl border bg-zinc-50 p-5">

      <h3 className="font-semibold">
        {title}
      </h3>

      <p className="mt-4 text-sm text-red-600">
        Pendiente
      </p>

      <button className="mt-5 rounded-lg border bg-white px-4 py-2 text-sm hover:bg-zinc-100">
        Subir documento
      </button>

    </div>
  );
}
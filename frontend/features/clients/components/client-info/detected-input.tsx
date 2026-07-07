interface DetectedInputProps {
  label: string;
}

export function DetectedInput({
  label,
}: DetectedInputProps) {
  return (
    <div>

      <label className="mb-2 block text-sm font-medium">
        {label}
      </label>

      <input
        className="w-full rounded-lg border bg-zinc-50 px-4 py-3"
        placeholder="Pendiente de analizar"
      />

      <p className="mt-2 text-xs text-zinc-500">
        La IA completará este dato automáticamente.
      </p>

    </div>
  );
}
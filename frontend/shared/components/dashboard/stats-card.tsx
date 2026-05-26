interface StatsCardProps {
  title: string;
  value: string;
}

export function StatsCard({
  title,
  value,
}: StatsCardProps) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm">
      <p className="text-sm text-zinc-500">
        {title}
      </p>

      <h2 className="mt-2 text-3xl font-bold">
        {value}
      </h2>
    </div>
  );
}
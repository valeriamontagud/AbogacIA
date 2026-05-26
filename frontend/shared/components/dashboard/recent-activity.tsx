const activities = [
  "Nuevo cliente añadido",
  "Documento subido",
  "Recordatorio creado",
  "Email recibido",
];

export function RecentActivity() {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm">
      <h2 className="mb-4 text-xl font-bold">
        Actividad reciente
      </h2>

      <div className="space-y-3">
        {activities.map((activity) => (
          <div
            key={activity}
            className="rounded-xl bg-zinc-100 p-3"
          >
            {activity}
          </div>
        ))}
      </div>
    </div>
  );
}
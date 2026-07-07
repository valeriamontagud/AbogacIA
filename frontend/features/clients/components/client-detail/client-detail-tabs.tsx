// ======================================================
// Client Detail Tabs
// ======================================================

interface ClientDetailTabsProps {
  activeTab: string;
  onChange: (tab: string) => void;
}

const tabs = [
  {
    id: "info",
    label: "Ficha",
  },
  {
    id: "opening",
    label: "Apertura",
  },
  {
    id: "processing",
    label: "Tramitación",
  },
  {
    id: "judicial",
    label: "Judicial",
  },
  {
    id: "accounting",
    label: "Contabilidad",
  },
];

export function ClientDetailTabs({
  activeTab,
  onChange,
}: ClientDetailTabsProps) {
  return (
    <div className="border-b">

      <nav className="flex gap-8">

        {tabs.map((tab) => (

          <button
            key={tab.id}
            onClick={() => onChange(tab.id)}
            className={`pb-3 text-sm font-medium ${
              activeTab === tab.id
                ? "border-b-2 border-black"
                : "text-zinc-500"
            }`}
          >
            {tab.label}
          </button>

        ))}

      </nav>

    </div>
  );
}
// ======================================================
// Client Detail Body
// ======================================================

import { ClientInfoTab } from "../client-info/client-info-tab";
import { OpeningTab } from "../opening/opening-tab";
import { ProcessingTab } from "../processing/processing-tab";
import { JudicialTab } from "../judicial/judicial-tab";
import { AccountingTab } from "../accounting/accounting-tab";

interface ClientDetailBodyProps {
  activeTab: string;
}

export function ClientDetailBody({
  activeTab,
}: ClientDetailBodyProps) {
  return (
    <div className="mt-8">

      {activeTab === "info" && <ClientInfoTab />}

      {activeTab === "opening" && <OpeningTab />}

      {activeTab === "processing" && <ProcessingTab />}

      {activeTab === "judicial" && <JudicialTab />}

      {activeTab === "accounting" && <AccountingTab />}

    </div>
  );
}
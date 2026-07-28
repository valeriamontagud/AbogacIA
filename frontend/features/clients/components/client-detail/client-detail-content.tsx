"use client";

// ======================================================
// Client Detail Content
// ======================================================

import { useState } from "react";

import { ClientDetailHeader } from "./client-detail-header";
import { ClientDetailTabs } from "./client-detail-tabs";
import { ClientDetailBody } from "./client-detail-body";
import { ClientDetailView } from "../../types/client.view";

interface ClientDetailContentProps {
  client: ClientDetailView;
}

export function ClientDetailContent({
  client,
}: ClientDetailContentProps) {
  const [activeTab, setActiveTab] = useState("info");

  return (
    <>
      <ClientDetailHeader client={client} />

      <ClientDetailTabs
        activeTab={activeTab}
        onChange={setActiveTab}
      />

      <ClientDetailBody
        activeTab={activeTab}
      />
    </>
  );
}
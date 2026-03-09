"use client";

import { useEffect, useState, useMemo } from "react";
import DashboardLayout from "@/components/DashboardLayout";
import EditableTable, { Column } from "@/components/EditableTable";
import { inventoryApi, optionsApi, InventoryItem } from "@/lib/api";

export default function InventoryPage() {
  const [inventory, setInventory] = useState<InventoryItem[]>([]);
  const [locations, setLocations] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const columns: Column<InventoryItem>[] = useMemo(() => [
    { key: "id", header: "ID", type: "number", editable: false, width: "80px" },
    { key: "product_name", header: "Product", type: "string", editable: false },
    { key: "quantity", header: "Quantity", type: "number", width: "120px" },
    { key: "min_quantity", header: "Min Qty", type: "number", width: "100px" },
    { key: "location", header: "Location", type: "select", options: locations },
  ], [locations]);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const [inventoryData, locationsData] = await Promise.all([
        inventoryApi.getAll(),
        optionsApi.getLocations(),
      ]);
      // Sort by ID to maintain consistent order
      setInventory(inventoryData.sort((a, b) => a.id - b.id));
      setLocations(locationsData);
    } catch (err) {
      setError("Failed to load inventory");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSave = async (changes: Map<string, unknown>) => {
    // Group changes by inventory ID
    const inventoryChanges = new Map<number, Partial<InventoryItem>>();
    
    changes.forEach((value, cellKey) => {
      // cellKey format: "inventory-{id}-{field}"
      const parts = cellKey.split("-");
      const inventoryId = parseInt(parts[1]);
      const field = parts[2] as keyof InventoryItem;
      
      if (!inventoryChanges.has(inventoryId)) {
        inventoryChanges.set(inventoryId, { id: inventoryId });
      }
      inventoryChanges.get(inventoryId)![field] = value as never;
    });

    // Convert to array for bulk update
    const updates = Array.from(inventoryChanges.values());
    await inventoryApi.bulkUpdate(updates);
    
    // Refresh data
    await fetchData();
  };

  if (isLoading) {
    return (
      <DashboardLayout>
        <div className="p-6">
          <div className="animate-pulse space-y-4">
            <div className="h-8 bg-gray-200 rounded w-48"></div>
            <div className="h-64 bg-gray-200 rounded"></div>
          </div>
        </div>
      </DashboardLayout>
    );
  }

  if (error) {
    return (
      <DashboardLayout>
        <div className="p-6">
          <div className="bg-red-50 text-red-700 p-4 rounded-lg" data-testid="error-message">
            {error}
            <button
              onClick={fetchData}
              className="ml-4 underline hover:no-underline"
            >
              Retry
            </button>
          </div>
        </div>
      </DashboardLayout>
    );
  }

  return (
    <DashboardLayout>
      <div className="p-6">
        <div className="mb-6">
          <h1 className="text-2xl font-bold text-gray-800" data-testid="page-title">
            Inventory
          </h1>
          <p className="text-gray-600 mt-1">
            Track and manage inventory levels. Click cells to select, double-click to edit.
          </p>
        </div>

        <EditableTable<InventoryItem>
          data={inventory}
          columns={columns}
          onSave={handleSave}
          tableName="inventory"
        />

        {/* Low stock warning */}
        {inventory.some((item) => item.quantity < item.min_quantity) && (
          <div
            className="mt-4 p-4 bg-yellow-50 border border-yellow-200 rounded-lg"
            data-testid="low-stock-warning"
          >
            <h3 className="font-medium text-yellow-800">⚠️ Low Stock Alert</h3>
            <p className="text-sm text-yellow-700 mt-1">
              Some items are below minimum quantity. Consider restocking soon.
            </p>
          </div>
        )}
      </div>
    </DashboardLayout>
  );
}

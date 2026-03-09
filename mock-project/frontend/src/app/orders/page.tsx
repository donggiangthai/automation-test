"use client";

import { useEffect, useState, useMemo } from "react";
import DashboardLayout from "@/components/DashboardLayout";
import EditableTable, { Column } from "@/components/EditableTable";
import { ordersApi, optionsApi, Order } from "@/lib/api";

const statusColors: Record<string, string> = {
  pending: "bg-yellow-100 text-yellow-800",
  processing: "bg-blue-100 text-blue-800",
  shipped: "bg-purple-100 text-purple-800",
  delivered: "bg-green-100 text-green-800",
  cancelled: "bg-red-100 text-red-800",
};

export default function OrdersPage() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [orderStatuses, setOrderStatuses] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [statusFilter, setStatusFilter] = useState<string>("all");

  const columns: Column<Order>[] = useMemo(() => [
    { key: "id", header: "Order ID", type: "number", editable: false, width: "100px" },
    { key: "customer_name", header: "Customer", type: "string" },
    { key: "customer_email", header: "Email", type: "string" },
    { key: "status", header: "Status", type: "select", options: orderStatuses },
    { key: "quantity", header: "Qty", type: "number", width: "80px" },
    { key: "total_amount", header: "Total ($)", type: "number", width: "120px" },
    { key: "notes", header: "Notes", type: "string" },
  ], [orderStatuses]);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const [ordersData, statusesData] = await Promise.all([
        ordersApi.getAll(),
        optionsApi.getOrderStatuses(),
      ]);
      // Sort by ID to maintain consistent order
      setOrders(ordersData.sort((a, b) => a.id - b.id));
      setOrderStatuses(statusesData);
    } catch (err) {
      setError("Failed to load orders");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSave = async (changes: Map<string, unknown>) => {
    // Group changes by order ID
    const orderChanges = new Map<number, Partial<Order>>();
    
    changes.forEach((value, cellKey) => {
      // cellKey format: "orders-{id}-{field}"
      const parts = cellKey.split("-");
      const orderId = parseInt(parts[1]);
      const field = parts[2] as keyof Order;
      
      if (!orderChanges.has(orderId)) {
        orderChanges.set(orderId, { id: orderId });
      }
      orderChanges.get(orderId)![field] = value as never;
    });

    // Convert to array for bulk update
    const updates = Array.from(orderChanges.values());
    await ordersApi.bulkUpdate(updates);
    
    // Refresh data
    await fetchData();
  };

  const filteredOrders =
    statusFilter === "all"
      ? orders
      : orders.filter((order) => order.status === statusFilter);

  const uniqueStatuses = Array.from(new Set(orders.map((o) => o.status)));

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
        <div className="mb-6 flex items-start justify-between">
          <div>
            <h1 className="text-2xl font-bold text-gray-800" data-testid="page-title">
              Orders
            </h1>
            <p className="text-gray-600 mt-1">
              Manage customer orders. Click cells to select, double-click to edit.
            </p>
          </div>

          {/* Status filter */}
          <div className="flex items-center gap-2">
            <label htmlFor="status-filter" className="text-sm text-gray-600">
              Filter by status:
            </label>
            <select
              id="status-filter"
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              data-testid="status-filter"
              className="px-3 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="all">All Orders</option>
              {uniqueStatuses.map((status) => (
                <option key={status} value={status}>
                  {status.charAt(0).toUpperCase() + status.slice(1)}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Status summary */}
        <div className="mb-4 flex gap-2 flex-wrap">
          {uniqueStatuses.map((status) => {
            const count = orders.filter((o) => o.status === status).length;
            return (
              <span
                key={status}
                data-testid={`status-badge-${status}`}
                className={`px-3 py-1 rounded-full text-xs font-medium ${
                  statusColors[status] || "bg-gray-100 text-gray-800"
                }`}
              >
                {status}: {count}
              </span>
            );
          })}
        </div>

        <EditableTable<Order>
          data={filteredOrders}
          columns={columns}
          onSave={handleSave}
          tableName="orders"
        />
      </div>
    </DashboardLayout>
  );
}

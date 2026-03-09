"use client";

import { useEffect, useState, useMemo } from "react";
import DashboardLayout from "@/components/DashboardLayout";
import EditableTable, { Column } from "@/components/EditableTable";
import { productsApi, optionsApi, Product } from "@/lib/api";

export default function ProductsPage() {
  const [products, setProducts] = useState<Product[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const columns: Column<Product>[] = useMemo(() => [
    { key: "id", header: "ID", type: "number", editable: false, width: "80px" },
    { key: "name", header: "Product Name", type: "string" },
    { key: "price", header: "Price ($)", type: "number", width: "120px", step: "0.01" },
    { key: "category", header: "Category", type: "select", options: categories },
    { key: "description", header: "Description", type: "string" },
  ], [categories]);

  const fetchData = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const [productsData, categoriesData] = await Promise.all([
        productsApi.getAll(),
        optionsApi.getCategories(),
      ]);
      // Sort by ID to maintain consistent order
      setProducts(productsData.sort((a, b) => a.id - b.id));
      setCategories(categoriesData);
    } catch (err) {
      setError("Failed to load products");
      console.error(err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSave = async (changes: Map<string, unknown>) => {
    // Group changes by product ID
    const productChanges = new Map<number, Partial<Product>>();
    
    changes.forEach((value, cellKey) => {
      // cellKey format: "products-{id}-{field}"
      const parts = cellKey.split("-");
      const productId = parseInt(parts[1]);
      const field = parts[2] as keyof Product;
      
      if (!productChanges.has(productId)) {
        productChanges.set(productId, { id: productId });
      }
      productChanges.get(productId)![field] = value as never;
    });

    // Convert to array for bulk update
    const updates = Array.from(productChanges.values());
    await productsApi.bulkUpdate(updates);
    
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
            Products
          </h1>
          <p className="text-gray-600 mt-1">
            Manage your product catalog. Click cells to select, double-click to edit.
          </p>
        </div>

        <EditableTable<Product>
          data={products}
          columns={columns}
          onSave={handleSave}
          tableName="products"
        />
      </div>
    </DashboardLayout>
  );
}

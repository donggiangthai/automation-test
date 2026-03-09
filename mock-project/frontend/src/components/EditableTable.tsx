"use client";

import { useState, useCallback, useEffect } from "react";
import { useAppStore } from "@/store/appStore";

export interface Column<T> {
  key: keyof T;
  header: string;
  type: "string" | "number" | "select";
  editable?: boolean;
  width?: string;
  step?: string;
  options?: string[];
}

interface EditableTableProps<T extends { id: number }> {
  data: T[];
  columns: Column<T>[];
  onSave: (changes: Map<string, unknown>) => Promise<void>;
  tableName: string;
}

export default function EditableTable<T extends { id: number }>({
  data,
  columns,
  onSave,
  tableName,
}: EditableTableProps<T>) {
  const {
    selectedCells,
    pendingChanges,
    addSelectedCell,
    removeSelectedCell,
    clearSelectedCells,
    addPendingChange,
    clearPendingChanges,
  } = useAppStore();

  const [editingCell, setEditingCell] = useState<string | null>(null);
  const [editValue, setEditValue] = useState<string>("");
  const [isSaving, setIsSaving] = useState(false);

  const getCellKey = (rowId: number, colKey: keyof T) => {
    return `${tableName}-${rowId}-${String(colKey)}`;
  };

  const handleCellClick = useCallback(
    (e: React.MouseEvent, rowId: number, colKey: keyof T) => {
      const cellKey = getCellKey(rowId, colKey);
      const isMultiSelect = e.ctrlKey || e.metaKey;

      if (isMultiSelect) {
        if (selectedCells.has(cellKey)) {
          removeSelectedCell(cellKey);
        } else {
          addSelectedCell(cellKey);
        }
      } else {
        clearSelectedCells();
        addSelectedCell(cellKey);
      }
    },
    [selectedCells, addSelectedCell, removeSelectedCell, clearSelectedCells, tableName]
  );

  const handleDoubleClick = useCallback(
    (rowId: number, colKey: keyof T, currentValue: unknown) => {
      const cellKey = getCellKey(rowId, colKey);
      setEditingCell(cellKey);
      setEditValue(String(currentValue));
    },
    [tableName]
  );

  const handleEditChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setEditValue(e.target.value);
  };

  const handleEditBlur = useCallback(
    (rowId: number, colKey: keyof T, column: Column<T>) => {
      const cellKey = getCellKey(rowId, colKey);
      const parsedValue = column.type === "number" ? parseFloat(editValue) || 0 : editValue;
      const row = data.find(r => r.id === rowId);
      const originalValue = row ? row[colKey] : null;
      
      // Only add change if value actually changed
      if (parsedValue === originalValue || String(parsedValue) === String(originalValue)) {
        setEditingCell(null);
        return;
      }
      
      // Apply change to all selected cells if this cell is selected
      if (selectedCells.has(cellKey)) {
        selectedCells.forEach((selectedKey) => {
          const [, selRowId, selField] = selectedKey.split('-');
          addPendingChange(selectedKey, { rowId: parseInt(selRowId), field: selField, value: parsedValue, originalValue });
        });
      } else {
        const [, , field] = cellKey.split('-');
        addPendingChange(cellKey, { rowId, field, value: parsedValue, originalValue });
      }
      
      setEditingCell(null);
    },
    [editValue, selectedCells, addPendingChange, tableName, data]
  );

  const handleEditKeyDown = useCallback(
    (e: React.KeyboardEvent, rowId: number, colKey: keyof T, column: Column<T>) => {
      if (e.key === "Enter") {
        handleEditBlur(rowId, colKey, column);
      } else if (e.key === "Escape") {
        setEditingCell(null);
      }
    },
    [handleEditBlur]
  );

  const handleSave = async () => {
    if (pendingChanges.size === 0) return;
    
    setIsSaving(true);
    try {
      // Convert pendingChanges to the format expected by onSave
      const changesMap = new Map<string, unknown>();
      pendingChanges.forEach((change, key) => {
        changesMap.set(key, change.value);
      });
      await onSave(changesMap);
      clearPendingChanges();
      clearSelectedCells();
    } catch (error) {
      console.error("Failed to save changes:", error);
      alert("Failed to save changes. Please try again.");
    } finally {
      setIsSaving(false);
    }
  };

  const handleReset = () => {
    clearPendingChanges();
    clearSelectedCells();
    setEditingCell(null);
  };

  const getCellValue = (rowId: number, colKey: keyof T, originalValue: unknown) => {
    const cellKey = getCellKey(rowId, colKey);
    const change = pendingChanges.get(cellKey);
    if (change) {
      return change.value;
    }
    return originalValue;
  };

  const isCellModified = (rowId: number, colKey: keyof T) => {
    const cellKey = getCellKey(rowId, colKey);
    return pendingChanges.has(cellKey);
  };

  const isCellSelected = (rowId: number, colKey: keyof T) => {
    const cellKey = getCellKey(rowId, colKey);
    return selectedCells.has(cellKey);
  };

  // Clear selection when clicking outside table
  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      const target = e.target as HTMLElement;
      if (!target.closest("[data-table-cell]") && !target.closest("[data-action-button]")) {
        // Don't clear if clicking action buttons
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  return (
    <div className="bg-white rounded-lg shadow">
      {/* Action buttons */}
      <div className="p-4 border-b flex items-center justify-between">
        <div className="text-sm text-gray-600">
          {selectedCells.size > 0 && (
            <span data-testid="selected-count">
              {selectedCells.size} cell(s) selected
            </span>
          )}
          {pendingChanges.size > 0 && (
            <span className="ml-4 text-orange-600" data-testid="pending-count">
              {pendingChanges.size} pending change(s)
            </span>
          )}
        </div>
        
        <div className="flex gap-2">
          <button
            onClick={handleReset}
            disabled={pendingChanges.size === 0}
            data-testid="reset-button"
            data-action-button
            className="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-lg hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            Reset
          </button>
          <button
            onClick={handleSave}
            disabled={pendingChanges.size === 0 || isSaving}
            data-testid="save-button"
            data-action-button
            className="px-4 py-2 text-sm font-medium text-white bg-blue-600 rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
          >
            {isSaving ? "Saving..." : "Save Changes"}
          </button>
        </div>
      </div>

      {/* Table */}
      <div className="overflow-x-auto">
        <table className="w-full" data-testid={`${tableName}-table`}>
          <thead className="bg-gray-50">
            <tr>
              {columns.map((column) => (
                <th
                  key={String(column.key)}
                  data-testid={`header-${String(column.key)}`}
                  className="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                  style={{ width: column.width }}
                >
                  {column.header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-gray-200">
            {data.map((row) => (
              <tr key={row.id} data-testid={`row-${row.id}`}>
                {columns.map((column) => {
                  const cellKey = getCellKey(row.id, column.key);
                  const value = getCellValue(row.id, column.key, row[column.key]);
                  const isEditing = editingCell === cellKey;
                  const isSelected = isCellSelected(row.id, column.key);
                  const isModified = isCellModified(row.id, column.key);
                  const isEditable = column.editable !== false;

                  return (
                    <td
                      key={String(column.key)}
                      data-testid={`cell-${row.id}-${String(column.key)}`}
                      data-table-cell
                      onClick={(e) => isEditable && handleCellClick(e, row.id, column.key)}
                      onDoubleClick={() =>
                        isEditable && handleDoubleClick(row.id, column.key, value)
                      }
                      className={`px-4 py-3 text-sm ${
                        isEditable ? "cursor-pointer" : "cursor-default"
                      } ${isSelected ? "bg-blue-100 ring-2 ring-blue-500 ring-inset" : ""} ${
                        isModified ? "bg-yellow-50" : ""
                      } ${isSelected && isModified ? "bg-orange-100" : ""}`}
                    >
                      {isEditing ? (
                        column.type === "select" && column.options ? (
                          <select
                            value={editValue}
                            onChange={(e) => {
                              setEditValue(e.target.value);
                            }}
                            onBlur={() => handleEditBlur(row.id, column.key, column)}
                            onKeyDown={(e) => handleEditKeyDown(e, row.id, column.key, column)}
                            autoFocus
                            data-testid={`select-${row.id}-${String(column.key)}`}
                            className="w-full px-2 py-1 border border-blue-500 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                          >
                            {column.options.map((option) => (
                              <option key={option} value={option}>
                                {option}
                              </option>
                            ))}
                          </select>
                        ) : (
                          <input
                            type={column.type === "number" ? "number" : "text"}
                            step={column.step}
                            value={editValue}
                            onChange={handleEditChange}
                            onBlur={() => handleEditBlur(row.id, column.key, column)}
                            onKeyDown={(e) => handleEditKeyDown(e, row.id, column.key, column)}
                            autoFocus
                            data-testid={`input-${row.id}-${String(column.key)}`}
                            className="w-full px-2 py-1 border border-blue-500 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                          />
                        )
                      ) : (
                        <span
                          className={isModified ? "font-medium text-orange-700" : ""}
                          data-testid={`value-${row.id}-${String(column.key)}`}
                        >
                          {String(value)}
                        </span>
                      )}
                    </td>
                  );
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Empty state */}
      {data.length === 0 && (
        <div className="p-8 text-center text-gray-500" data-testid="empty-state">
          No data available
        </div>
      )}

      {/* Instructions */}
      <div className="p-4 border-t bg-gray-50 text-xs text-gray-500">
        <p>
          <strong>Tips:</strong> Click to select • Double-click to edit •{" "}
          <kbd className="px-1.5 py-0.5 bg-gray-200 rounded">Ctrl</kbd>/
          <kbd className="px-1.5 py-0.5 bg-gray-200 rounded">Cmd</kbd> + Click to multi-select • 
          <strong className="ml-1">Bulk edit:</strong> Multi-select → double-click any selected cell → edit → value applies to all
        </p>
      </div>
    </div>
  );
}

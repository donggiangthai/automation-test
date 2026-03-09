import { create } from 'zustand';

interface AppState {
  // Sidebar
  isSidebarCollapsed: boolean;
  toggleSidebar: () => void;
  
  // Selected cells for multi-edit
  selectedCells: Set<string>; // Format: "rowId-columnId"
  addSelectedCell: (cellId: string) => void;
  removeSelectedCell: (cellId: string) => void;
  toggleSelectedCell: (cellId: string, isMultiSelect: boolean) => void;
  clearSelectedCells: () => void;
  
  // Pending changes
  pendingChanges: Map<string, { rowId: number; field: string; value: any; originalValue: any }>;
  addPendingChange: (key: string, change: { rowId: number; field: string; value: any; originalValue: any }) => void;
  removePendingChange: (key: string) => void;
  clearPendingChanges: () => void;
  hasPendingChanges: () => boolean;
}

export const useAppStore = create<AppState>((set, get) => ({
  // Sidebar state
  isSidebarCollapsed: false,
  toggleSidebar: () => set((state) => ({ isSidebarCollapsed: !state.isSidebarCollapsed })),
  
  // Selected cells
  selectedCells: new Set<string>(),
  
  addSelectedCell: (cellId: string) => {
    set((state) => {
      const newSet = new Set(state.selectedCells);
      newSet.add(cellId);
      return { selectedCells: newSet };
    });
  },
  
  removeSelectedCell: (cellId: string) => {
    set((state) => {
      const newSet = new Set(state.selectedCells);
      newSet.delete(cellId);
      return { selectedCells: newSet };
    });
  },
  
  toggleSelectedCell: (cellId: string, isMultiSelect: boolean) => {
    set((state) => {
      const newSet = isMultiSelect ? new Set(state.selectedCells) : new Set<string>();
      
      if (newSet.has(cellId)) {
        newSet.delete(cellId);
      } else {
        newSet.add(cellId);
      }
      
      return { selectedCells: newSet };
    });
  },
  
  clearSelectedCells: () => set({ selectedCells: new Set<string>() }),
  
  // Pending changes
  pendingChanges: new Map(),
  
  addPendingChange: (key: string, change) => {
    set((state) => {
      const newMap = new Map(state.pendingChanges);
      newMap.set(key, change);
      return { pendingChanges: newMap };
    });
  },
  
  removePendingChange: (key: string) => {
    set((state) => {
      const newMap = new Map(state.pendingChanges);
      newMap.delete(key);
      return { pendingChanges: newMap };
    });
  },
  
  clearPendingChanges: () => set({ pendingChanges: new Map() }),
  
  hasPendingChanges: () => get().pendingChanges.size > 0,
}));

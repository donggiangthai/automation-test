"use client";

import { useEffect } from "react";
import { useRouter, usePathname } from "next/navigation";
import Link from "next/link";
import { useAuthStore } from "@/store/authStore";
import { useAppStore } from "@/store/appStore";
import {
  Package,
  Warehouse,
  ShoppingCart,
  ChevronLeft,
  ChevronRight,
  LogOut,
  User,
} from "lucide-react";

interface DashboardLayoutProps {
  children: React.ReactNode;
}

const navItems = [
  { href: "/products", label: "Products", icon: Package },
  { href: "/inventory", label: "Inventory", icon: Warehouse },
  { href: "/orders", label: "Orders", icon: ShoppingCart },
];

export default function DashboardLayout({ children }: DashboardLayoutProps) {
  const router = useRouter();
  const pathname = usePathname();
  const { user, isAuthenticated, checkAuth, logout } = useAuthStore();
  const { isSidebarCollapsed, toggleSidebar } = useAppStore();

  useEffect(() => {
    checkAuth();
  }, [checkAuth]);

  useEffect(() => {
    if (!isAuthenticated) {
      router.push("/login");
    }
  }, [isAuthenticated, router]);

  const handleLogout = () => {
    logout();
    router.push("/login");
  };

  if (!isAuthenticated) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen flex bg-gray-100">
      {/* Sidebar */}
      <aside
        data-testid="sidebar"
        className={`sidebar ${isSidebarCollapsed ? "collapsed" : "expanded"} bg-white shadow-lg flex flex-col`}
      >
        {/* Logo */}
        <div className="p-4 border-b flex items-center justify-between">
          {!isSidebarCollapsed && (
            <span className="font-bold text-xl text-gray-800" data-testid="app-logo">
              DataMgmt
            </span>
          )}
          <button
            onClick={toggleSidebar}
            data-testid="sidebar-toggle"
            className="p-2 rounded-lg hover:bg-gray-100 transition-colors"
            aria-label={isSidebarCollapsed ? "Expand sidebar" : "Collapse sidebar"}
          >
            {isSidebarCollapsed ? (
              <ChevronRight className="w-5 h-5 text-gray-600" />
            ) : (
              <ChevronLeft className="w-5 h-5 text-gray-600" />
            )}
          </button>
        </div>

        {/* Navigation */}
        <nav className="flex-1 p-4">
          <ul className="space-y-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = pathname === item.href;
              
              return (
                <li key={item.href}>
                  <Link
                    href={item.href}
                    data-testid={`nav-${item.label.toLowerCase()}`}
                    className={`flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${
                      isActive
                        ? "bg-blue-100 text-blue-700"
                        : "text-gray-600 hover:bg-gray-100"
                    }`}
                  >
                    <Icon className="w-5 h-5 flex-shrink-0" />
                    {!isSidebarCollapsed && (
                      <span className="font-medium">{item.label}</span>
                    )}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>

        {/* User section */}
        <div className="p-4 border-t">
          <div className="flex items-center gap-3 mb-3">
            <div className="w-8 h-8 rounded-full bg-gray-200 flex items-center justify-center flex-shrink-0">
              <User className="w-4 h-4 text-gray-600" />
            </div>
            {!isSidebarCollapsed && (
              <div className="overflow-hidden">
                <p className="text-sm font-medium text-gray-800 truncate" data-testid="user-name">
                  {user?.name || "User"}
                </p>
                <p className="text-xs text-gray-500 truncate" data-testid="user-email">
                  {user?.email}
                </p>
              </div>
            )}
          </div>
          
          <button
            onClick={handleLogout}
            data-testid="logout-button"
            className={`flex items-center gap-3 px-3 py-2 rounded-lg text-red-600 hover:bg-red-50 transition-colors w-full ${
              isSidebarCollapsed ? "justify-center" : ""
            }`}
          >
            <LogOut className="w-5 h-5 flex-shrink-0" />
            {!isSidebarCollapsed && <span className="font-medium">Logout</span>}
          </button>
        </div>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-auto">
        {children}
      </main>
    </div>
  );
}

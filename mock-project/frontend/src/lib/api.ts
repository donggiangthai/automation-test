import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Types
export interface Product {
  id: number;
  name: string;
  description: string | null;
  price: number;
  category: string | null;
  created_at: string;
  updated_at: string | null;
}

export interface InventoryItem {
  id: number;
  product_id: number;
  product_name: string | null;
  quantity: number;
  min_quantity: number;
  location: string | null;
  updated_at: string | null;
}

export interface Order {
  id: number;
  customer_name: string;
  customer_email: string;
  product_id: number;
  product_name?: string | null;
  quantity: number;
  total_amount: number;
  status: string;
  notes: string | null;
  created_at: string;
  updated_at: string | null;
}

// Request interceptor to add auth token
api.interceptors.request.use(
  (config) => {
    // Token is set by authStore
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor to handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Handle unauthorized - redirect to login
      if (typeof window !== 'undefined') {
        localStorage.removeItem('auth-storage');
        window.location.href = '/login';
      }
    }
    return Promise.reject(error);
  }
);

// API functions
export const productsApi = {
  getAll: async (): Promise<Product[]> => {
    const response = await api.get('/api/products');
    return response.data;
  },
  get: async (id: number): Promise<Product> => {
    const response = await api.get(`/api/products/${id}`);
    return response.data;
  },
  update: async (id: number, data: Partial<Product>): Promise<Product> => {
    const response = await api.put(`/api/products/${id}`, data);
    return response.data;
  },
  bulkUpdate: async (items: Partial<Product>[]): Promise<void> => {
    await api.patch('/api/products/bulk', items);
  },
};

export const inventoryApi = {
  getAll: async (): Promise<InventoryItem[]> => {
    const response = await api.get('/api/inventory');
    return response.data;
  },
  get: async (id: number): Promise<InventoryItem> => {
    const response = await api.get(`/api/inventory/${id}`);
    return response.data;
  },
  update: async (id: number, data: Partial<InventoryItem>): Promise<InventoryItem> => {
    const response = await api.put(`/api/inventory/${id}`, data);
    return response.data;
  },
  bulkUpdate: async (items: Partial<InventoryItem>[]): Promise<void> => {
    await api.patch('/api/inventory/bulk', items);
  },
};

export const ordersApi = {
  getAll: async (): Promise<Order[]> => {
    const response = await api.get('/api/orders');
    return response.data;
  },
  get: async (id: number): Promise<Order> => {
    const response = await api.get(`/api/orders/${id}`);
    return response.data;
  },
  update: async (id: number, data: Partial<Order>): Promise<Order> => {
    const response = await api.put(`/api/orders/${id}`, data);
    return response.data;
  },
  bulkUpdate: async (items: Partial<Order>[]): Promise<void> => {
    await api.patch('/api/orders/bulk', items);
  },
};

export const authApi = {
  me: () => api.get('/auth/me'),
  logout: () => api.post('/auth/logout'),
  devToken: () => api.post('/auth/dev-token'),
};

// Options/Lookups API
export interface AllOptions {
  categories: string[];
  locations: string[];
  orderStatuses: string[];
}

export const optionsApi = {
  getCategories: async (): Promise<string[]> => {
    const response = await api.get('/api/options/categories');
    return response.data;
  },
  getLocations: async (): Promise<string[]> => {
    const response = await api.get('/api/options/locations');
    return response.data;
  },
  getOrderStatuses: async (): Promise<string[]> => {
    const response = await api.get('/api/options/order-statuses');
    return response.data;
  },
  getAll: async (): Promise<AllOptions> => {
    const response = await api.get('/api/options/all');
    return response.data;
  },
};

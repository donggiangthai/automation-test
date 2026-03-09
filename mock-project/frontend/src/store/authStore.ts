import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { api } from '@/lib/api';

interface User {
  id: number;
  email: string;
  name: string | null;
  picture: string | null;
}

interface AuthState {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  
  // Actions
  setToken: (token: string) => void;
  setUser: (user: User) => void;
  logout: () => void;
  checkAuth: () => Promise<void>;
  loginWithGoogle: () => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isAuthenticated: false,
      isLoading: false,

      setToken: (token: string) => {
        set({ token, isAuthenticated: true });
        // Set token in API client
        api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      },

      setUser: (user: User) => {
        set({ user });
      },

      logout: () => {
        set({ user: null, token: null, isAuthenticated: false });
        delete api.defaults.headers.common['Authorization'];
        localStorage.removeItem('auth-storage');
      },

      checkAuth: async () => {
        const { token } = get();
        if (!token) {
          set({ isAuthenticated: false });
          return;
        }

        try {
          set({ isLoading: true });
          api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
          const response = await api.get('/auth/me');
          set({ user: response.data, isAuthenticated: true });
        } catch (error) {
          set({ user: null, token: null, isAuthenticated: false });
          delete api.defaults.headers.common['Authorization'];
        } finally {
          set({ isLoading: false });
        }
      },

      loginWithGoogle: () => {
        const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
        window.location.href = `${apiUrl}/auth/google`;
      },
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({ token: state.token }),
    }
  )
);

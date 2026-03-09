"use client";

import { useEffect, Suspense } from "react";
import { useRouter, useSearchParams } from "next/navigation";
import { useAuthStore } from "@/store/authStore";

function AuthCallbackContent() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { setToken, checkAuth } = useAuthStore();

  useEffect(() => {
    const token = searchParams.get("token");
    const bypass = searchParams.get("bypass");

    if (token) {
      setToken(token);
      checkAuth().then(() => {
        router.push("/products");
      });
    } else if (bypass) {
      // Handle bypass mode - get dev token
      fetch(`${process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"}/auth/dev-token`, {
        method: "POST",
      })
        .then((res) => res.json())
        .then((data) => {
          setToken(data.access_token);
          router.push("/products");
        })
        .catch((error) => {
          console.error("Auth callback error:", error);
          router.push("/login");
        });
    } else {
      router.push("/login");
    }
  }, [searchParams, setToken, checkAuth, router]);

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
        <p className="mt-4 text-gray-600">Completing sign in...</p>
      </div>
    </div>
  );
}

export default function AuthCallbackPage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    }>
      <AuthCallbackContent />
    </Suspense>
  );
}

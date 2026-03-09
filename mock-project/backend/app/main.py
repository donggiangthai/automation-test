"""
Mock Project Backend - FastAPI Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from app.config import settings
from app.database import engine, Base
from app.routers import auth, products, inventory, orders, options
from app.seed import seed_database


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup and shutdown events"""
    # Startup: Create tables and seed data
    Base.metadata.create_all(bind=engine)
    seed_database()
    yield
    # Shutdown: cleanup if needed


app = FastAPI(
    title="Mock Data Management API",
    description="API for E2E testing practice",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        settings.FRONTEND_URL,
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(products.router, prefix="/api/products", tags=["Products"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["Inventory"])
app.include_router(orders.router, prefix="/api/orders", tags=["Orders"])
app.include_router(options.router, prefix="/api/options", tags=["Options"])


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Mock Data Management API",
        "docs": "/docs",
        "health": "/health"
    }

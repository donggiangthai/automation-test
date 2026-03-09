# ============================================================================
# Mock Project - Makefile for E2E Testing Training
# ============================================================================
#
# Prerequisites:
#   - Docker Desktop installed and running
#   - Python 3.12+
#   - Node.js 18+
#   - Poetry (will be installed automatically if missing)
#   - Make utility (Windows: choco install make)
#
# Quick Start:
#   make deps   - Install all dependencies
#   make dev    - Start application (includes DB setup & seed data)
#   make stop   - Stop all services
#   make logs   - View application logs
#
# ============================================================================

.PHONY: deps dev stop logs clean clean-deps clean-all reset help check-poetry check-pnpm config

# Default target
.DEFAULT_GOAL := help

# Detect OS
ifeq ($(OS),Windows_NT)
    DETECTED_OS := Windows
    SHELL := cmd.exe
    POETRY_CHECK := where poetry >nul 2>nul
    POETRY_INSTALL := powershell -Command "& {(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -}"
else
    DETECTED_OS := $(shell uname -s)
    POETRY_CHECK := command -v poetry >/dev/null 2>&1
    POETRY_INSTALL := curl -sSL https://install.python-poetry.org | python3 -
endif

# ============================================================================
# DEPENDENCY MANAGEMENT
# ============================================================================

## Check and install Poetry if needed
check-poetry:
	@echo "🔍 Checking for Poetry..."
ifeq ($(OS),Windows_NT)
	@where poetry >nul 2>nul || ( \
		echo "📦 Poetry not found. Installing..." && \
		powershell -Command "& {(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -}" && \
		echo "✅ Poetry installed!" && \
		echo "⚠️  Please restart your terminal, then run: make deps" \
	)
else
	@command -v poetry >/dev/null 2>&1 || ( \
		echo "📦 Poetry not found. Installing..." && \
		curl -sSL https://install.python-poetry.org | python3 - && \
		echo "✅ Poetry installed!" && \
		echo "⚠️  Please restart your terminal, then run: make deps" \
	)
endif
	@echo "✅ Poetry is ready"
	@echo "⚙️  Configuring Poetry to use in-project virtualenvs..."
	@poetry config virtualenvs.in-project true

## Check and install pnpm if needed
check-pnpm:
	@echo "🔍 Checking for pnpm..."
ifeq ($(OS),Windows_NT)
	@where pnpm >nul 2>nul || ( \
		echo "📦 pnpm not found. Installing via npm..." && \
		npm install -g pnpm && \
		echo "✅ pnpm installed!" \
	)
else
	@command -v pnpm >/dev/null 2>&1 || ( \
		echo "📦 pnpm not found. Installing..." && \
		curl -fsSL https://get.pnpm.io/install.sh | sh - && \
		echo "✅ pnpm installed!" && \
		echo "⚠️  Please restart your terminal if pnpm command not found" \
	)
endif
	@echo "✅ pnpm is ready"

# ============================================================================
# CONFIGURATION
# ============================================================================

## Create .env files from .env.example (safe - won't overwrite existing)
config:
	@echo "📝 Setting up environment files..."
ifeq ($(OS),Windows_NT)
	@if not exist backend\.env copy backend\.env.example backend\.env && echo "✅ Created backend/.env"
	@if not exist frontend\.env copy frontend\.env.example frontend\.env && echo "✅ Created frontend/.env"
else
	@if [ ! -f backend/.env ]; then cp backend/.env.example backend/.env && echo "✅ Created backend/.env"; else echo "⏭️  backend/.env already exists (skipped)"; fi
	@if [ ! -f frontend/.env ]; then cp frontend/.env.example frontend/.env && echo "✅ Created frontend/.env"; else echo "⏭️  frontend/.env already exists (skipped)"; fi
endif
	@echo "✅ Environment files ready!"

# ============================================================================
# MAIN COMMANDS
# ============================================================================

## Install all dependencies (backend + frontend + e2e)
deps: check-poetry check-pnpm config
	@echo ""
	@echo "📦 Installing backend dependencies..."
	cd backend && poetry install --no-interaction
	@echo ""
	@echo "📦 Installing frontend dependencies..."
	cd frontend && COREPACK_ENABLE_DOWNLOAD_PROMPT=0 pnpm install
	@echo ""
	@echo "📦 Installing E2E test dependencies..."
	cd e2e && poetry install --no-interaction
	@echo ""
	@echo "🎭 Installing Playwright browsers..."
	cd e2e && poetry run playwright install
	@echo ""
	@echo "✅ All dependencies installed!"

## Start development environment (DB + Backend + Frontend)
dev:
	@echo "🚀 Starting development environment..."
	@echo "   This will:"
	@echo "   - Start PostgreSQL database"
	@echo "   - Create database tables"
	@echo "   - Seed sample data"
	@echo "   - Start Backend API (http://localhost:8000)"
	@echo "   - Start Frontend UI (http://localhost:3000)"
	@echo ""
	docker compose up --build
	@echo ""
	@echo "✅ Application is running!"
	@echo "   Frontend: http://localhost:3000"
	@echo "   Backend:  http://localhost:8000"
	@echo "   API Docs: http://localhost:8000/docs"

## Start in background (detached mode)
dev-bg:
	@echo "🚀 Starting development environment in background..."
	docker compose up --build -d
	@echo ""
	@echo "✅ Application started in background!"
	@echo "   Frontend: http://localhost:3000"
	@echo "   Backend:  http://localhost:8000"
	@echo "   Use 'make logs' to view logs"
	@echo "   Use 'make stop' to stop services"

## Stop all services
stop:
	@echo "🛑 Stopping all services..."
	docker compose down
	@echo "✅ All services stopped!"

## View logs
logs:
	docker compose logs -f

## View backend logs only
logs-backend:
	docker compose logs -f backend

## View frontend logs only
logs-frontend:
	docker compose logs -f frontend

# ============================================================================
# UTILITY COMMANDS
# ============================================================================

## Reset database (remove all data)
reset:
	@echo "⚠️  This will delete all data!"
	@echo "    Press Ctrl+C to cancel, or wait 5 seconds to continue..."
ifeq ($(OS),Windows_NT)
	@timeout /t 5 /nobreak >nul
else
	@sleep 5
endif
	docker compose down -v
	@echo "✅ Database reset complete!"

## Clean up everything (containers, volumes, images)
clean:
	@echo "🧹 Cleaning up Docker resources..."
	docker compose down -v --rmi local
	@echo "✅ Docker cleanup complete!"

## Clean up all installed dependencies
clean-deps:
	@echo "🧹 Cleaning up installed dependencies..."
	@echo "   Removing backend/.venv..."
	rm -rf backend/.venv
	@echo "   Removing e2e/.venv..."
	rm -rf e2e/.venv
	@echo "   Removing frontend/node_modules..."
	rm -rf frontend/node_modules
	@echo "✅ All dependencies removed!"

## Clean up everything (Docker + dependencies)
clean-all: clean clean-deps
	@echo "✅ Full cleanup complete!"

## Rebuild containers (useful after Dockerfile changes)
rebuild:
	@echo "🔄 Rebuilding containers..."
	docker compose build --no-cache
	@echo "✅ Rebuild complete!"

# ============================================================================
# E2E TESTING COMMANDS
# ============================================================================

## Run E2E tests (headless)
test:
	@echo "🧪 Running E2E tests..."
	cd e2e && poetry run pytest tests/ -v

## Run E2E tests with browser visible
test-headed:
	@echo "🧪 Running E2E tests (headed mode)..."
	cd e2e && poetry run pytest tests/ -v --headed

## Run specific test file
test-file:
	@echo "🧪 Running specific test file..."
	@echo "    Usage: make test-file FILE=test_auth.py"
	cd e2e && poetry run pytest tests/$(FILE) -v --headed

# ============================================================================
# HELP
# ============================================================================

## Show this help message
help:
	@echo ""
	@echo "╔════════════════════════════════════════════════════════════════╗"
	@echo "║           Mock Project - E2E Testing Training                  ║"
	@echo "╚════════════════════════════════════════════════════════════════╝"
	@echo ""
	@echo "📚 QUICK START"
	@echo "   make deps   Install all dependencies (auto-installs Poetry)"
	@echo "   make dev    Start application (recommended)"
	@echo ""
	@echo "🛠️  DEVELOPMENT"
	@echo "   make dev-bg      Start in background"
	@echo "   make stop        Stop all services"
	@echo "   make logs        View all logs"
	@echo "   make reset       Reset database"
	@echo "   make clean-deps  Remove all dependencies"
	@echo ""
	@echo "🧪 TESTING"
	@echo "   make test         Run E2E tests (headless)"
	@echo "   make test-headed  Run E2E tests with browser"
	@echo ""
	@echo "📖 After starting, open:"
	@echo "   Frontend: http://localhost:3000"
	@echo "   Backend:  http://localhost:8000"
	@echo "   API Docs: http://localhost:8000/docs"
	@echo ""

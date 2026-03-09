# Training Mock Project: Data Management App

A monorepo application for E2E testing practice.

## 🚀 Quick Start (2 commands only!)

```bash
# 1. Install dependencies & setup config (auto-installs Poetry & pnpm if needed)
make deps

# 2. Start everything
make dev
```

That's it! After running `make dev`:

- **Frontend UI**: <http://localhost:3000>
- **Backend API**: <http://localhost:8000>
- **API Documentation**: <http://localhost:8000/docs>

> **Note**: Database tables are created and sample data is seeded automatically.

## 📋 Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running
- Python 3.12+
- Node.js 18+
- Poetry (Python dependency manager) - auto-installed via `make deps`
- pnpm (Node.js package manager) - auto-installed via `make deps`

### For Windows Users

**Install Make:**

```powershell
# Using Chocolatey (Recommended)
choco install make

# Or using winget
winget install GnuWin32.Make
```

After installation, restart your terminal and verify:

```powershell
make --version
```

## 🏗️ Architecture

```text
mock-project/
├── backend/          # FastAPI + PostgreSQL (Poetry)
├── frontend/         # NextJS 14 (pnpm)
├── e2e/              # Playwright Python tests (Poetry)
└── docker-compose.yml
```

## 📱 Application Features

| Page | URL | Features |
|------|-----|----------|
| Products | `/products` | View/edit product catalog |
| Inventory | `/inventory` | Track stock levels |
| Orders | `/orders` | Manage customer orders |

### UI Features for Testing

- ✏️ **Editable cells** - Double-click to edit
- 🖱️ **Multi-select** - Ctrl/Cmd + Click
- 📁 **Collapsible sidebar** - Toggle to focus
- 💾 **Save/Reset** - Persist or revert changes
- 🔐 **Authentication** - Dev bypass enabled

## 🧪 E2E Testing Practice

Your task is to implement E2E tests in the `e2e/` folder:

### Test Scenarios

1. ✅ Login with dev bypass
2. 🧭 Navigate between pages
3. 📊 View data in tables
4. ✏️ Edit single cell
5. 🖱️ Edit multiple cells (Ctrl/Cmd + Click)
6. 💾 Save changes
7. ↩️ Reset changes
8. 📁 Toggle sidebar

### Run Tests

```bash
make test          # Run headless
make test-headed   # Run with browser visible
```

## 📚 Available Commands

| Command | Description |
|---------|-------------|
| `make deps` | Install all dependencies |
| `make config` | Create .env files from templates |
| `make dev` | Start application |
| `make stop` | Stop all services |
| `make logs` | View logs |
| `make test` | Run E2E tests |
| `make help` | Show all commands |

## 📝 Development Notes

### API Endpoints

- **Auth**: `/auth/google`, `/auth/me`, `/auth/logout`
- **Products**: `/api/products`, `/api/products/{id}`
- **Inventory**: `/api/inventory`, `/api/inventory/{id}`
- **Orders**: `/api/orders`, `/api/orders/{id}`

### Test Account

Dev bypass is enabled by default. Click "Dev Login" on the login page.

---

**Need help?** Run `make help` to see all available commands.

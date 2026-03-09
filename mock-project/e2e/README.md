# E2E Tests for Mock Project

This folder contains end-to-end tests using **Python + Playwright**.

## Structure

```text
e2e/
├── conftest.py          # Shared fixtures
├── pyproject.toml       # Dependencies & pytest config
├── pages/               # Page Object Models
│   ├── __init__.py
│   ├── base_page.py     # Base page class
│   ├── login_page.py    # Login page object
│   ├── products_page.py # Products page object
│   ├── inventory_page.py # Inventory page object
│   └── orders_page.py   # Orders page object
├── tests/               # Test files
│   ├── __init__.py
│   ├── test_auth.py     # Authentication tests
│   ├── test_products.py # Products page tests
│   ├── test_inventory.py # Inventory page tests
│   ├── test_orders.py   # Orders page tests
│   └── test_navigation.py # Navigation tests
└── utils/               # Utility functions
    ├── __init__.py
    └── helpers.py       # Helper functions
```

## Setup

From the project root, run:

```bash
# Install all dependencies (backend + frontend + e2e)
make deps
```

Or manually:

```bash
cd e2e
poetry install
poetry run playwright install
```

## Run Tests

```bash
# From project root
make test          # Run headless
make test-headed   # Run with browser visible

# Or from e2e folder
cd e2e
poetry run pytest --headed  # Run with browser visible
poetry run pytest           # Run headless
```

## Key Testing Scenarios

### Authentication

- [ ] Login with Google SSO
- [ ] Dev login (bypass auth)
- [ ] Logout functionality
- [ ] Session persistence

### Products Page

- [ ] View product list
- [ ] Select single cell
- [ ] Multi-select cells (Ctrl/Cmd + click)
- [ ] Edit cell by double-click
- [ ] Save changes
- [ ] Reset changes
- [ ] Verify changes persist after save

### Inventory Page

- [ ] View inventory list
- [ ] Edit quantity
- [ ] Edit location
- [ ] Low stock warning display
- [ ] Bulk edit multiple cells

### Orders Page

- [ ] View orders list
- [ ] Filter by status
- [ ] Edit order status
- [ ] Edit customer info
- [ ] Status badge counts

### Navigation

- [ ] Navigate between pages
- [ ] Sidebar collapse/expand
- [ ] Active page highlight
- [ ] Responsive sidebar

## Test Data IDs (data-testid)

### Global

- `sidebar` - Main sidebar container
- `sidebar-toggle` - Collapse/expand button
- `nav-products` - Products nav link
- `nav-inventory` - Inventory nav link
- `nav-orders` - Orders nav link
- `logout-button` - Logout button
- `user-name` - Logged in user name
- `user-email` - Logged in user email

### Tables

- `{tableName}-table` - Table container (e.g., `products-table`)
- `header-{columnKey}` - Column header
- `row-{id}` - Table row
- `cell-{id}-{columnKey}` - Cell
- `value-{id}-{columnKey}` - Cell value display
- `input-{id}-{columnKey}` - Cell edit input

### Actions

- `save-button` - Save changes button
- `reset-button` - Reset changes button
- `selected-count` - Selected cells count
- `pending-count` - Pending changes count

### Login Page

- `google-login-button` - Google SSO button
- `dev-login-button` - Dev login bypass button

### Orders Page Specific

- `status-filter` - Status filter dropdown
- `status-badge-{status}` - Status count badges

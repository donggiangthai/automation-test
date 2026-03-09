# Day 7: Fixtures & Test Organization

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Fixture concepts introduction |
| 15 min | Test isolation principle |
| 30 min | Hands-on demo: fixtures & conftest |
| 25 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Create reusable test fixtures using **pure function → fixture pattern**
- Organize tests with conftest.py
- Understand fixture scopes
- Learn **Test Isolation** principle

---

## 🔴 CRITICAL: Test Isolation Principle

```
┌─────────────────────────────────────────────────────────────┐
│                    TEST ISOLATION RULES                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ✅ Each test MUST be independent                           │
│  ✅ Tests can run in ANY order                              │
│  ✅ One test failure should NOT affect others               │
│  ✅ Each test creates its OWN test data                     │
│  ✅ Each test cleans up after itself                        │
│                                                             │
│  ❌ NEVER share state between tests                         │
│  ❌ NEVER depend on test execution order                    │
│  ❌ NEVER assume data from previous test exists             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Pattern: Pure Function → Fixture

### Step 1: Pure Functions (utils/test_data_factory.py)

```python
# utils/test_data_factory.py
"""
PURE FUNCTIONS - reusable, testable, no framework dependency
"""
import random
import string

def create_user_data(
    username: str = None,
    email: str = None,
    password: str = "Test@123",
    role: str = "user"
) -> dict:
    """
    Pure function to create user data.
    Can be used in unit tests, fixtures, or standalone scripts.
    """
    if username is None:
        username = f"user_{random.randint(1000, 9999)}"
    if email is None:
        email = f"{username}@test.com"
    
    return {
        "username": username,
        "email": email,
        "password": password,
        "role": role
    }

def create_product_data(
    name: str = None,
    price: float = None,
    category: str = "General"
) -> dict:
    """Pure function to create product data"""
    if name is None:
        suffix = ''.join(random.choices(string.ascii_lowercase, k=5))
        name = f"Product_{suffix}"
    if price is None:
        price = round(random.uniform(10, 500), 2)
    
    return {
        "name": name,
        "price": price,
        "category": category,
        "in_stock": True
    }
```

### Step 2: Fixture Wrappers (tests/conftest.py)

```python
# tests/conftest.py
"""
FIXTURE WRAPPERS - inject pure functions into pytest
"""
import pytest
from utils.test_data_factory import create_user_data, create_product_data

# ============ User Fixtures ============

@pytest.fixture
def sample_user():
    """Provide a standard test user"""
    return create_user_data(username="testuser")

@pytest.fixture
def admin_user():
    """Provide an admin user"""
    return create_user_data(username="admin", role="admin")

@pytest.fixture
def unique_user():
    """Provide a UNIQUE user for each test (isolation!)"""
    return create_user_data()  # Random username each time

@pytest.fixture
def valid_products():
    """Provide list of valid products"""
    return [
        create_product_data(name="Laptop", price=999.99),
        create_product_data(name="Mouse", price=29.99),
        create_product_data(name="Keyboard", price=79.99),
    ]

@pytest.fixture
def empty_cart():
    """Provide empty shopping cart"""
    return {"items": [], "total": 0}

# ============ Session-scoped Fixtures ============

@pytest.fixture(scope="session")
def test_config():
    """Configuration loaded once per test session"""
    return {
        "base_url": "https://example.com",
        "timeout": 30,
        "browser": "chromium"
    }

# ============ Cleanup Pattern ============

@pytest.fixture
def user_with_cleanup(sample_user):
    """
    Fixture with cleanup - ensures test isolation.
    Yield allows code to run AFTER test completes.
    """
    # Setup: create user
    created_user = sample_user
    
    yield created_user  # Test runs here
    
    # Teardown: cleanup (runs even if test fails!)
    # In real app: api.delete_user(created_user['email'])
    print(f"Cleaned up user: {created_user['email']}")
```

### Step 3: Using Fixtures in Tests

```python
# tests/test_user.py
"""Tests using fixtures"""

def test_user_has_username(sample_user):
    """Verify user fixture has username"""
    assert "username" in sample_user
    assert len(sample_user["username"]) > 0

def test_user_has_valid_email(sample_user):
    """Verify email format"""
    assert "@" in sample_user["email"]
    assert "." in sample_user["email"]

def test_admin_has_role(admin_user):
    """Verify admin has role"""
    assert admin_user["role"] == "admin"

def test_products_have_prices(valid_products):
    """All products should have prices"""
    for product in valid_products:
        assert "price" in product
        assert product["price"] > 0

def test_cart_starts_empty(empty_cart):
    """Cart should start with no items"""
    assert len(empty_cart["items"]) == 0
    assert empty_cart["total"] == 0
```

---

## Fixture Scopes

| Scope | When Created | When Destroyed |
|-------|--------------|----------------|
| `function` (default) | Before each test | After each test |
| `class` | Before first test in class | After last test in class |
| `module` | Before first test in file | After last test in file |
| `session` | Once for entire test run | After all tests |

---

## Practice Exercise

Create fixtures for an e-commerce application:

```python
# tests/conftest.py
# TODO: Create these fixtures:

@pytest.fixture
def logged_in_user():
    """Provide a logged-in user session"""
    # Create user data with token
    pass

@pytest.fixture
def shopping_cart_with_items():
    """Provide a cart with 3 items"""
    # Create cart with products
    pass

@pytest.fixture(scope="module")
def product_catalog():
    """Provide list of 10 products (module scope)"""
    pass

@pytest.fixture(scope="session")
def app_config():
    """App config loaded once per session"""
    pass
```

---

## Homework (2 hours)

### Reading
1. [pytest Fixtures Documentation](https://docs.pytest.org/en/stable/how-to/fixtures.html)
2. [Fixture Scope](https://docs.pytest.org/en/stable/how-to/fixtures.html#scope-sharing-fixtures-across-classes-modules-packages-or-session)

### Coding Tasks
1. **Test Data Factory:** Create `utils/test_data_factory.py` with pure functions:
   - `create_user_data(username, email, role)`
   - `create_product_data(name, price, category)`
   - `create_order_data(user_id, products)`

2. **Fixture Suite:** Create fixtures in conftest.py wrapping your factory functions

3. **Cleanup Pattern:** Implement a fixture that creates a temporary file and cleans it up after test

### Quiz Yourself
1. What's the difference between `function` and `session` scope?
2. How does `yield` enable cleanup in fixtures?
3. Why is test isolation important?
4. What's the "pure function → fixture" pattern?

---

[← Day 6](day-06-pytest-intro.md) | [Next: Day 8 - Parameterized Tests →](day-08-parametrize.md)

# Personalized Training Plan: QA Automation with AI

**Trainee Profile:** Experienced Manual QA transitioning to Automation  
**Platform:** Windows  
**Duration:** 4 weeks, 1.5 hours per day (20 sessions) + 2 hours self-study  
**Tech Stack:** Python + Playwright + GitHub Copilot

---

## Trainee Strengths (Leverage These)

| Strength | How We'll Use It |
| ---------- | ------------------ |
| Manual QA experience | Skip testing theory, focus on automation implementation |
| Testing mindset | Apply to test case design immediately |
| DevTools familiarity | Use for locator identification from Day 1 |
| Command Prompt experience | Quick transition to running Python/Playwright |
| Knows Selenium concept | Compare/contrast with Playwright approach |
| High motivation | Accelerated pace with challenging exercises |

## Focus Areas (Build These)

| Area | Current Level | Target |
| ------ | --------------- | -------- |
| Python coding | Beginner | Write functions, classes, handle data |
| Playwright | Concept only | Write complete E2E tests independently |
| AI-assisted coding | New | Generate tests with Copilot, review/improve AI code |

---

## 🎯 Production-Ready Patterns (Key Differentiators)

This training includes **critical patterns** that separate professional automation from toy examples:

| Pattern | Why It Matters | When Learned |
| --------- | ---------------- | -------------- |
| **Test Isolation** | Tests can run in any order, independently | Day 7 |
| **Pure Function → Fixture** | Reusable, testable, maintainable code | Day 7 |
| **Semantic Locators** | Resilient to UI changes | Day 12 |
| **Wait Strategies** | No flaky tests from race conditions | Day 13 |
| **Network Mocking** | Fast, stable, deterministic tests | Day 14 |
| **Debug Artifacts** | Quick failure diagnosis in CI/CD | Day 15 |
| **AI Code Review** | Catch common AI mistakes | Day 18 |

---

## Windows Environment Setup (Day 0 - Pre-Training)

Complete these steps before Day 1:

### 1. Install Python

```powershell
# Download from python.org or use winget
winget install Python.Python.3.13

# Verify installation
python --version
pip --version
```

### 2. Install VS Code

```powershell
winget install Microsoft.VisualStudioCode

# Install extensions:
# - Python (Microsoft)
# - Pylance
# - GitHub Copilot
# - GitHub Copilot Chat
```

### 3. Configure VS Code for Windows

Settings to verify:

- Terminal: Select "Command Prompt" or "PowerShell" as default
- Python interpreter: Select Python 3.13

### 4. Create Project Structure

```powershell
# Open Command Prompt or PowerShell
cd Desktop
mkdir automation-training
cd automation-training
mkdir tests pages utils data
```

### 5. Keyboard Shortcuts Reference (Windows)

| Action | Shortcut |
| -------- | ---------- |
| Copy | `Ctrl+C` |
| Paste | `Ctrl+V` |
| Cut | `Ctrl+X` |
| Save file | `Ctrl+S` |
| Open file | `Ctrl+O` |
| Quick open (VS Code) | `Ctrl+P` |
| Command palette | `Ctrl+Shift+P` |
| Toggle terminal | `` Ctrl+` `` |
| DevTools (Browser) | `F12` or `Ctrl+Shift+I` |

---

## Week 1: Python Fundamentals for Testers

### Day 1: Python Basics - Variables & Data Types

**Objectives:**

- Write first Python program
- Understand variables, strings, numbers, booleans
- Use print() and input()

**Session (1.5 hours):**

```python
# hello_test.py
# Your first Python program

# Variables - like test data storage
test_username = "admin"
test_password = "P@ssw0rd123"
is_valid_user = True
login_attempts = 3

# Print - useful for debugging tests
print("Testing login with:", test_username)
print(f"Valid user: {is_valid_user}")  # f-string formatting

# Input - interactive testing
user_input = input("Enter username to test: ")
print(f"You entered: {user_input}")

# Basic operations
total_tests = 50
passed_tests = 45
pass_rate = (passed_tests / total_tests) * 100
print(f"Pass rate: {pass_rate}%")
```

**Exercise:** Create variables for a test scenario (user registration with name, email, age, is_premium).

**Self-study (2 hours):**

- Complete Python basics on W3Schools
- Practice 10 variable exercises

---

### Day 2: Control Flow - Making Decisions

**Objectives:**

- Use if/elif/else statements
- Apply comparison operators
- Write basic test validations

**Session:**

```python
# validation_tests.py
# Testing login validation logic

def validate_login(username, password):
    """
    Simulate login validation - this is what we'll automate later
    """
    # Test case 1: Empty username
    if not username:
        return "Error: Username required"
    
    # Test case 2: Empty password
    if not password:
        return "Error: Password required"
    
    # Test case 3: Username too short
    if len(username) < 3:
        return "Error: Username must be at least 3 characters"
    
    # Test case 4: Password requirements
    if len(password) < 8:
        return "Error: Password must be at least 8 characters"
    
    # Test case 5: Valid credentials (mock check)
    valid_users = {"admin": "Admin123!", "testuser": "Test@123"}
    if username in valid_users and valid_users[username] == password:
        return "Login successful"
    
    return "Error: Invalid credentials"

# Run test cases
test_cases = [
    ("", "password"),           # Empty username
    ("admin", ""),              # Empty password
    ("ab", "password123"),      # Short username
    ("admin", "short"),         # Short password
    ("admin", "Admin123!"),     # Valid login
    ("admin", "wrongpass"),     # Wrong password
]

print("Running login validation tests:\n")
for username, password in test_cases:
    result = validate_login(username, password)
    print(f"Test: username='{username}', password='{password}'")
    print(f"Result: {result}\n")
```

**Exercise:** Add validation for email format (must contain @ and .)

---

### Day 3: Functions - Reusable Test Helpers

**Objectives:**

- Create functions with parameters
- Return values
- Build test utility functions

**Session:**

```python
# test_helpers.py
# Functions you'll use in real automation

import random
import string

def generate_random_email(domain="test.com"):
    """Generate unique email for test user"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"user_{random_string}@{domain}"

def generate_random_password(length=12):
    """Generate password meeting requirements"""
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choices(chars, k=length))
    return password

def create_test_user():
    """Create complete test user data"""
    return {
        "email": generate_random_email(),
        "password": generate_random_password(),
        "first_name": f"Test_{random.randint(1000, 9999)}",
        "last_name": "User"
    }

def assert_equals(actual, expected, message=""):
    """Custom assertion - similar to what pytest does"""
    if actual == expected:
        print(f"✅ PASS: {message}")
        return True
    else:
        print(f"❌ FAIL: {message}")
        print(f"   Expected: {expected}")
        print(f"   Actual: {actual}")
        return False

# Test our helpers
print("Generated emails:")
for i in range(3):
    print(f"  {generate_random_email()}")

print("\nGenerated passwords:")
for i in range(3):
    print(f"  {generate_random_password()}")

print("\nTest user:")
user = create_test_user()
for key, value in user.items():
    print(f"  {key}: {value}")

# Using our assertion
print("\nTesting assertions:")
assert_equals(2 + 2, 4, "Basic math")
assert_equals("hello".upper(), "HELLO", "String uppercase")
assert_equals(len([1, 2, 3]), 3, "List length")
```

**Exercise:** Create a function `validate_email(email)` that returns True/False.

---

### Day 4: Lists, Loops & Dictionaries - Test Data Management

**Objectives:**

- Work with collections
- Iterate through test data
- Store structured test data

**Session:**

```python
# test_data_management.py
# Managing test data like a pro

# List of test scenarios
login_test_data = [
    {"username": "admin", "password": "Admin123!", "expected": "success"},
    {"username": "", "password": "Admin123!", "expected": "error"},
    {"username": "admin", "password": "", "expected": "error"},
    {"username": "invalid", "password": "wrong", "expected": "error"},
]

# Running data-driven tests
print("=== Data-Driven Login Tests ===\n")
passed = 0
failed = 0

for test in login_test_data:
    # Simulate test execution
    if test["username"] and test["password"]:
        if test["username"] == "admin" and test["password"] == "Admin123!":
            result = "success"
        else:
            result = "error"
    else:
        result = "error"
    
    # Verify result
    if result == test["expected"]:
        print(f"✅ PASS: username='{test['username']}'")
        passed += 1
    else:
        print(f"❌ FAIL: username='{test['username']}'")
        print(f"   Expected: {test['expected']}, Got: {result}")
        failed += 1

print(f"\n=== Results: {passed} passed, {failed} failed ===")

# Dictionary for page elements (Page Object preview)
login_page_elements = {
    "username_input": "#username",
    "password_input": "#password", 
    "login_button": "button[type='submit']",
    "error_message": ".error-message",
    "success_message": ".welcome-message"
}

print("\n=== Login Page Elements ===")
for name, selector in login_page_elements.items():
    print(f"  {name}: {selector}")
```

**Exercise:** Create test data for product search (search term, expected results count, category filter).

---

### Day 5: Week 1 Review & Mini-Project

**Mini-Project:** Test Data Generator Tool

Build a command-line tool that generates test data for your QA work:

```python
# test_data_generator.py
import random
import string
import json
from datetime import datetime, timedelta

class TestDataGenerator:
    """Generate various types of test data"""
    
    @staticmethod
    def random_string(length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    @staticmethod
    def random_email():
        return f"{TestDataGenerator.random_string(8).lower()}@test.com"
    
    @staticmethod
    def random_phone():
        return f"+1{random.randint(1000000000, 9999999999)}"
    
    @staticmethod
    def random_date(start_year=2020, end_year=2025):
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
    
    @staticmethod
    def random_price(min_val=1, max_val=1000):
        return round(random.uniform(min_val, max_val), 2)
    
    @staticmethod
    def generate_user():
        return {
            "id": random.randint(1, 99999),
            "email": TestDataGenerator.random_email(),
            "first_name": TestDataGenerator.random_string(6).capitalize(),
            "last_name": TestDataGenerator.random_string(8).capitalize(),
            "phone": TestDataGenerator.random_phone(),
            "created_at": TestDataGenerator.random_date()
        }
    
    @staticmethod
    def generate_product():
        categories = ["Electronics", "Clothing", "Books", "Home", "Sports"]
        return {
            "id": random.randint(1, 99999),
            "name": f"Product {TestDataGenerator.random_string(5)}",
            "category": random.choice(categories),
            "price": TestDataGenerator.random_price(),
            "in_stock": random.choice([True, False])
        }
    
    @staticmethod
    def generate_order(user_id=None):
        return {
            "id": random.randint(1, 99999),
            "user_id": user_id or random.randint(1, 99999),
            "products": [TestDataGenerator.generate_product() for _ in range(random.randint(1, 5))],
            "status": random.choice(["pending", "processing", "shipped", "delivered"]),
            "created_at": TestDataGenerator.random_date()
        }


def main():
    gen = TestDataGenerator()
    
    print("=== Test Data Generator ===\n")
    
    # Generate users
    print("Users:")
    users = [gen.generate_user() for _ in range(3)]
    for user in users:
        print(f"  {user['email']} - {user['first_name']} {user['last_name']}")
    
    # Generate products
    print("\nProducts:")
    products = [gen.generate_product() for _ in range(3)]
    for product in products:
        print(f"  {product['name']} - ${product['price']} ({product['category']})")
    
    # Save to JSON file
    test_data = {
        "users": users,
        "products": products,
        "orders": [gen.generate_order() for _ in range(2)]
    }
    
    with open("test_data.json", "w") as f:
        json.dump(test_data, f, indent=2)
    
    print("\n✅ Test data saved to test_data.json")


if __name__ == "__main__":
    main()
```

---

## Week 2: pytest & Test Framework

### Day 6: Introduction to pytest

**Objectives:**

- Install and configure pytest
- Write first pytest tests
- Understand assertions

**Setup:**

```powershell
# In your project folder
pip install pytest pytest-html

# Verify
pytest --version
```

**Session:**

```python
# tests/test_calculator.py
"""
First pytest tests - testing a simple calculator
"""

# Simple calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# TESTS - pytest discovers functions starting with test_

def test_add_positive_numbers():
    """Test adding two positive numbers"""
    assert add(2, 3) == 5

def test_add_negative_numbers():
    """Test adding negative numbers"""
    assert add(-1, -1) == -2

def test_add_zero():
    """Test adding zero"""
    assert add(5, 0) == 5

def test_subtract():
    """Test subtraction"""
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0
    assert subtract(0, 5) == -5

def test_multiply():
    """Test multiplication"""
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    """Test division"""
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    """Test that dividing by zero raises error"""
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)
```

**Run tests:**

```powershell
# Run all tests
pytest tests/test_calculator.py -v

# Run specific test
pytest tests/test_calculator.py::test_add_positive_numbers -v

# Generate HTML report
pytest tests/test_calculator.py -v --html=report.html
```

---

### Day 7: Fixtures & Test Organization

**Objectives:**

- Create reusable test fixtures using **pure function → fixture pattern**
- Organize tests with conftest.py
- Understand fixture scopes
- Learn **Test Isolation** principle

### Test Isolation Principle

CRITICAL: Test Isolation Principle

```text
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

**Session:**

### Pattern: Pure Function → Fixture (Production Best Practice)

```python
# utils/test_data_factory.py
"""
Step 1: PURE FUNCTIONS - reusable, testable, no framework dependency
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

```python
# tests/conftest.py
"""
Step 2: FIXTURE WRAPPERS - inject pure functions into pytest
"""
import pytest
from utils.test_data_factory import create_user_data, create_product_data

# ============ User Fixtures (using pure functions) ============

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

### Day 8: Parameterized Tests (Data-Driven)

**Objectives:**

- Run same test with different data
- Use pytest.mark.parametrize
- Leverage your QA experience with data-driven testing

**Session:**

```python
# tests/test_login_validation.py
"""
Data-driven tests - similar to running manual test cases with different data
"""
import pytest

def validate_email(email):
    """Simple email validation"""
    if not email:
        return False
    if "@" not in email:
        return False
    if "." not in email.split("@")[-1]:
        return False
    return True

def validate_password(password):
    """Password must be 8+ chars with uppercase, lowercase, number"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit


# Parameterized tests - each tuple is a test case
@pytest.mark.parametrize("email,expected", [
    ("user@example.com", True),          # Valid email
    ("user@domain.co.uk", True),         # Valid with subdomain
    ("user.name@example.com", True),     # Valid with dot in local
    ("invalid-email", False),            # Missing @
    ("@example.com", False),             # Missing local part
    ("user@", False),                    # Missing domain
    ("user@domain", False),              # Missing TLD
    ("", False),                         # Empty string
    (None, False),                       # None value
])
def test_email_validation(email, expected):
    """Test email validation with various inputs"""
    result = validate_email(email) if email is not None else False
    assert result == expected, f"Email '{email}' validation failed"


@pytest.mark.parametrize("password,expected", [
    ("Password1", True),                  # Valid - meets all requirements
    ("MyP@ss123", True),                  # Valid with special char
    ("password", False),                  # No uppercase or digit
    ("PASSWORD", False),                  # No lowercase or digit
    ("Password", False),                  # No digit
    ("12345678", False),                  # No letters
    ("Pass1", False),                     # Too short
    ("", False),                          # Empty
])
def test_password_validation(password, expected):
    """Test password validation rules"""
    assert validate_password(password) == expected


# Combining multiple parameters
@pytest.mark.parametrize("username,password,expected_result", [
    ("admin", "Admin123", "success"),
    ("user", "User1234", "success"),
    ("", "Password1", "error_username"),
    ("admin", "", "error_password"),
    ("admin", "short", "error_password"),
    ("x", "Password1", "error_username"),
])
def test_login_scenarios(username, password, expected_result):
    """Test various login scenarios"""
    # Simulate login logic
    if not username or len(username) < 2:
        result = "error_username"
    elif not password or len(password) < 8:
        result = "error_password"
    else:
        result = "success"
    
    assert result == expected_result
```

---

### Day 9: Test Markers & Selection

**Objectives:**

- Organize tests with markers
- Run specific test groups
- Configure pytest.ini

**Session:**

```python
# pytest.ini (create in project root)
"""
[pytest]
markers =
    smoke: Quick critical path tests
    regression: Full regression suite
    login: Login-related tests
    cart: Shopping cart tests
    slow: Tests that take longer
    
testpaths = tests
addopts = -v --tb=short
"""

# tests/test_e2e_scenarios.py
import pytest

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login():
    """Critical: User can login with valid credentials"""
    # Will be automated with Playwright
    assert True

@pytest.mark.smoke
def test_homepage_loads():
    """Critical: Homepage loads successfully"""
    assert True

@pytest.mark.regression
@pytest.mark.login
def test_login_with_email():
    """User can login with email instead of username"""
    assert True

@pytest.mark.regression
@pytest.mark.login
def test_remember_me_functionality():
    """Remember me checkbox keeps user logged in"""
    assert True

@pytest.mark.regression
@pytest.mark.cart
def test_add_single_item_to_cart():
    """User can add one item to cart"""
    assert True

@pytest.mark.regression
@pytest.mark.cart
def test_add_multiple_items_to_cart():
    """User can add multiple items to cart"""
    assert True

@pytest.mark.slow
@pytest.mark.cart
def test_cart_with_100_items():
    """Performance: Cart handles 100 items"""
    assert True

@pytest.mark.skip(reason="Feature not implemented yet")
def test_social_login():
    """User can login with Google account"""
    assert True
```

**Run commands:**

```powershell
# Run only smoke tests
pytest -m smoke

# Run login tests
pytest -m login

# Run regression excluding slow tests
pytest -m "regression and not slow"

# Run smoke OR login tests
pytest -m "smoke or login"
```

---

### Day 10: Week 2 Review - Complete Test Suite

**Mini-Project:** Test suite for User Management module

```python
# tests/test_user_management.py
"""
Complete test suite demonstrating pytest features
"""
import pytest

# ============ Fixtures ============

@pytest.fixture
def user_service():
    """Mock user service"""
    class UserService:
        def __init__(self):
            self.users = {}
        
        def create_user(self, email, password, name):
            if email in self.users:
                raise ValueError("User already exists")
            if not self._validate_email(email):
                raise ValueError("Invalid email format")
            if len(password) < 8:
                raise ValueError("Password too short")
            
            user_id = len(self.users) + 1
            self.users[email] = {
                "id": user_id,
                "email": email,
                "name": name,
                "active": True
            }
            return self.users[email]
        
        def get_user(self, email):
            return self.users.get(email)
        
        def delete_user(self, email):
            if email in self.users:
                del self.users[email]
                return True
            return False
        
        def _validate_email(self, email):
            return "@" in email and "." in email
    
    return UserService()


# ============ Smoke Tests ============

@pytest.mark.smoke
class TestUserCreation:
    """Critical user creation tests"""
    
    def test_create_valid_user(self, user_service):
        """User can be created with valid data"""
        user = user_service.create_user(
            email="test@example.com",
            password="Password123",
            name="Test User"
        )
        assert user["email"] == "test@example.com"
        assert user["active"] == True
    
    def test_create_user_generates_id(self, user_service):
        """Created user receives an ID"""
        user = user_service.create_user(
            email="test@example.com",
            password="Password123",
            name="Test User"
        )
        assert "id" in user
        assert user["id"] > 0


# ============ Validation Tests ============

@pytest.mark.regression
class TestUserValidation:
    """Input validation tests"""
    
    @pytest.mark.parametrize("invalid_email", [
        "invalid",
        "no-at-sign.com",
        "@nodomain",
        "spaces in@email.com",
    ])
    def test_reject_invalid_email(self, user_service, invalid_email):
        """Invalid emails are rejected"""
        with pytest.raises(ValueError, match="Invalid email"):
            user_service.create_user(invalid_email, "Password123", "Test")
    
    @pytest.mark.parametrize("short_password", [
        "short",
        "1234567",
        "",
    ])
    def test_reject_short_password(self, user_service, short_password):
        """Short passwords are rejected"""
        with pytest.raises(ValueError, match="Password too short"):
            user_service.create_user("test@example.com", short_password, "Test")
    
    def test_reject_duplicate_email(self, user_service):
        """Duplicate emails are rejected"""
        user_service.create_user("test@example.com", "Password123", "First")
        
        with pytest.raises(ValueError, match="already exists"):
            user_service.create_user("test@example.com", "Password456", "Second")


# ============ CRUD Tests ============

@pytest.mark.regression
class TestUserCRUD:
    """Create, Read, Update, Delete tests"""
    
    def test_get_existing_user(self, user_service):
        """Can retrieve created user"""
        user_service.create_user("test@example.com", "Password123", "Test")
        
        user = user_service.get_user("test@example.com")
        assert user is not None
        assert user["name"] == "Test"
    
    def test_get_nonexistent_user_returns_none(self, user_service):
        """Getting non-existent user returns None"""
        user = user_service.get_user("nobody@example.com")
        assert user is None
    
    def test_delete_existing_user(self, user_service):
        """Can delete existing user"""
        user_service.create_user("test@example.com", "Password123", "Test")
        
        result = user_service.delete_user("test@example.com")
        assert result == True
        assert user_service.get_user("test@example.com") is None
    
    def test_delete_nonexistent_user(self, user_service):
        """Deleting non-existent user returns False"""
        result = user_service.delete_user("nobody@example.com")
        assert result == False
```

Run and generate report:

```powershell
pytest tests/test_user_management.py -v --html=user_tests_report.html
```

---

## Week 3: Playwright Web Automation

### Day 11: Playwright Setup & First Automation

**Objectives:**

- Install Playwright with proper project configuration
- Setup **production-ready conftest.py**
- Write first browser automation
- Understand environment configuration

**Setup:**

```powershell
pip install pytest-playwright
playwright install
```

### CRITICAL: Project Configuration (Do This First!)

**pytest.ini** (create in project root):

```ini
[pytest]
markers =
    smoke: Quick critical path tests
    regression: Full regression suite
    slow: Tests that take longer

testpaths = tests
addopts = -v --tb=short

# Playwright settings
playwright_browser = chromium
```

**tests/conftest.py** (Production-ready Playwright fixtures):

```python
"""
Production-ready Playwright conftest.py
This file is CRITICAL for stable, maintainable E2E tests.
"""
import pytest
from playwright.sync_api import Page, BrowserContext
from typing import Generator
import os

# ============ Configuration ============

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Configure browser context for all tests.
    This runs ONCE per test session.
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        # Record video for debugging failed tests
        "record_video_dir": "test-results/videos",
    }

@pytest.fixture(scope="session")
def base_url():
    """
    Base URL from environment or default.
    Allows switching environments: staging, production, local.
    """
    return os.getenv("BASE_URL", "https://the-internet.herokuapp.com")

# ============ Enhanced Page Fixture ============

@pytest.fixture
def page(page: Page, base_url: str) -> Generator[Page, None, None]:
    """
    Enhanced page fixture with:
    - Default timeout
    - Base URL injection
    - Console error logging
    """
    # Set default timeout (10 seconds)
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    
    # Capture console errors (helps debug JavaScript issues)
    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    
    yield page
    
    # After test: report any console errors
    if console_errors:
        print(f"\\n⚠️ Console errors during test: {console_errors}")

# ============ Screenshot on Failure ============

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    \"\"\"
    Take screenshot on test failure.
    Screenshots saved to: test-results/screenshots/
    \"\"\"
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Get page from test fixtures
        page = item.funcargs.get("page")
        if page:
            screenshot_dir = "test-results/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = f"{screenshot_dir}/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"\\n📸 Screenshot saved: {screenshot_path}")

# ============ Test Data Fixtures ============

@pytest.fixture
def valid_credentials():
    \"\"\"Valid login credentials for the-internet.herokuapp.com\"\"\"
    return {
        "username": "tomsmith",
        "password": "SuperSecretPassword!"
    }

@pytest.fixture
def invalid_credentials():
    \"\"\"Invalid credentials for negative testing\"\"\"
    return {
        "username": "invalid_user",
        "password": "wrong_password"
    }
```

**Session:**

```python
# tests/test_first_automation.py
"""
First Playwright automation - leveraging your DevTools experience!
"""
from playwright.sync_api import Page, expect

def test_google_homepage(page: Page):
    """Navigate to Google and verify title"""
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_search_automation_testing(page: Page):
    """Search for automation testing"""
    page.goto("https://www.google.com")
    
    # Find search box - you can find this selector using DevTools!
    search_box = page.locator("textarea[name='q']")
    search_box.fill("automation testing")
    search_box.press("Enter")
    
    # Wait for results
    page.wait_for_load_state("networkidle")
    
    # Verify results appeared
    expect(page.locator("#search")).to_be_visible()

def test_playwright_docs(page: Page):
    """Navigate Playwright documentation"""
    page.goto("https://playwright.dev")
    
    # Click on Python docs
    page.get_by_role("link", name="Docs").click()
    
    # Verify navigation
    expect(page).to_have_url_pattern(".*docs.*")
```

**Run with browser visible:**

```powershell
pytest tests/test_first_automation.py --headed -v

# Run with different base URL (environment switch)
$env:BASE_URL="https://staging.example.com"; pytest tests/ -v
```

**Generate trace for debugging:**

```powershell
pytest tests/test_first_automation.py --tracing=on
```

---

### Day 12: Locators - Your DevTools Skills Shine

**Objectives:**

- Use modern Playwright locators
- Apply DevTools knowledge

**Session:**

```python
# tests/test_locators.py
"""
Locator strategies - organized by reliability
"""
from playwright.sync_api import Page, expect

def test_role_based_locators(page: Page):
    """
    BEST: Role-based locators - most reliable
    These match what users actually see/interact with
    """
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Find elements by their role in the page
    username_input = page.get_by_role("textbox", name="Username")
    password_input = page.get_by_role("textbox", name="Password")
    login_button = page.get_by_role("button", name="Login")
    
    # Interact
    username_input.fill("tomsmith")
    password_input.fill("SuperSecretPassword!")
    login_button.click()
    
    # Verify
    expect(page.get_by_role("heading", name="Secure Area")).to_be_visible()

def test_text_based_locators(page: Page):
    """
    GOOD: Text-based locators
    Use when element has unique visible text
    """
    page.goto("https://the-internet.herokuapp.com")
    
    # Find link by its text
    page.get_by_text("Form Authentication").click()
    
    # Verify we're on login page
    expect(page).to_have_url_pattern(".*login.*")

def test_label_and_placeholder_locators(page: Page):
    """
    GOOD: Label and placeholder locators
    Great for forms
    """
    page.goto("https://the-internet.herokuapp.com/login")
    
    # By label (if form has proper labels)
    # page.get_by_label("Username").fill("test")
    
    # By placeholder
    page.get_by_placeholder("Username").fill("tomsmith")
    page.get_by_placeholder("Password").fill("SuperSecretPassword!")

def test_css_selectors(page: Page):
    """
    FALLBACK: CSS selectors
    Use when semantic locators don't work
    You know these from DevTools!
    """
    page.goto("https://the-internet.herokuapp.com/login")
    
    # ID selector
    page.locator("#username").fill("tomsmith")
    
    # Class selector
    page.locator("button.radius").click()
    
    # Attribute selector
    page.locator("input[name='password']").fill("SuperSecretPassword!")
    
    # Combined
    page.locator("form#login button[type='submit']").click()

def test_test_id_locators(page: Page):
    """
    RECOMMENDED: data-testid attributes
    Best practice for automation-friendly apps
    """
    # If your app uses data-testid:
    # page.get_by_test_id("login-button").click()
    # page.get_by_test_id("username-input").fill("test")
    pass
```

### Locator Decision Guide

CRITICAL: When to Use data-testid vs Role-based Locators

```text
┌─────────────────────────────────────────────────────────────────┐
│                    LOCATOR DECISION GUIDE                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  USE ROLE-BASED LOCATORS WHEN:                                 │
│  ✅ Element has unique accessible name                          │
│     → page.get_by_role("button", name="Submit")                │
│  ✅ Form inputs have proper labels                              │
│     → page.get_by_label("Email")                               │
│  ✅ Links/headings with unique text                            │
│     → page.get_by_role("link", name="Sign Up")                 │
│                                                                 │
│  USE data-testid WHEN:                                         │
│  🔧 Icon-only buttons (no text, no accessible name)            │
│     → <button data-testid="close-modal">✕</button>             │
│  🔧 Multiple similar elements (list items, table rows)         │
│     → <tr data-testid="user-row-123">...</tr>                  │
│  🔧 Dynamic/generated content                                   │
│     → page.get_by_test_id(f"product-{product_id}")             │
│  🔧 Elements that frequently change text                       │
│     → Promotional banners, A/B test variants                   │
│                                                                 │
│  ❌ AVOID CSS SELECTORS FOR:                                    │
│  - Styling classes (.btn-primary, .card)                       │
│  - Generated IDs (#ember123, #react-component-456)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Practical Examples:**

```python
# tests/test_locator_decisions.py
"""When to use which locator strategy"""
from playwright.sync_api import Page, expect

def test_button_with_text(page: Page):
    """Button has visible text → use role"""
    # ✅ GOOD: Role-based (user sees "Login")
    page.get_by_role("button", name="Login").click()
    
    # ❌ AVOID: CSS class (might change with redesign)
    # page.locator(".btn-login").click()

def test_icon_button_no_text(page: Page):
    """Icon button without text → need data-testid"""
    # ✅ GOOD: data-testid (no visible text to locator)
    page.get_by_test_id("close-modal").click()
    
    # ⚠️ FALLBACK: aria-label if set
    # page.get_by_role("button", name="Close")

def test_list_items(page: Page):
    """Multiple similar items → use data-testid with ID"""
    # ✅ GOOD: Target specific item in list
    page.get_by_test_id("product-row-SKU123").click()
    
    # ⚠️ AVOID: nth() - breaks if order changes
    # page.locator(".product-row").nth(2).click()

def test_form_with_labels(page: Page):
    """Form inputs with labels → use get_by_label"""
    # ✅ GOOD: Semantic, accessibility-friendly
    page.get_by_label("Email Address").fill("test@example.com")
    page.get_by_label("Password").fill("secure123")
    
    # ⚠️ ACCEPTABLE: Placeholder (less reliable)
    # page.get_by_placeholder("Enter email").fill(...)
```

---

### Day 13: Actions, Assertions & Wait Strategies

**Objectives:**

- Perform all common user actions
- Write meaningful assertions
- **Master wait strategies** (avoid flaky tests!)
- **Handle errors gracefully**

**Session:**

```python
# tests/test_actions.py
"""
Complete guide to Playwright actions
"""
from playwright.sync_api import Page, expect

def test_text_input_actions(page: Page):
    """Various ways to input text"""
    page.goto("https://the-internet.herokuapp.com/inputs")
    
    input_field = page.locator("input[type='number']")
    
    # Fill - clears and types
    input_field.fill("12345")
    
    # Clear
    input_field.clear()
    
    # Type character by character (slower, simulates real typing)
    input_field.type("67890", delay=100)
    
    # Press special keys
    input_field.press("Backspace")
    input_field.press("Control+a")  # Select all
    input_field.press("Delete")

def test_click_actions(page: Page):
    """Various click actions"""
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    
    add_button = page.get_by_role("button", name="Add Element")
    
    # Single click
    add_button.click()
    
    # Double click
    add_button.dblclick()
    
    # Right click
    # add_button.click(button="right")
    
    # Click with modifier
    # add_button.click(modifiers=["Shift"])
    
    # Verify buttons were added
    delete_buttons = page.get_by_role("button", name="Delete")
    expect(delete_buttons).to_have_count(3)

def test_checkbox_and_radio(page: Page):
    """Handle checkboxes and radio buttons"""
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    
    checkboxes = page.locator("input[type='checkbox']")
    
    # Check
    checkboxes.first.check()
    expect(checkboxes.first).to_be_checked()
    
    # Uncheck
    checkboxes.last.uncheck()
    expect(checkboxes.last).not_to_be_checked()

def test_dropdown_selection(page: Page):
    """Handle dropdown/select elements"""
    page.goto("https://the-internet.herokuapp.com/dropdown")
    
    dropdown = page.locator("#dropdown")
    
    # Select by value
    dropdown.select_option("1")
    
    # Select by label
    dropdown.select_option(label="Option 2")
    
    # Verify selection
    expect(dropdown).to_have_value("2")

def test_hover_action(page: Page):
    """Mouse hover"""
    page.goto("https://the-internet.herokuapp.com/hovers")
    
    # Hover over first figure
    page.locator(".figure").first.hover()
    
    # Verify caption appears
    expect(page.get_by_text("name: user1")).to_be_visible()

def test_file_upload(page: Page):
    """Upload a file"""
    page.goto("https://the-internet.herokuapp.com/upload")
    
    # Create a test file first
    # page.locator("#file-upload").set_input_files("path/to/file.txt")
    pass

def test_drag_and_drop(page: Page):
    """Drag and drop elements"""
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    
    # Drag column A to column B
    page.locator("#column-a").drag_to(page.locator("#column-b"))


# ============ Assertions ============

def test_assertions_examples(page: Page):
    """Various assertion types"""
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Page assertions
    expect(page).to_have_title("The Internet")
    expect(page).to_have_url_pattern(".*login.*")
    
    # Element visibility
    expect(page.locator("#username")).to_be_visible()
    expect(page.locator("#nonexistent")).not_to_be_visible()
    
    # Element state
    expect(page.locator("button")).to_be_enabled()
    
    # Text content
    expect(page.locator("h2")).to_have_text("Login Page")
    expect(page.locator("h2")).to_contain_text("Login")
    
    # Attributes
    expect(page.locator("#username")).to_have_attribute("name", "username")
    
    # Count
    expect(page.locator("input")).to_have_count(2)
```

### CRITICAL: Wait Strategies (Avoid Flaky Tests!)

```python
# tests/test_wait_strategies.py
"""
NEVER use time.sleep() in tests!
Always use Playwright's built-in waits.
"""
from playwright.sync_api import Page, expect
import pytest

# ❌ BAD: Hard-coded wait (NEVER DO THIS!)
def test_bad_wait_example(page: Page):
    import time
    page.goto("/slow-loading-page")
    time.sleep(5)  # ❌ Wastes time if page loads faster
    # ... test continues

# ✅ GOOD: Wait for specific condition
def test_wait_for_element(page: Page):
    """Wait for element to be visible"""
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    
    # ✅ Wait for loading to complete (auto-waits up to timeout)
    expect(page.locator("#finish h4")).to_be_visible()
    expect(page.locator("#finish h4")).to_have_text("Hello World!")

def test_wait_for_navigation(page: Page):
    """Wait for page navigation"""
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    
    # ✅ Click and wait for navigation
    with page.expect_navigation():
        page.get_by_role("button", name="Login").click()
    
    expect(page).to_have_url_pattern(".*secure.*")

def test_wait_for_network_idle(page: Page):
    """Wait for all network requests to complete"""
    page.goto("https://example.com")
    
    # ✅ Wait for network to be idle (no requests for 500ms)
    page.wait_for_load_state("networkidle")

def test_wait_for_api_response(page: Page):
    """Wait for specific API call"""
    page.goto("https://example.com")
    
    # ✅ Wait for specific API response
    with page.expect_response("**/api/users") as response_info:
        page.get_by_role("button", name="Load Users").click()
    
    response = response_info.value
    assert response.status == 200

def test_custom_wait_condition(page: Page):
    """Wait for custom condition"""
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    
    # ✅ Wait for element with custom timeout
    page.locator("#finish h4").wait_for(state="visible", timeout=10000)
```

**Wait Strategy Decision Guide:**

| Scenario | Wait Method |
| ---------- | ------------- |
| Element appears | `expect(locator).to_be_visible()` |
| Page navigation | `page.expect_navigation()` |
| API call completes | `page.expect_response(url)` |
| All network done | `page.wait_for_load_state("networkidle")` |
| Custom condition | `locator.wait_for(state="visible")` |

### Error Handling & Expected Failures

```python
# tests/test_error_handling.py
"""
How to handle expected errors and verify negative scenarios
"""
from playwright.sync_api import Page, expect, TimeoutError
import pytest

def test_element_should_not_exist(page: Page):
    """Verify element does NOT appear"""
    page.goto("https://the-internet.herokuapp.com/login")
    
    # ✅ Correct: Verify element is NOT visible
    expect(page.locator("#error-message")).not_to_be_visible()
    
    # ✅ Alternative: Check count is 0
    expect(page.locator(".non-existent")).to_have_count(0)

def test_handle_expected_timeout(page: Page):
    """Handle expected timeout gracefully"""
    page.goto("https://the-internet.herokuapp.com")
    
    # ✅ Expect timeout for non-existent element
    with pytest.raises(TimeoutError):
        page.locator("#never-exists").click(timeout=1000)

def test_conditional_element(page: Page):
    """Handle element that may or may not exist"""
    page.goto("https://the-internet.herokuapp.com")
    
    # ✅ Check if element exists before interacting
    popup = page.locator("#optional-popup")
    if popup.is_visible():
        popup.locator("button.close").click()
    
    # Continue with test...

def test_soft_assertion_pattern(page: Page):
    """Collect multiple failures before failing test"""
    page.goto("https://the-internet.herokuapp.com/login")
    
    errors = []
    
    # Check multiple things, collect all errors
    try:
        expect(page).to_have_title("The Internet")
    except AssertionError as e:
        errors.append(f"Title check failed: {e}")
    
    try:
        expect(page.locator("#username")).to_be_visible()
    except AssertionError as e:
        errors.append(f"Username field not visible: {e}")
    
    # Fail with all collected errors
    if errors:
        pytest.fail("\\n".join(errors))
```

---

### Day 14: Page Object Model & Network Mocking

**Objectives:**

- Implement POM pattern
- Create maintainable test structure
- **Master Network Mocking** (stable, fast tests!)

### Network-First Pattern

CRITICAL: Network-First Pattern

```text
┌─────────────────────────────────────────────────────────────────┐
│                  NETWORK-FIRST PATTERN                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ALWAYS setup network intercepts BEFORE navigation!            │
│                                                                 │
│  ✅ CORRECT ORDER:                                              │
│     1. page.route("**/api/...", handler)  ← Setup intercept    │
│     2. page.goto("/page")                  ← Then navigate     │
│                                                                 │
│  ❌ WRONG ORDER:                                                │
│     1. page.goto("/page")                  ← Page loads        │
│     2. page.route("**/api/...", handler)  ← Too late!         │
│                                                                 │
│  WHY?                                                           │
│  - Page might make API calls immediately on load               │
│  - Race condition: request fires before intercept is set       │
│  - Results in flaky tests                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Network Mocking Examples:**

```python
# tests/test_network_mocking.py
"""
Network mocking - control API responses for stable tests
"""
from playwright.sync_api import Page, Route, expect
import json

def test_mock_api_success(page: Page):
    """Mock API to return success response"""
    
    # ✅ Step 1: Setup intercept BEFORE navigation
    def handle_login(route: Route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body=json.dumps({
                "success": True,
                "token": "mock-jwt-token",
                "user": {"id": 1, "name": "Test User"}
            })
        )
    
    page.route("**/api/login", handle_login)
    
    # ✅ Step 2: Navigate AFTER intercept is set
    page.goto("https://example.com/login")
    
    # ✅ Step 3: Perform actions
    page.get_by_label("Username").fill("testuser")
    page.get_by_label("Password").fill("password")
    page.get_by_role("button", name="Login").click()
    
    # Test will use mocked response, not real API!

def test_mock_api_error(page: Page):
    """Mock API to return error - test error handling"""
    
    page.route("**/api/login", lambda route: route.fulfill(
        status=401,
        content_type="application/json",
        body=json.dumps({"error": "Invalid credentials"})
    ))
    
    page.goto("https://example.com/login")
    page.get_by_label("Username").fill("wrong")
    page.get_by_label("Password").fill("wrong")
    page.get_by_role("button", name="Login").click()
    
    # Verify error handling UI
    expect(page.locator(".error-message")).to_contain_text("Invalid")

def test_mock_slow_api(page: Page):
    """Mock slow API - test loading states"""
    import time
    
    def slow_response(route: Route):
        time.sleep(2)  # Simulate slow network
        route.fulfill(
            status=200,
            body=json.dumps({"data": "loaded"})
        )
    
    page.route("**/api/data", slow_response)
    page.goto("https://example.com/dashboard")
    
    # Verify loading spinner appears
    expect(page.locator(".loading-spinner")).to_be_visible()
    
    # Then verify data loads
    expect(page.locator(".data-container")).to_be_visible()

def test_mock_products_list(page: Page):
    """Mock product list - consistent test data"""
    
    mock_products = [
        {"id": 1, "name": "Test Product 1", "price": 99.99},
        {"id": 2, "name": "Test Product 2", "price": 149.99},
    ]
    
    page.route("**/api/products", lambda route: route.fulfill(
        status=200,
        body=json.dumps(mock_products)
    ))
    
    page.goto("https://example.com/products")
    
    # Tests use consistent mock data, never real API
    expect(page.locator(".product-card")).to_have_count(2)
    expect(page.get_by_text("Test Product 1")).to_be_visible()

def test_intercept_and_modify(page: Page):
    """Let real API call through but modify response"""
    
    def modify_response(route: Route):
        # Get real response
        response = route.fetch()
        body = response.json()
        
        # Modify it
        body["injected_test_flag"] = True
        
        # Return modified response
        route.fulfill(
            response=response,
            body=json.dumps(body)
        )
    
    page.route("**/api/user", modify_response)
    page.goto("https://example.com/profile")
```

**Session - Page Object Model:**

```python
# pages/base_page.py
"""Base page with common functionality"""
from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, path: str):
        """Navigate to a path"""
        base_url = "https://the-internet.herokuapp.com"
        self.page.goto(f"{base_url}{path}")
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def wait_for_load(self):
        """Wait for page to fully load"""
        self.page.wait_for_load_state("networkidle")


# pages/login_page.py
"""Login page object"""
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "/login"
    
    def __init__(self, page: Page):
        super().__init__(page)
        # Locators
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")
    
    def navigate(self):
        """Navigate to login page"""
        self.navigate_to(self.URL)
        return self
    
    def login(self, username: str, password: str):
        """Perform login action"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self
    
    def expect_success(self):
        """Verify successful login"""
        expect(self.flash_message).to_contain_text("You logged into a secure area")
        expect(self.logout_button).to_be_visible()
        return self
    
    def expect_error(self, message: str = None):
        """Verify login error"""
        if message:
            expect(self.flash_message).to_contain_text(message)
        expect(self.flash_message).to_have_class_pattern(".*error.*")
        return self
    
    def logout(self):
        """Perform logout"""
        self.logout_button.click()
        return self


# tests/test_login_pom.py
"""Tests using Page Object Model"""
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    """Provide login page object"""
    return LoginPage(page)


class TestLogin:
    """Login functionality tests"""
    
    @pytest.mark.smoke
    def test_successful_login(self, login_page: LoginPage):
        """Valid credentials allow login"""
        login_page.navigate()
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.expect_success()
    
    @pytest.mark.smoke
    def test_logout(self, login_page: LoginPage):
        """User can logout after login"""
        login_page.navigate()
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.logout()
        
        # Should be back at login page
        expect(login_page.login_button).to_be_visible()
    
    @pytest.mark.regression
    def test_invalid_username(self, login_page: LoginPage):
        """Invalid username shows error"""
        login_page.navigate()
        login_page.login("invalid", "SuperSecretPassword!")
        login_page.expect_error("Your username is invalid")
    
    @pytest.mark.regression
    def test_invalid_password(self, login_page: LoginPage):
        """Invalid password shows error"""
        login_page.navigate()
        login_page.login("tomsmith", "wrongpassword")
        login_page.expect_error("Your password is invalid")
    
    @pytest.mark.regression
    @pytest.mark.parametrize("username,password", [
        ("", "password"),        # Empty username
        ("user", ""),            # Empty password
        ("", ""),                # Both empty
    ])
    def test_empty_credentials(self, login_page: LoginPage, username, password):
        """Empty credentials show error"""
        login_page.navigate()
        login_page.login(username, password)
        login_page.expect_error()
```

---

### Day 15: Week 3 Project - Production-Ready E2E Test Suite

**Mini-Project:** Complete E2E test suite with debug artifacts

**Project Structure:**

```text
automation-training/
├── pytest.ini                  # pytest configuration
├── conftest.py                 # Root fixtures (optional)
├── pages/
│   ├── __init__.py
│   ├── base_page.py           # Base page with common methods
│   ├── login_page.py          # Login page object
│   └── secure_page.py         # Secure area page object
├── tests/
│   ├── conftest.py            # Test fixtures (Playwright, mocks)
│   ├── test_login.py          # Login tests
│   └── test_navigation.py     # Navigation tests
├── utils/
│   ├── __init__.py
│   └── test_data_factory.py   # Pure functions for test data
└── test-results/              # Auto-generated
    ├── screenshots/           # Failure screenshots
    ├── videos/                # Test recordings
    └── traces/                # Playwright traces
```

**Complete Implementation:**

```python
# pages/base_page.py
"""Base page with wait helpers and common functionality"""
from playwright.sync_api import Page, expect
from typing import Optional
import os

class BasePage:
    # Get base URL from environment or use default
    BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, path: str):
        """Navigate to a path relative to base URL"""
        full_url = f"{self.BASE_URL}{path}"
        self.page.goto(full_url)
        return self
    
    def wait_for_page_load(self):
        """Wait for page to be fully loaded"""
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        return self
    
    def take_screenshot(self, name: str):
        """Take screenshot for debugging"""
        os.makedirs("test-results/screenshots", exist_ok=True)
        self.page.screenshot(path=f"test-results/screenshots/{name}.png")
        return self
    
    def get_page_title(self) -> str:
        return self.page.title()


# pages/login_page.py
"""Login page with network mocking support"""
from playwright.sync_api import Page, expect, Route
from pages.base_page import BasePage
import json

class LoginPage(BasePage):
    URL = "/login"
    
    def __init__(self, page: Page):
        super().__init__(page)
        # Use semantic locators (role-based preferred)
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")
        self.logout_button = page.get_by_role("link", name="Logout")
    
    def navigate(self):
        self.navigate_to(self.URL)
        return self
    
    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return self
    
    def expect_success(self):
        expect(self.flash_message).to_contain_text("You logged into")
        expect(self.logout_button).to_be_visible()
        return self
    
    def expect_error(self, message: str = None):
        expect(self.flash_message).to_be_visible()
        if message:
            expect(self.flash_message).to_contain_text(message)
        return self
    
    def logout(self):
        self.logout_button.click()
        return self


# tests/conftest.py
"""Production-ready test fixtures"""
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage
import os

# ============ Configuration ============

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "record_video_dir": "test-results/videos",
    }

# ============ Page Object Fixtures ============

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """Provide login page object"""
    return LoginPage(page)

# ============ Test Data Fixtures ============

@pytest.fixture
def valid_credentials():
    return {"username": "tomsmith", "password": "SuperSecretPassword!"}

@pytest.fixture
def invalid_credentials():
    return {"username": "invalid", "password": "wrong"}


# tests/test_login.py
"""Login functionality - production-ready tests"""
import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

class TestLoginSmoke:
    """Smoke tests - run on every deployment"""
    
    @pytest.mark.smoke
    def test_successful_login(self, login_page: LoginPage, valid_credentials):
        """P0: User can login with valid credentials"""
        login_page.navigate()
        login_page.login(
            valid_credentials["username"],
            valid_credentials["password"]
        )
        login_page.expect_success()
    
    @pytest.mark.smoke
    def test_logout(self, login_page: LoginPage, valid_credentials):
        """P0: User can logout"""
        login_page.navigate()
        login_page.login(
            valid_credentials["username"],
            valid_credentials["password"]
        )
        login_page.logout()
        expect(login_page.login_button).to_be_visible()


class TestLoginValidation:
    """Regression tests - login validation"""
    
    @pytest.mark.regression
    def test_invalid_username(self, login_page: LoginPage):
        """P1: Invalid username shows error"""
        login_page.navigate()
        login_page.login("invalid_user", "SuperSecretPassword!")
        login_page.expect_error("Your username is invalid")
    
    @pytest.mark.regression
    def test_invalid_password(self, login_page: LoginPage):
        """P1: Invalid password shows error"""
        login_page.navigate()
        login_page.login("tomsmith", "wrong_password")
        login_page.expect_error("Your password is invalid")
    
    @pytest.mark.regression
    @pytest.mark.parametrize("username,password,error_type", [
        ("", "password", "username"),
        ("user", "", "password"),
    ])
    def test_empty_fields(self, login_page: LoginPage, username, password, error_type):
        """P2: Empty fields show appropriate error"""
        login_page.navigate()
        login_page.login(username, password)
        # Verify error is shown (specific message depends on app)
        login_page.expect_error()
```

**Running Tests with Artifacts:**

```powershell
# Run all tests with video recording
pytest tests/ -v

# Run smoke tests only
pytest tests/ -m smoke -v

# Run with trace (for debugging failures)
pytest tests/ --tracing=on

# View trace file
playwright show-trace test-results/trace.zip

# Generate HTML report
pip install pytest-html
pytest tests/ -v --html=test-results/report.html
```

**Debugging Failed Tests:**

```text
┌─────────────────────────────────────────────────────────────────┐
│                   DEBUG ARTIFACTS GUIDE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  📸 SCREENSHOTS (test-results/screenshots/)                     │
│     - Auto-captured on failure                                  │
│     - Shows exact state when test failed                       │
│                                                                 │
│  🎬 VIDEOS (test-results/videos/)                               │
│     - Full test recording                                       │
│     - See what happened step-by-step                           │
│                                                                 │
│  🔍 TRACES (playwright show-trace trace.zip)                    │
│     - Timeline of all actions                                   │
│     - Network requests/responses                                │
│     - Console logs                                              │
│     - DOM snapshots at each step                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Week 4: AI-Assisted Testing with GitHub Copilot

### Day 16: GitHub Copilot Setup & Basics

**Objectives:**

- Configure GitHub Copilot
- Understand AI code generation
- First AI-assisted test

**Setup:**

1. Install "GitHub Copilot" extension in VS Code
2. Install "GitHub Copilot Chat" extension
3. Sign in with GitHub account
4. Enable Copilot for Python files

**Session - Let Copilot Help:**

```python
# Type comments and let Copilot suggest code

# tests/test_copilot_demo.py
"""
Let's see Copilot in action
"""
from playwright.sync_api import Page, expect

# Function to validate email format
# (Type this comment, then press Tab to accept Copilot suggestion)

# Function to generate random username with prefix "test_"

# Playwright test for login page that:
# 1. Navigates to login page
# 2. Enters valid credentials
# 3. Clicks login button
# 4. Verifies successful login

# Page Object for a product search page with:
# - search input field
# - search button
# - results container
# - method to search for a product
# - method to get number of results
```

---

### Day 17: Effective Prompting for Tests

**Objectives:**

- Write effective prompts
- Use Copilot Chat for test generation
- Apply your QA knowledge to prompts

**Session:**

**Copilot Chat Prompts (Press Ctrl+Shift+I to open):**

```text
Prompt 1 - Generate Test Cases:
"Generate pytest test cases for a shopping cart that supports:
- Adding items
- Removing items
- Updating quantities
- Calculating total price
Include edge cases like empty cart and invalid quantities."

Prompt 2 - Generate Page Object:
"Create a Playwright Page Object class for an e-commerce checkout page with:
- Shipping address form (name, address, city, zip)
- Payment method selector
- Place order button
- Order confirmation message
Include methods for filling the form and completing checkout."

Prompt 3 - Generate Data-Driven Tests:
"Create parameterized Playwright tests for login functionality testing:
- Valid credentials (success)
- Invalid username (error)
- Invalid password (error)
- Empty fields (error)
- SQL injection attempt (error)
Use pytest.mark.parametrize."
```

**Tips for Better Prompts:**

1. Be specific about framework (pytest, Playwright)
2. Mention patterns you want (POM, fixtures)
3. Include edge cases you want tested
4. Specify assertions needed

---

### Day 18: Reviewing AI-Generated Code

**Objectives:**

- Critically evaluate AI suggestions
- Identify common AI mistakes
- Apply QA mindset to code review

**Session - Review Checklist:**

```python
# AI CODE REVIEW CHECKLIST
"""
When Copilot generates code, check:

□ CORRECTNESS
  - Does it do what I asked?
  - Are assertions actually verifying the right things?
  - Is the logic correct?

□ LOCATORS
  - Are locators reliable? (prefer role-based over CSS)
  - Will they break if page changes slightly?
  - Are they specific enough?

□ WAITS
  - Does it wait for elements before interacting?
  - Is it using proper wait strategies (not time.sleep)?
  - Will it handle slow networks?

□ ERROR HANDLING
  - What happens if element not found?
  - Are there timeouts?
  - Is failure message helpful?

□ MAINTAINABILITY
  - Is the code readable?
  - Can someone else understand it?
  - Is there unnecessary duplication?

□ TEST DESIGN
  - Is each test independent?
  - Does it clean up after itself?
  - Is it testing one thing well?

□ HARDCODING
  - Are values parameterized where appropriate?
  - Are there magic numbers/strings?
  - Is test data external or inline?
"""

# Example: Review this AI-generated test
def test_login_ai_generated(page):
    page.goto("https://example.com/login")
    page.fill("#username", "testuser")           # ⚠️ CSS selector
    page.fill("#password", "password123")        # ⚠️ Hardcoded password
    page.click("button")                         # ⚠️ Too generic
    time.sleep(2)                                # ❌ Bad wait!
    assert page.url == "https://example.com/dashboard"  # ⚠️ Not using expect

# IMPROVED version:
def test_login_improved(page: Page):
    page.goto("https://example.com/login")
    page.get_by_label("Username").fill("testuser")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url_pattern(".*dashboard.*")
```

---

### Day 19: Integration - AI + Manual Coding

**Objectives:**

- Know when to use AI vs manual coding
- Build efficient workflow
- Complete test suite with AI assistance

**Workflow:**

```text
┌─────────────────────────────────────────────────────┐
│                  AI-ASSISTED WORKFLOW               │
├─────────────────────────────────────────────────────┤
│                                                      │
│  1. PLAN (Manual)                                   │
│     - Define test scenarios                         │
│     - List test cases                               │
│                                                      │
│  2. SCAFFOLD (AI)                                   │
│     - Generate Page Object structure                │
│     - Generate test file structure                  │
│                                                      │
│  3. IMPLEMENT (AI + Manual)                         │
│     - AI: Initial locators and actions              │
│     - Manual: Review and improve                    │
│                                                      │
│  4. REVIEW (Manual with AI help)                    │
│     - Check each test works                         │
│     - Ask AI to suggest improvements                │
│                                                      │
│  5. REFACTOR (AI + Manual)                          │
│     - AI: Suggest DRY improvements                  │
│     - Manual: Apply selectively                     │
│                                                      │
└─────────────────────────────────────────────────────┘
```

**Practice Project:**
Build a complete test suite for <https://automationexercise.com> with:

- Login page tests
- Product search tests
- Cart functionality tests
- Use AI for initial generation
- Review and improve each test

---

### Day 20: Final Assessment & Next Steps

**Assessment:**

| Component | Weight | Description |
| ----------- | -------- | ------------- |
| Quiz | 15% | Python, pytest, Playwright concepts |
| Code Review | 25% | Review AI-generated tests, provide improvements |
| Live Coding | 35% | Write tests for new feature with AI assistance |
| Project | 25% | Complete test suite review |

**Competency Checklist:**

```text
□ Python
  □ Write functions with parameters and return values
  □ Use lists, dictionaries, and loops
  □ Create classes with methods
  □ Handle exceptions
  □ Create pure functions for test data (factory pattern)

□ pytest
  □ Write tests with meaningful assertions
  □ Use fixtures for test setup
  □ Create parameterized tests
  □ Organize tests with markers
  □ Generate test reports
  □ Implement cleanup pattern (yield fixtures)
  □ Understand test isolation principle

□ Playwright
  □ Navigate web pages
  □ Use locators effectively (role-based preferred)
  □ Perform user actions (click, fill, select)
  □ Write assertions with expect
  □ Implement Page Object Model
  □ Use proper wait strategies (NO time.sleep!)
  □ Mock network responses (network-first pattern)
  □ Handle expected errors gracefully
  □ Configure test artifacts (screenshots, videos, traces)
  □ Debug failed tests using traces

□ AI-Assisted Testing
  □ Generate tests with GitHub Copilot
  □ Write effective prompts
  □ Review and improve AI code
  □ Know when to use AI vs manual

□ Production Readiness
  □ Write independent, isolated tests
  □ Use environment configuration (base_url, timeouts)
  □ Generate test reports for CI/CD
  □ Debug production failures with artifacts
```

---

## Post-Training Path

**Immediate (1-2 weeks):**

- Apply to real project at work
- Automate 5 manual test cases
- Share knowledge with team

**Short-term (1-3 months):**

- API testing with Playwright
- CI/CD integration
- Advanced reporting

**Long-term (3-6 months):**

- Test architecture design
- Mentoring others
- Contributing to test strategy

---

## Resources

**Python:**

- W3Schools Python: <https://www.w3schools.com/python/>
- Real Python: <https://realpython.com/>

**pytest:**

- Official Docs: <https://docs.pytest.org/>
- pytest-bdd for BDD: <https://pytest-bdd.readthedocs.io/>
- pytest Fixtures Guide: <https://docs.pytest.org/en/stable/how-to/fixtures.html>

**Playwright:**

- Python Docs: <https://playwright.dev/python/>
- Locators Guide: <https://playwright.dev/python/docs/locators>
- Network Mocking: <https://playwright.dev/python/docs/mock>
- Trace Viewer: <https://playwright.dev/python/docs/trace-viewer>
- Best Practices: <https://playwright.dev/python/docs/best-practices>

**GitHub Copilot:**

- Getting Started: <https://docs.github.com/en/copilot>
- Best Practices: <https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/>

**Practice Sites:**

- <https://the-internet.herokuapp.com/> (recommended for training)
- <https://automationexercise.com/>
- <https://www.saucedemo.com/>
- <https://demoqa.com/>

**Additional Learning:**

- Test Automation University: <https://testautomationu.applitools.com/>
- Ministry of Testing: <https://www.ministryoftesting.com/>

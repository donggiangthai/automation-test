# Day 8: Parameterized Tests (Data-Driven)

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Why data-driven testing? |
| 20 min | @parametrize syntax & options |
| 30 min | Hands-on demo (follow along) |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Run same test with different data
- Use pytest.mark.parametrize
- Leverage your QA experience with data-driven testing

---

## Visual Concept

```
┌─────────────────────────────────────────────────────────────┐
│           DATA-DRIVEN TESTING                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Manual Testing:         Automated (parametrize):          │
│   ┌──────────────────┐   ┌──────────────────┐              │
│   │ Test Case 1: A   │   │ @parametrize(    │              │
│   │ Test Case 2: B   │   │   [(A), (B),     │              │
│   │ Test Case 3: C   │   │    (C), (D)]     │              │
│   │ Test Case 4: D   │   │ )                │              │
│   └──────────────────┘   │ def test_it():   │              │
│   Run 4 times manually   │   assert ...     │              │
│                          └──────────────────┘              │
│                          One test, runs 4x                  │
│                                                             │
│   Result: Same coverage, way less code!                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

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

## Key Concepts

### Basic Parametrize

```python
@pytest.mark.parametrize("input,expected", [
    (1, 2),
    (2, 4),
    (3, 6),
])
def test_double(input, expected):
    assert input * 2 == expected
```

### Multiple Parameters

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (5, 5, 10),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert a + b == expected
```

### Test IDs

```python
@pytest.mark.parametrize("email,expected", [
    pytest.param("user@example.com", True, id="valid_email"),
    pytest.param("invalid", False, id="missing_at_sign"),
    pytest.param("", False, id="empty_string"),
])
def test_email(email, expected):
    assert validate_email(email) == expected
```

### Combining Parametrize Decorators

```python
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [10, 20])
def test_combinations(x, y):
    # Runs 4 times: (1,10), (1,20), (2,10), (2,20)
    print(f"x={x}, y={y}")
```

---

## Running Output

```
tests/test_login_validation.py::test_email_validation[user@example.com-True] PASSED
tests/test_login_validation.py::test_email_validation[user@domain.co.uk-True] PASSED
tests/test_login_validation.py::test_email_validation[invalid-email-False] PASSED
...
```

---

## Practice Exercise

Create parameterized tests for a shopping cart:

```python
# tests/test_cart_calculations.py
import pytest

def calculate_total(quantity, price, discount_percent):
    """Calculate cart total with discount"""
    subtotal = quantity * price
    discount = subtotal * (discount_percent / 100)
    return subtotal - discount

@pytest.mark.parametrize("quantity,price,discount,expected_total", [
    # TODO: Add test cases
    pytest.param(1, 100, 0, 100, id="no_discount"),
    pytest.param(2, 50, 10, 90, id="10_percent_off"),
    # Add more: zero quantity, 50% discount, free item (100%)
])
def test_cart_total(quantity, price, discount, expected_total):
    """Calculate cart total with discount"""
    total = calculate_total(quantity, price, discount)
    assert total == pytest.approx(expected_total, rel=0.01)
```

---

## Homework (2 hours)

### Reading
1. [pytest Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
2. [pytest.param](https://docs.pytest.org/en/stable/reference/reference.html#pytest-param)

### Coding Tasks
1. **Validation Suite:** Create 15 parameterized tests for:
   - Email validation (8 cases)
   - Phone number validation (5 cases)
   - Age validation (4 cases: under 0, 0, valid, over 150)

2. **External Data:** Load test data from JSON:
   ```python
   import json
   with open("test_data.json") as f:
       test_cases = json.load(f)
   
   @pytest.mark.parametrize("data", test_cases)
   def test_from_file(data):
       pass
   ```

3. **Matrix Testing:** Create tests with combined parametrize decorators (e.g., browsers x viewports)

### Quiz Yourself
1. How do you give meaningful IDs to test cases?
2. What happens when you stack multiple `@parametrize` decorators?
3. How do you use `pytest.approx` for float comparisons?
4. How do you mark a specific parametrized case to skip?

---

[← Day 7](day-07-fixtures.md) | [Next: Day 9 - Test Markers →](day-09-markers.md)

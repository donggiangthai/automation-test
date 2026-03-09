# Day 6: Introduction to pytest

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | pytest overview & philosophy |
| 15 min | Installation & first test |
| 30 min | Hands-on demo (follow along) |
| 25 min | Practice exercise |
| 10 min | Q&A & next steps |

---

## Objectives

- Install and configure pytest
- Write first pytest tests
- Understand assertions

---

## Visual Concept

```text
┌─────────────────────────────────────────────────────────────┐
│                    pytest FLOW                               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Discovery → Collection → Execution → Reporting            │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │  tests/                                              │  │
│   │  ├── test_login.py      ←─ Files: test_*.py         │  │
│   │  │   ├── test_valid()   ←─ Functions: test_*       │  │
│   │  │   └── test_invalid()                             │  │
│   │  └── test_cart.py                                   │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
│   Test Function Pattern:                                    │
│   ┌─────────────────────────────────────────────────────┐  │
│   │ def test_something():                                │  │
│   │     # Arrange - setup                                │  │
│   │     data = prepare_data()                            │  │
│   │     # Act - execute                                  │  │
│   │     result = function_to_test(data)                  │  │
│   │     # Assert - verify                                │  │
│   │     assert result == expected                        │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Setup

```powershell
# In your project folder
pip install pytest pytest-html

# Verify
pytest --version
```

---

## Hands-on Demo

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

---

## Running Tests

```powershell
# Run all tests
pytest tests/test_calculator.py -v

# Run specific test
pytest tests/test_calculator.py::test_add_positive_numbers -v

# Run tests matching pattern
pytest tests/test_calculator.py -k "add" -v

# Generate HTML report
pytest tests/test_calculator.py -v --html=report.html
```

---

## Key Concepts

### pytest Discovery

pytest automatically finds tests by:

- Files: `test_*.py` or `*_test.py`
- Functions: `test_*`
- Classes: `Test*` (methods must start with `test_`)

### Assert Statements

```python
# Basic assertions
assert value == expected
assert value != unexpected
assert value is True
assert value is None
assert value in collection

# With message
assert value == expected, f"Expected {expected}, got {value}"

# Approximate equality (for floats)
assert value == pytest.approx(expected, rel=0.01)
```

### Testing Exceptions

```python
import pytest

def test_raises_value_error():
    with pytest.raises(ValueError):
        # Code that should raise ValueError
        raise ValueError("Something went wrong")

def test_raises_with_message():
    with pytest.raises(ValueError, match="Something"):
        raise ValueError("Something went wrong")
```

---

## Practice Exercise

Create tests for a password validator:

```python
# tests/test_password.py

def is_valid_password(password):
    """Password must be 8+ chars with uppercase, lowercase, and digit"""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit


# TODO: Write tests for:
def test_valid_password():
    """Test a password that meets all requirements"""
    pass

def test_password_too_short():
    """Test password less than 8 characters"""
    pass

def test_password_missing_uppercase():
    pass

def test_password_missing_lowercase():
    pass

def test_password_missing_digit():
    pass
```

Run with: `pytest tests/test_password.py -v`

---

## Homework (2 hours)

### Reading

1. [pytest Documentation](https://docs.pytest.org/en/stable/)
2. [pytest Good Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html)

### Coding Tasks

1. **Calculator Tests:** Write 10 tests for add, subtract, multiply, divide functions
2. **String Validator Tests:** Test email, phone, credit card validation functions from Week 1
3. **Explore Options:** Try running with different flags:
   - `pytest -v` (verbose)
   - `pytest -s` (show print statements)
   - `pytest --tb=short` (shorter traceback)
   - `pytest --html=report.html` (HTML report)

### Quiz Yourself

1. How does pytest discover test files and functions?
2. What's the difference between `assert` and `pytest.raises()`?
3. What does the `-v` flag do?
4. How do you run only tests matching a pattern?

---

[← Week 1 Project](../week-1/day-05-project.md) | [Next: Day 7 - Fixtures →](day-07-fixtures.md)

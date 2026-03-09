# Day 9: Test Markers & Selection

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Why organize tests with markers? |
| 15 min | pytest.ini & marker configuration |
| 30 min | Hands-on demo (follow along) |
| 25 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Organize tests with markers
- Run specific test groups
- Configure pytest.ini

---

## Visual Concept

```
┌─────────────────────────────────────────────────────────────┐
│               TEST ORGANIZATION WITH MARKERS                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   All Tests                                                 │
│   ┌─────────────────────────────────────────────────────┐  │
│   │ ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ │  │
│   │ │ @smoke  │  │@login   │  │ @cart   │  │ @slow   │ │  │
│   │ │ (5 min) │  │(10 tests│  │(15 tests│  │(30 min) │ │  │
│   │ └─────────┘  └─────────┘  └─────────┘  └─────────┘ │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
│   Run Commands:                                             │
│   pytest -m smoke          # Quick sanity check            │
│   pytest -m "not slow"     # Everything except slow        │
│   pytest -m "login or cart" # Feature-specific            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## pytest.ini Configuration

Create in project root:

```ini
# pytest.ini
[pytest]
markers =
    smoke: Quick critical path tests
    regression: Full regression suite
    login: Login-related tests
    cart: Shopping cart tests
    slow: Tests that take longer
    
testpaths = tests
addopts = -v --tb=short
```

---

## Session

```python
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

@pytest.mark.xfail(reason="Known bug - JIRA-123")
def test_edge_case_bug():
    """This test covers a known bug"""
    assert False  # Expected to fail
```

---

## Running Tests by Markers

```powershell
# Run only smoke tests
pytest -m smoke

# Run login tests
pytest -m login

# Run regression excluding slow tests
pytest -m "regression and not slow"

# Run smoke OR login tests
pytest -m "smoke or login"

# Run everything except slow
pytest -m "not slow"
```

---

## Built-in Markers

| Marker | Purpose |
|--------|---------|
| `@pytest.mark.skip(reason="...")` | Skip test always |
| `@pytest.mark.skipif(condition, reason="...")` | Skip conditionally |
| `@pytest.mark.xfail(reason="...")` | Expected to fail |
| `@pytest.mark.parametrize(...)` | Data-driven tests |

### Conditional Skipping

```python
import sys
import pytest

@pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
def test_unix_only():
    pass

@pytest.mark.skipif(sys.version_info < (3, 10), reason="Requires Python 3.10+")
def test_new_feature():
    pass
```

---

## Marker Strategy for QA

```
┌─────────────────────────────────────────────────────────────┐
│                    MARKER STRATEGY                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  @smoke       - Run on every deployment (5-10 min)         │
│  @regression  - Full test suite (30-60 min)                │
│  @slow        - Performance/load tests (exclude in CI)     │
│                                                             │
│  Feature markers:                                           │
│  @login, @cart, @checkout, @search, @profile               │
│                                                             │
│  Priority markers:                                          │
│  @p0 (critical), @p1 (high), @p2 (medium)                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Practice Exercise

Create a test file with organized markers:

```python
# tests/test_ecommerce.py
import pytest

# TODO: Create 3 smoke tests (critical paths)
@pytest.mark.smoke
def test_homepage_loads():
    pass

# TODO: Create 5 regression tests (detailed scenarios)

# TODO: Create 2 slow tests (performance)

# TODO: Create 1 skipped test (not implemented feature)

# TODO: Create 1 xfail test (known bug)
```

Run different combinations:
```bash
pytest -m smoke -v
pytest -m "regression and not slow" -v
pytest -m "smoke or login" -v
```

---

## Homework (2 hours)

### Reading
1. [pytest Markers](https://docs.pytest.org/en/stable/how-to/mark.html)
2. [Built-in Markers](https://docs.pytest.org/en/stable/reference/reference.html#marks)

### Coding Tasks
1. **Marker Strategy:** Design your marker strategy:
   - Define at least 5 custom markers in pytest.ini
   - Create 15 tests using these markers
   - Document your marker strategy in a README

2. **CI Simulation:** Create test runs for:
   - Quick check (smoke only) - target 2 min
   - Full regression (all except slow) - target 15 min
   - Nightly (everything including slow)

3. **Priority System:** Implement P0/P1/P2 markers

### Quiz Yourself
1. Where do you define custom markers?
2. How do you combine markers with `and`, `or`, `not`?
3. What's the difference between `@skip` and `@xfail`?
4. When would you use `@skipif` vs `@skip`?

---

[← Day 8](day-08-parametrize.md) | [Next: Day 10 - Week 2 Project →](day-10-project.md)

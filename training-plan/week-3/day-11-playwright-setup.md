# Day 11: Playwright Setup & First Automation

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | E2E testing intro & Playwright overview |
| 20 min | Installation & project setup |
| 30 min | Hands-on demo: first tests |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Install Playwright with proper project configuration
- Setup **production-ready conftest.py**
- Write first browser automation
- Understand environment configuration

---

## Setup

```powershell
pip install pytest-playwright
playwright install
```

---

## 🔴 CRITICAL: Project Configuration

### pytest.ini

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

### tests/conftest.py (Production-ready)

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
    """Configure browser context for all tests."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "ignore_https_errors": True,
        "record_video_dir": "test-results/videos",
    }

@pytest.fixture(scope="session")
def base_url():
    """Base URL from environment or default."""
    return os.getenv("BASE_URL", "https://the-internet.herokuapp.com")

# ============ Enhanced Page Fixture ============

@pytest.fixture
def page(page: Page, base_url: str) -> Generator[Page, None, None]:
    """Enhanced page fixture with default timeout and console logging."""
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    
    console_errors = []
    page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)
    
    yield page
    
    if console_errors:
        print(f"\n⚠️ Console errors: {console_errors}")

# ============ Screenshot on Failure ============

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Take screenshot on test failure."""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            os.makedirs("test-results/screenshots", exist_ok=True)
            page.screenshot(path=f"test-results/screenshots/{item.name}.png")

# ============ Test Data Fixtures ============

@pytest.fixture
def valid_credentials():
    return {"username": "tomsmith", "password": "SuperSecretPassword!"}

@pytest.fixture
def invalid_credentials():
    return {"username": "invalid_user", "password": "wrong_password"}
```

---

## Session: First Tests

```python
# tests/test_first_automation.py
"""First Playwright automation"""
from playwright.sync_api import Page, expect

def test_google_homepage(page: Page):
    """Navigate to Google and verify title"""
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_search_automation_testing(page: Page):
    """Search for automation testing"""
    page.goto("https://www.google.com")
    
    search_box = page.locator("textarea[name='q']")
    search_box.fill("automation testing")
    search_box.press("Enter")
    
    page.wait_for_load_state("networkidle")
    expect(page.locator("#search")).to_be_visible()

def test_playwright_docs(page: Page):
    """Navigate Playwright documentation"""
    page.goto("https://playwright.dev")
    page.get_by_role("link", name="Docs").click()
    expect(page).to_have_url_pattern(".*docs.*")
```

---

## Running Tests

```powershell
# Run with browser visible
pytest tests/test_first_automation.py --headed -v

# Run with different browser
pytest tests/ --browser firefox -v

# Run with different base URL
$env:BASE_URL="https://staging.example.com"; pytest tests/ -v

# Generate trace for debugging
pytest tests/test_first_automation.py --tracing=on

# View trace file
playwright show-trace test-results/trace.zip
```

---

## Practice Exercise

Write tests for <https://the-internet.herokuapp.com>:

```python
# tests/test_internet.py
from playwright.sync_api import Page, expect

def test_homepage_loads(page: Page):
    """Test that homepage loads successfully"""
    # TODO: Navigate and verify title contains "Internet"
    pass

def test_navigate_to_login(page: Page):
    """Test navigation to Form Authentication"""
    # TODO: Click link, verify URL contains "login"
    pass

def test_login_page_elements(page: Page):
    """Test login page has required fields"""
    # TODO: Verify username and password inputs exist
    pass
```

---

## Homework (2 hours)

### Reading

1. [Playwright Python Getting Started](https://playwright.dev/python/docs/intro)
2. [pytest-playwright Plugin](https://playwright.dev/python/docs/test-runners)

### Coding Tasks

1. **First Test Suite:** Write 5 navigation tests for different pages on the-internet.herokuapp.com
2. **Screenshot on Fail:** Verify conftest.py captures screenshots when tests fail
3. **Explore Options:** Try these flags:
   - `--headed` (watch browser)
   - `--slowmo=500` (slow down actions)
   - `--browser firefox` (different browser)

### Quiz Yourself

1. What's the difference between `page.goto()` and `page.wait_for_url()`?
2. Why do we set `default_timeout` in conftest.py?
3. What does `expect(page).to_have_title()` do?
4. How do you run tests with the browser visible?

---

[← Week 2 Project](../week-2/day-10-project.md) | [Next: Day 12 - Locators →](day-12-locators.md)

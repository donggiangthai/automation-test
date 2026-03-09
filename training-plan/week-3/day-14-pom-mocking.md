# Day 14: Page Object Model & Network Mocking

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | POM pattern introduction |
| 20 min | Network mocking concepts |
| 30 min | Hands-on demo (follow along) |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Implement POM pattern
- Create maintainable test structure
- **Master Network Mocking** (stable, fast tests!)

---

## 🔴 CRITICAL: Network-First Pattern

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
└─────────────────────────────────────────────────────────────────┘
```

---

## Network Mocking Examples

```python
# tests/test_network_mocking.py
from playwright.sync_api import Page, Route, expect
import json

def test_mock_api_success(page: Page):
    """Mock API to return success response"""
    
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
    
    # Setup intercept BEFORE navigation
    page.route("**/api/login", handle_login)
    
    # Then navigate
    page.goto("https://example.com/login")
    # Test will use mocked response!

def test_mock_api_error(page: Page):
    """Mock API to return error"""
    page.route("**/api/login", lambda route: route.fulfill(
        status=401,
        content_type="application/json",
        body=json.dumps({"error": "Invalid credentials"})
    ))
    
    page.goto("https://example.com/login")
    # Verify error handling UI

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
    expect(page.locator(".product-card")).to_have_count(2)
```

---

## Page Object Model

### Base Page

```python
# pages/base_page.py
from playwright.sync_api import Page, expect
import os

class BasePage:
    BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate_to(self, path: str):
        self.page.goto(f"{self.BASE_URL}{path}")
        return self
    
    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")
        return self
```

### Login Page

```python
# pages/login_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "/login"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = page.locator("#username")
        self.password_input = page.locator("#password")
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
        if message:
            expect(self.flash_message).to_contain_text(message)
        return self
    
    def logout(self):
        self.logout_button.click()
        return self
```

### Tests Using POM

```python
# tests/test_login_pom.py
import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

class TestLogin:
    @pytest.mark.smoke
    def test_successful_login(self, login_page: LoginPage):
        login_page.navigate()
        login_page.login("tomsmith", "SuperSecretPassword!")
        login_page.expect_success()
    
    @pytest.mark.regression
    def test_invalid_username(self, login_page: LoginPage):
        login_page.navigate()
        login_page.login("invalid", "SuperSecretPassword!")
        login_page.expect_error("Your username is invalid")
```

---

## Practice Exercise

Create a Page Object for: <https://the-internet.herokuapp.com/add_remove_elements/>

```python
# pages/elements_page.py
from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class ElementsPage(BasePage):
    URL = "/add_remove_elements/"
    
    def __init__(self, page: Page):
        super().__init__(page)
        # TODO: Define locators
        self.add_button = ...
        self.delete_buttons = ...
    
    def navigate(self):
        # TODO: Implement
        pass
    
    def add_element(self):
        # TODO: Click add button
        pass
    
    def delete_element(self):
        # TODO: Click first delete button
        pass
    
    def get_element_count(self) -> int:
        # TODO: Return count of delete buttons
        pass
```

---

## Homework (2 hours)

### Reading

1. [Page Object Model Pattern](https://playwright.dev/python/docs/pom)
2. [Network Mocking](https://playwright.dev/python/docs/network)

### Coding Tasks

1. **POM Suite:** Create Page Objects for 3 pages:
   - LoginPage (done in demo)
   - CheckboxPage
   - DropdownPage

2. **Network Mocking:** Write tests that:
   - Mock successful API responses
   - Mock error responses (401, 500)
   - Mock slow responses (with delay)

3. **Combined Tests:** Create tests using POM + mocking together

### Quiz Yourself

1. What are the benefits of Page Object Model?
2. Why setup network intercepts BEFORE navigation?
3. How do you mock different HTTP status codes?
4. When should you use fluent interface (return self)?

---

[← Day 13](day-13-actions-waits.md) | [Next: Day 15 - Week 3 Project →](day-15-project.md)

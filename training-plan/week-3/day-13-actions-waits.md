# Day 13: Actions, Assertions & Wait Strategies

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Actions overview |
| 15 min | Assertions & expect API |
| 25 min | Wait strategies (CRITICAL!) |
| 20 min | Hands-on demo |
| 20 min | Practice exercise |

---

## Objectives

- Perform all common user actions
- Write meaningful assertions
- **Master wait strategies** (avoid flaky tests!)
- **Handle errors gracefully**

---

## Common Actions

```python
# tests/test_actions.py
from playwright.sync_api import Page, expect

def test_text_input_actions(page: Page):
    """Various ways to input text"""
    page.goto("https://the-internet.herokuapp.com/inputs")
    
    input_field = page.locator("input[type='number']")
    
    input_field.fill("12345")           # Fill - clears and types
    input_field.clear()                 # Clear
    input_field.type("67890", delay=100) # Type char by char
    input_field.press("Backspace")      # Press key
    input_field.press("Control+a")      # Select all

def test_click_actions(page: Page):
    """Various click actions"""
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    
    add_button = page.get_by_role("button", name="Add Element")
    
    add_button.click()                  # Single click
    add_button.dblclick()               # Double click
    # add_button.click(button="right")  # Right click

def test_checkbox_and_radio(page: Page):
    """Handle checkboxes"""
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    
    checkboxes = page.locator("input[type='checkbox']")
    checkboxes.first.check()
    checkboxes.last.uncheck()
    
    expect(checkboxes.first).to_be_checked()

def test_dropdown_selection(page: Page):
    """Handle dropdowns"""
    page.goto("https://the-internet.herokuapp.com/dropdown")
    
    dropdown = page.locator("#dropdown")
    dropdown.select_option("1")              # By value
    dropdown.select_option(label="Option 2") # By label
    
    expect(dropdown).to_have_value("2")

def test_hover_action(page: Page):
    """Mouse hover"""
    page.goto("https://the-internet.herokuapp.com/hovers")
    page.locator(".figure").first.hover()
    expect(page.get_by_text("name: user1")).to_be_visible()
```

---

## Assertions

```python
def test_assertions_examples(page: Page):
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

---

## 🔴 CRITICAL: Wait Strategies

```python
# tests/test_wait_strategies.py
from playwright.sync_api import Page, expect
import pytest

# ❌ BAD: Hard-coded wait (NEVER DO THIS!)
def test_bad_wait_example(page: Page):
    import time
    page.goto("/slow-loading-page")
    time.sleep(5)  # ❌ Wastes time!

# ✅ GOOD: Wait for specific condition
def test_wait_for_element(page: Page):
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")
    page.get_by_role("button", name="Start").click()
    
    # Auto-waits up to timeout
    expect(page.locator("#finish h4")).to_be_visible()
    expect(page.locator("#finish h4")).to_have_text("Hello World!")

def test_wait_for_navigation(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    
    with page.expect_navigation():
        page.get_by_role("button", name="Login").click()
    
    expect(page).to_have_url_pattern(".*secure.*")

def test_wait_for_network_idle(page: Page):
    page.goto("https://example.com")
    page.wait_for_load_state("networkidle")

def test_wait_for_api_response(page: Page):
    page.goto("https://example.com")
    
    with page.expect_response("**/api/users") as response_info:
        page.get_by_role("button", name="Load Users").click()
    
    response = response_info.value
    assert response.status == 200
```

### Wait Strategy Decision Guide

| Scenario | Wait Method |
|----------|-------------|
| Element appears | `expect(locator).to_be_visible()` |
| Page navigation | `page.expect_navigation()` |
| API call completes | `page.expect_response(url)` |
| All network done | `page.wait_for_load_state("networkidle")` |
| Custom condition | `locator.wait_for(state="visible")` |

---

## Error Handling

```python
from playwright.sync_api import Page, expect, TimeoutError

def test_element_should_not_exist(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")
    
    # Verify element is NOT visible
    expect(page.locator("#error-message")).not_to_be_visible()
    expect(page.locator(".non-existent")).to_have_count(0)

def test_handle_expected_timeout(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    
    with pytest.raises(TimeoutError):
        page.locator("#never-exists").click(timeout=1000)

def test_conditional_element(page: Page):
    page.goto("https://the-internet.herokuapp.com")
    
    popup = page.locator("#optional-popup")
    if popup.is_visible():
        popup.locator("button.close").click()
```

---

## Practice Exercise

Write tests for https://the-internet.herokuapp.com/dynamic_loading/2:

```python
# tests/test_dynamic_loading.py
from playwright.sync_api import Page, expect

def test_dynamic_loading(page: Page):
    """Test dynamic content loading WITHOUT time.sleep!"""
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    # TODO: Click "Start" button
    # TODO: Wait for loading to complete (use expect!)
    # TODO: Verify "Hello World!" appears
    pass

def test_checkbox_interactions(page: Page):
    """Test all checkbox states"""
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # TODO: Check first, uncheck second, verify states
    pass

def test_dropdown_selection(page: Page):
    """Test dropdown selection"""
    page.goto("https://the-internet.herokuapp.com/dropdown")
    # TODO: Select options by value and label, verify selection
    pass
```

---

## Homework (2 hours)

### Reading
1. [Playwright Actions](https://playwright.dev/python/docs/input)
2. [Playwright Assertions](https://playwright.dev/python/docs/test-assertions)
3. [Auto-waiting](https://playwright.dev/python/docs/actionability)

### Coding Tasks
1. **Action Suite:** Write tests covering:
   - Text input (fill, type, clear)
   - Click variations (single, double, right)
   - Checkboxes and dropdowns
   - Hover actions

2. **Wait Practice:** Create tests for:
   - Dynamic loading pages
   - AJAX content
   - Page navigation

3. **Error Handling:** Write tests that:
   - Verify element NOT visible
   - Handle expected timeouts
   - Check conditional elements

### Quiz Yourself
1. Why is `time.sleep()` bad in automation?
2. What's the difference between `fill()` and `type()`?
3. How does Playwright auto-wait work?
4. When would you use `expect_navigation()`?

---

[← Day 12](day-12-locators.md) | [Next: Day 14 - POM & Network Mocking →](day-14-pom-mocking.md)

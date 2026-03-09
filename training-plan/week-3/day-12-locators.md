# Day 12: Locators - Your DevTools Skills Shine

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Locator strategies overview |
| 20 min | Locator decision guide |
| 30 min | Hands-on demo with DevTools |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Use modern Playwright locators
- Apply DevTools knowledge
- Learn when to use each locator strategy

---

## Session

```python
# tests/test_locators.py
"""Locator strategies - organized by reliability"""
from playwright.sync_api import Page, expect

def test_role_based_locators(page: Page):
    """
    BEST: Role-based locators - most reliable
    """
    page.goto("https://the-internet.herokuapp.com/login")
    
    username_input = page.get_by_role("textbox", name="Username")
    password_input = page.get_by_role("textbox", name="Password")
    login_button = page.get_by_role("button", name="Login")
    
    username_input.fill("tomsmith")
    password_input.fill("SuperSecretPassword!")
    login_button.click()
    
    expect(page.get_by_role("heading", name="Secure Area")).to_be_visible()

def test_text_based_locators(page: Page):
    """GOOD: Text-based locators"""
    page.goto("https://the-internet.herokuapp.com")
    page.get_by_text("Form Authentication").click()
    expect(page).to_have_url_pattern(".*login.*")

def test_label_and_placeholder_locators(page: Page):
    """GOOD: Label and placeholder locators"""
    page.goto("https://the-internet.herokuapp.com/login")
    page.get_by_placeholder("Username").fill("tomsmith")
    page.get_by_placeholder("Password").fill("SuperSecretPassword!")

def test_css_selectors(page: Page):
    """FALLBACK: CSS selectors"""
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.locator("#username").fill("tomsmith")
    page.locator("button.radius").click()
    page.locator("input[name='password']").fill("SuperSecretPassword!")
    page.locator("form#login button[type='submit']").click()

def test_test_id_locators(page: Page):
    """RECOMMENDED: data-testid attributes"""
    # If your app uses data-testid:
    # page.get_by_test_id("login-button").click()
    pass
```

---

## 🔴 CRITICAL: Locator Decision Guide

```
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
│  🔧 Icon-only buttons (no text)                                │
│  🔧 Multiple similar elements (list items, table rows)         │
│  🔧 Dynamic/generated content                                   │
│  🔧 Elements that frequently change text                       │
│                                                                 │
│  ❌ AVOID CSS SELECTORS FOR:                                    │
│  - Styling classes (.btn-primary, .card)                       │
│  - Generated IDs (#ember123, #react-component-456)             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Locator Priority (Best to Worst)

| Priority | Method | Example |
|----------|--------|---------|
| 1 | Role-based | `get_by_role("button", name="Submit")` |
| 2 | Label | `get_by_label("Email")` |
| 3 | Placeholder | `get_by_placeholder("Enter email")` |
| 4 | Text | `get_by_text("Welcome")` |
| 5 | Test ID | `get_by_test_id("submit-btn")` |
| 6 | CSS/XPath | `locator("#username")` |

---

## Practical Examples

```python
def test_button_with_text(page: Page):
    """Button has visible text → use role"""
    # ✅ GOOD
    page.get_by_role("button", name="Login").click()
    
    # ❌ AVOID
    # page.locator(".btn-login").click()

def test_icon_button_no_text(page: Page):
    """Icon button without text → need data-testid"""
    # ✅ GOOD
    page.get_by_test_id("close-modal").click()

def test_list_items(page: Page):
    """Multiple similar items → use data-testid with ID"""
    # ✅ GOOD
    page.get_by_test_id("product-row-SKU123").click()
    
    # ⚠️ AVOID nth()
    # page.locator(".product-row").nth(2).click()

def test_form_with_labels(page: Page):
    """Form inputs with labels → use get_by_label"""
    # ✅ GOOD
    page.get_by_label("Email Address").fill("test@example.com")
```

---

## Practice Exercise

Use DevTools to find locators for these pages:

```python
# tests/test_locator_practice.py
from playwright.sync_api import Page, expect

def test_login_form(page: Page):
    """Find best locators for login form"""
    page.goto("https://the-internet.herokuapp.com/login")
    
    # TODO: Use role-based locators
    username = page.get_by_role(...)  # Find the best locator
    password = page.get_by_role(...)  
    login_btn = page.get_by_role(...)

def test_add_element_button(page: Page):
    "/add_remove_elements/ page"""
    page.goto("https://the-internet.herokuapp.com/add_remove_elements/")
    # TODO: Find best locator for "Add Element" button

def test_dropdown(page: Page):
    """Find locator for dropdown at /dropdown"""
    page.goto("https://the-internet.herokuapp.com/dropdown")
    # TODO: Select "Option 2" using best locator
```

---

## Homework (2 hours)

### Reading
1. [Playwright Locators](https://playwright.dev/python/docs/locators)
2. [Best Practices - Locators](https://playwright.dev/python/docs/best-practices#use-locators)

### Coding Tasks
1. **Locator Audit:** Review 5 existing tests and improve their locators
2. **DevTools Practice:** Use browser DevTools to find locators for 10 elements on different sites
3. **Create Cheatsheet:** Document your preferred locator patterns for common elements:
   - Buttons with text
   - Icon-only buttons
   - Form inputs with labels
   - Links
   - Tables

### Quiz Yourself
1. What's the priority order for locator strategies?
2. When should you use `data-testid` vs role-based locators?
3. Why avoid CSS class selectors like `.btn-primary`?
4. How do you handle elements with dynamic IDs?

---

[← Day 11](day-11-playwright-setup.md) | [Next: Day 13 - Actions & Waits →](day-13-actions-waits.md)

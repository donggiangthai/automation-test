# Day 15: Week 3 Project - E2E Test Suite

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | Week 3 concepts recap |
| 15 min | Project requirements review |
| 45 min | Mini-project implementation |
| 15 min | Code review & improvements |
| 5 min | Week 4 preview |

---

## Objectives

- Complete E2E test suite for mock application
- Apply ALL Playwright concepts learned
- Demonstrate mastery before Week 4

---

## Project: E2E Test Suite for Mock Project

```text
automation-test/
├── e2e-tests/
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── product_page.py
│   │   ├── inventory_page.py
│   │   └── order_page.py
│   ├── tests/
│   │   ├── conftest.py
│   │   ├── test_products.py
│   │   ├── test_inventory.py
│   │   └── test_orders.py
│   └── pytest.ini
```

---

## Deliverables

### 1. Page Objects (3 required)

```python
# pages/product_page.py
class ProductPage(BasePage):
    URL = "/products"
    
    def __init__(self, page: Page):
        super().__init__(page)
        self.add_button = page.get_by_role("button", name="Add Product")
        self.search_input = page.get_by_placeholder("Search")
        self.product_table = page.locator("table")
        self.product_rows = page.locator("table tbody tr")
    
    def navigate(self):
        self.navigate_to(self.URL)
        return self
    
    def add_product(self, name: str, category: str, price: float):
        self.add_button.click()
        # Fill form...
        return self
    
    def search(self, query: str):
        self.search_input.fill(query)
        return self
    
    def get_product_count(self) -> int:
        return self.product_rows.count()
```

### 2. Test Suite Requirements

- ✅ **8+ test cases minimum**
- ✅ **Use network mocking** for API responses
- ✅ **Use parametrize** for multiple data scenarios
- ✅ **Use markers** (smoke, regression, slow)
- ✅ **Use fixtures** for setup/teardown

### 3. Test Scenarios

```python
# tests/test_products.py
@pytest.mark.smoke
def test_product_page_loads(product_page):
    """Verify product page loads correctly"""
    product_page.navigate()
    expect(product_page.product_table).to_be_visible()

@pytest.mark.regression
@pytest.mark.parametrize("name,category,price", [
    ("Test Product", "Electronics", 99.99),
    ("Another Item", "Clothing", 49.99),
])
def test_add_product(product_page, name, category, price):
    """Test adding products with different data"""
    pass

@pytest.mark.smoke
def test_product_list_with_mock(page: Page, product_page):
    """Test with mocked API"""
    mock_products = [
        {"id": 1, "name": "Mock Product", "price": 10.00}
    ]
    page.route("**/api/products", lambda route: route.fulfill(
        status=200,
        body=json.dumps(mock_products)
    ))
    product_page.navigate()
    expect(product_page.product_rows).to_have_count(1)
```

---

## Evaluation Criteria

| Criteria | Points |
| ---------- | -------- |
| Page Objects implemented correctly | 25 |
| 8+ test cases working | 25 |
| Network mocking used | 20 |
| Parametrize applied | 15 |
| Markers and fixtures | 15 |
| **Total** | **100** |

---

## Session Activity

1. **First 30 min:** Create page objects structure
2. **Next 30 min:** Implement first 4 test cases
3. **Final 30 min:** Add mocking & review

---

## Homework (2 hours)

### Extend the Project

1. Add 4 more test cases to reach 12 total
2. Add error scenario tests (mocked 500 errors)
3. Add visual regression test (screenshot comparison)

### Week 3 Self-Assessment

Complete all checklist items:

- [ ] Playwright setup with production conftest.py
- [ ] Role-based locators preferred
- [ ] No time.sleep() in tests
- [ ] POM pattern implemented
- [ ] Network mocking used
- [ ] Tests organized with markers

### Prepare for Week 4

1. Get GitHub Copilot access (free trial or subscription)
2. Install VS Code extensions: GitHub Copilot, GitHub Copilot Chat
3. Preview: Think about how AI can help write tests faster

---

[← Day 14](day-14-pom-mocking.md) | [Week 4 →](../week-4/day-16-copilot-setup.md)

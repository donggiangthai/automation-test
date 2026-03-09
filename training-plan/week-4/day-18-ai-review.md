# Day 18: AI-Assisted Code Review

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Topic | Activity |
|------|-------|----------|
| 0:00-0:10 | Recap & Code Review Introduction | Discussion |
| 0:10-0:30 | Review Workflow with Copilot | Demo |
| 0:30-0:50 | Review Prompts: Quality, Coverage, Performance | Hands-on |
| 0:50-1:10 | Common Issues AI Catches | Practice |
| 1:10-1:25 | Practice Exercise: Review Challenge | Hands-on |
| 1:25-1:30 | Q&A & Homework Review | Discussion |

---

## Objectives

- Use AI for test code review
- Identify quality issues automatically
- Improve code through AI suggestions

---

## Visual Concept: AI Code Review Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                  AI Review Pipeline                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐ │
│   │ Select  │    │ Ask for │    │ Review  │    │ Apply   │ │
│   │ Code    │ ─► │ Review  │ ─► │ Results │ ─► │ Fixes   │ │
│   └─────────┘    └─────────┘    └─────────┘    └─────────┘ │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│   Common Issues AI Catches:                                 │
│                                                             │
│   • Missing Assertions  ──► "Test has no expect()"          │
│   • Hard-coded Data     ──► "Use parametrize instead"       │
│   • Flaky Patterns      ──► "Replace sleep with waits"      │
│   • Coverage Gaps       ──► "Missing edge case tests"       │
│   • Performance Issues  ──► "Unnecessary operations"        │
└─────────────────────────────────────────────────────────────┘
```

---

## Code Review with Copilot

### Review Workflow

```
1. Select code block
2. Ctrl+I (inline chat) or Ctrl+L (chat panel)
3. Ask for review:
   - "Review this test for issues"
   - "Suggest improvements"
   - "Check for best practices"
```

---

## Review Prompts

### Test Quality Review

```
Review this test code and identify:
1. Missing assertions
2. Hard-coded values that should be parametrized
3. Setup/teardown that could be fixtures
4. Flaky test patterns
5. Missing edge cases

{paste test code}
```

### Coverage Analysis

```
Analyze this test file and identify:
1. What scenarios are NOT covered?
2. What boundary conditions are missing?
3. What error cases should be tested?

{paste test code}
```

### Performance Review

```
Review this test for performance issues:
1. Unnecessary waits
2. Redundant operations
3. Opportunities for parallelization

{paste test code}
```

---

## Common Issues AI Catches

### 1. Missing Assertions

```python
# Before (AI identifies: no assertion!)
def test_login(page):
    page.fill("#username", "user")
    page.fill("#password", "pass")
    page.click("#login")

# After AI suggestion
def test_login(page):
    page.fill("#username", "user")
    page.fill("#password", "pass")
    page.click("#login")
    expect(page.locator(".welcome")).to_be_visible()  # Added!
```

### 2. Hard-coded Data

```python
# Before
def test_price():
    assert calculate_tax(100) == 10

# After AI suggestion
@pytest.mark.parametrize("amount,expected", [
    (100, 10),
    (200, 20),
    (0, 0),
])
def test_price(amount, expected):
    assert calculate_tax(amount) == expected
```

### 3. Flaky Patterns

```python
# Before (flaky!)
def test_async_operation(page):
    page.click("#start")
    time.sleep(5)  # AI: "Use explicit waits instead"
    assert page.is_visible("#result")

# After AI suggestion
def test_async_operation(page):
    page.click("#start")
    expect(page.locator("#result")).to_be_visible(timeout=5000)
```

---

## Review Checklist

Use AI to verify each item:

- [ ] All tests have meaningful assertions
- [ ] No hardcoded waits (time.sleep)
- [ ] Test data is appropriate (parametrized if needed)
- [ ] Fixtures used for common setup
- [ ] Error messages are descriptive
- [ ] Tests are independent (no order dependency)
- [ ] Resources are cleaned up

---

## Practice Exercise: AI Code Review Challenge (15 min)

**Goal:** Use AI to identify and fix issues in existing tests

```python
# tests/test_review_challenge.py
"""Review this test file and find the issues using AI."""
import time

# Issue 1: Find it using AI
def test_user_login(page):
    page.fill("#username", "user123")
    page.fill("#password", "pass123")
    page.click("#login")
    time.sleep(3)

# Issue 2: Find it using AI
def test_price_calculation():
    result = calculate_total(100, 0.1)
    assert result == 110

# Issue 3: Find it using AI
def test_search_results(page):
    page.fill("#search", "laptop")
    page.click("#search-btn")
    time.sleep(2)
    results = page.locator(".result").count()
    # missing assertion!

# Task: Use Copilot to:
# 1. Review each test and identify issues
# 2. Apply suggested fixes
# 3. Compare before/after quality
```

---

## Homework

### Reading
- [Test Code Anti-patterns](https://blog.codepipes.com/testing/software-testing-antipatterns.html)
- [Effective Code Review](https://google.github.io/eng-practices/review/)

### Coding Tasks
1. **Full Project Review**: Review all Week 3 project tests with AI, apply improvements
2. **Personal Checklist**: Create your own "code review checklist" based on AI suggestions
3. **Comparison Study**: Review the same code manually first, then with AI - note differences

### Quiz Yourself
- What are the 3 most common issues AI catches in test code?
- How can AI help identify coverage gaps?
- What's the difference between /fix and asking for a review?

---

[← Day 17](day-17-prompting.md) | [Next: Day 19 - Workflow Integration →](day-19-integration.md)

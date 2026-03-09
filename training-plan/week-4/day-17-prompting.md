# Day 17: Effective Prompting for QA

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Topic | Activity |
|------|-------|----------|
| 0:00-0:10 | Recap & Introduction to Prompting | Discussion |
| 0:10-0:30 | CRAFT Framework for Prompts | Lecture |
| 0:30-0:50 | QA-Specific Prompt Templates | Demo |
| 0:50-1:10 | Prompt Chaining Techniques | Hands-on |
| 1:10-1:25 | Practice Exercise: Build Prompts | Practice |
| 1:25-1:30 | Q&A & Homework Review | Discussion |

---

## Objectives

- Master prompt engineering for testing
- Learn QA-specific prompt patterns
- Write effective instructions for AI

---

## Visual Concept: CRAFT Framework

```
┌─────────────────────────────────────────────────────────────┐
│                    CRAFT Framework                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   C ─ Context   ──► "Testing a checkout flow"               │
│   │                                                         │
│   ▼                                                         │
│   R ─ Role      ──► "Act as QA engineer"                    │
│   │                                                         │
│   ▼                                                         │
│   A ─ Action    ──► "Generate pytest test cases"            │
│   │                                                         │
│   ▼                                                         │
│   F ─ Format    ──► "Use POM pattern, parametrize"          │
│   │                                                         │
│   ▼                                                         │
│   T ─ Target    ──► "5 positive + 5 negative tests"         │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│   Better Prompt = Better Results                            │
│   • Be specific about technology (pytest, playwright)       │
│   • Include constraints (no hardcoded values)               │
│   • Specify output format (code, list, table)               │
└─────────────────────────────────────────────────────────────┘
```

---

## Prompt Engineering Basics

### The CRAFT Framework

```
C - Context: What's the situation?
R - Role: Who should the AI be?
A - Action: What do you want done?
F - Format: How should output look?
T - Target: What's the expected result?
```

---

## QA-Specific Prompts

### 1. Test Generation

```
PROMPT:
"Generate pytest test cases for a login function.
Context: 
- Function accepts username and password
- Returns True for success, raises AuthError on failure
- Valid credentials: username must be email format, password 8+ chars

Generate:
- 3 positive test cases
- 5 negative test cases
- Use parametrize decorator
- Include docstrings"
```

### 2. Page Object Creation

```
PROMPT:
"Create a Page Object Model for a checkout page with:
- URL: /checkout
- Elements: cart items table, subtotal, shipping dropdown, 
  promo code input, apply button, total, place order button
- Methods: apply_promo(), select_shipping(), place_order()
- Use Playwright with Python
- Follow POM best practices"
```

### 3. Bug Analysis

```
PROMPT:
"Analyze this test failure and suggest fixes:
[paste error message]

Provide:
1. Root cause analysis
2. Possible fixes (ranked by likelihood)
3. Prevention strategies"
```

---

## Prompt Templates for QA

### Test Case Template

```
Generate {test_type} test cases for {feature}.

Context:
- {business_context}
- {technical_constraints}

Requirements:
- Framework: pytest + playwright
- Style: {BDD/TDD/data-driven}
- Coverage: {edge_cases to include}

Output format:
- Python code with docstrings
- Include arrange-act-assert comments
```

### Review Template

```
Review this test code for:
1. Test coverage gaps
2. Assertion quality
3. Maintainability
4. Performance concerns
5. Best practice violations

Code:
{paste code}
```

---

## Prompt Chaining

### Step-by-step approach

```
Step 1:
"Analyze the login page at https://example.com/login
and list all testable elements"

Step 2:
"Based on those elements, create a test plan
covering positive and negative scenarios"

Step 3:
"Generate pytest code for the first 3 test cases
using Page Object Model"
```

---

## Practice Exercise: Build QA Prompts (15 min)

**Goal:** Create effective prompts using the CRAFT framework

```python
# Task 1: Create a CRAFT prompt to generate API test cases
# Target: POST /orders endpoint
# Requirements: Pytest, parametrize, positive/negative cases

# YOUR PROMPT:
"""
C - Context: 
R - Role: 
A - Action: 
F - Format: 
T - Target: 
"""

# Task 2: Create a prompt chain for building a Login Page Object
# Step 1: Analyze requirements
# Step 2: Generate page object class
# Step 3: Generate test cases using the page object

# Task 3: Create a test fixture generation prompt
# Target: Database setup fixture with SQLAlchemy
```

---

## Homework

### Reading
- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)
- [GitHub Copilot Best Practices](https://docs.github.com/en/copilot/using-github-copilot)

### Coding Tasks
1. **Prompt Library**: Create 5 custom prompt templates for different QA scenarios
2. **Iterative Refinement**: Take one prompt and iterate 3 times, improving output each time
3. **Comparison Study**: Write the same test 3 ways using different prompt styles, compare results

### Quiz Yourself
- What does each letter in CRAFT stand for?
- Why is prompt chaining useful for complex tasks?
- What information should you always include in a QA prompt?

---

[← Day 16](day-16-copilot-setup.md) | [Next: Day 18 - AI-Assisted Code Review →](day-18-ai-review.md)

# Day 2: Control Flow - Making Decisions

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | Review Day 1 & intro |
| 20 min | Comparison & logical operators |
| 30 min | Hands-on demo (follow along) |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Use if/elif/else statements
- Apply comparison operators
- Write basic test validations

---

## Visual Concept

```text
┌─────────────────────────────────────────────────────────────┐
│                    CONTROL FLOW                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    ┌───────────┐                            │
│                    │ Condition │                            │
│                    └─────┬─────┘                            │
│                          │                                  │
│              ┌───────────┴───────────┐                      │
│              ▼                       ▼                      │
│         ┌────────┐             ┌────────┐                   │
│         │  True  │             │ False  │                   │
│         └────┬───┘             └────┬───┘                   │
│              ▼                      ▼                       │
│         ┌────────┐             ┌────────┐                   │
│         │ Do X   │             │ Do Y   │                   │
│         └────────┘             └────────┘                   │
│                                                             │
│   Code Pattern:                                             │
│   ┌─────────────────────────────────────────────┐          │
│   │ if condition:      # Check first             │          │
│   │     do_this()                                │          │
│   │ elif other_cond:   # Check if first failed   │          │
│   │     do_that()                                │          │
│   │ else:              # All checks failed       │          │
│   │     do_default()                             │          │
│   └─────────────────────────────────────────────┘          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

```python
# validation_tests.py
# Testing login validation logic

def validate_login(username, password):
    """
    Simulate login validation - this is what we'll automate later
    """
    # Test case 1: Empty username
    if not username:
        return "Error: Username required"
    
    # Test case 2: Empty password
    if not password:
        return "Error: Password required"
    
    # Test case 3: Username too short
    if len(username) < 3:
        return "Error: Username must be at least 3 characters"
    
    # Test case 4: Password requirements
    if len(password) < 8:
        return "Error: Password must be at least 8 characters"
    
    # Test case 5: Valid credentials (mock check)
    valid_users = {"admin": "Admin123!", "testuser": "Test@123"}
    if username in valid_users and valid_users[username] == password:
        return "Login successful"
    
    return "Error: Invalid credentials"

# Run test cases
test_cases = [
    ("", "password"),           # Empty username
    ("admin", ""),              # Empty password
    ("ab", "password123"),      # Short username
    ("admin", "short"),         # Short password
    ("admin", "Admin123!"),     # Valid login
    ("admin", "wrongpass"),     # Wrong password
]

print("Running login validation tests:\n")
for username, password in test_cases:
    result = validate_login(username, password)
    print(f"Test: username='{username}', password='{password}'")
    print(f"Result: {result}\n")
```

---

## Key Concepts

### Comparison Operators

| Operator | Meaning | Example |
| ---------- | --------- | --------- |
| `==` | Equal | `x == 5` |
| `!=` | Not equal | `x != 5` |
| `<` | Less than | `x < 5` |
| `>` | Greater than | `x > 5` |
| `<=` | Less or equal | `x <= 5` |
| `>=` | Greater or equal | `x >= 5` |

### Logical Operators

| Operator | Meaning | Example |
| ---------- | --------- | --------- |
| `and` | Both true | `x > 0 and x < 10` |
| `or` | Either true | `x < 0 or x > 10` |
| `not` | Negation | `not x` |

### Truthy/Falsy Values

```python
# Falsy values (evaluate to False)
if not "":          # Empty string
if not 0:           # Zero
if not None:        # None
if not []:          # Empty list
if not {}:          # Empty dict

# Truthy values (evaluate to True)
if "hello":         # Non-empty string
if 42:              # Non-zero number
if [1, 2, 3]:       # Non-empty list
```

---

## Practice Exercise

Add validation for email format:

```python
# exercise_day2.py
def validate_email(email):
    """
    Return True if email is valid, False otherwise.
    Valid email must:
    - Not be empty
    - Contain exactly one @
    - Have text before and after @
    - Have a . after the @
    """
    # TODO: Implement validation logic
    pass

# Test your function with these cases:
test_emails = [
    ("user@example.com", True),      # Valid
    ("user@domain.co.uk", True),     # Valid
    ("invalid-email", False),        # Invalid - no @
    ("@example.com", False),         # Invalid - no local part
    ("user@", False),                # Invalid - no domain
    ("", False),                     # Invalid - empty
]

for email, expected in test_emails:
    result = validate_email(email)
    status = "✅" if result == expected else "❌"
    print(f"{status} {email}: {result}")
```

---

## Homework (2 hours)

### Reading

1. [Python If...Else](https://www.w3schools.com/python/python_conditions.asp)
2. [Python Operators](https://www.w3schools.com/python/python_operators.asp)

### Coding Tasks

1. **Grade Calculator:** Write a function that converts score (0-100) to letter grade (A, B, C, D, F)
2. **Number Guessing Game:** Create a game that tells user "higher/lower" until they guess correctly
3. **Password Strength Checker:** Check if password has uppercase, lowercase, number, and special char

### Quiz Yourself

1. What's the difference between `==` and `=`?
2. When does an `elif` block execute?
3. What values are considered "falsy" in Python?
4. What does `and` vs `or` return?

---

[← Day 1](day-01-variables.md) | [Next: Day 3 - Functions →](day-03-functions.md)

# Day 1: Python Basics - Variables & Data Types

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Introduction & setup verification |
| 20 min | Variables & data types theory |
| 30 min | Hands-on demo (follow along) |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Write first Python program
- Understand variables, strings, numbers, booleans
- Use print() and input()

---

## Visual Concept

```
┌─────────────────────────────────────────────────────────────┐
│                    PYTHON VARIABLES                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Variable = "container" that stores data                   │
│                                                             │
│   ┌───────────┐    ┌───────────┐    ┌───────────┐         │
│   │  username │    │   price   │    │ is_valid  │         │
│   │  ───────  │    │  ───────  │    │  ───────  │         │
│   │  "admin"  │    │   99.99   │    │   True    │         │
│   │   (str)   │    │  (float)  │    │  (bool)   │         │
│   └───────────┘    └───────────┘    └───────────┘         │
│                                                             │
│   Data Types:                                               │
│   • str   → Text: "hello", 'world'                         │
│   • int   → Whole numbers: 42, -7                          │
│   • float → Decimals: 3.14, 99.99                          │
│   • bool  → True / False                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

```python
# hello_test.py
# Your first Python program

# Variables - like test data storage
test_username = "admin"
test_password = "P@ssw0rd123"
is_valid_user = True
login_attempts = 3

# Print - useful for debugging tests
print("Testing login with:", test_username)
print(f"Valid user: {is_valid_user}")  # f-string formatting

# Input - interactive testing
user_input = input("Enter username to test: ")
print(f"You entered: {user_input}")

# Basic operations
total_tests = 50
passed_tests = 45
pass_rate = (passed_tests / total_tests) * 100
print(f"Pass rate: {pass_rate}%")
```

---

## Key Concepts

### Variable Types

| Type | Example | Use Case |
|------|---------|----------|
| `str` | `"admin"` | Usernames, passwords, text |
| `int` | `42` | Counts, IDs |
| `float` | `99.99` | Prices, percentages |
| `bool` | `True`/`False` | Flags, conditions |

### f-strings (Formatted Strings)

```python
name = "Test User"
age = 25

# Old way
print("Name: " + name + ", Age: " + str(age))

# f-string way (preferred)
print(f"Name: {name}, Age: {age}")
```

---

## Practice Exercise

Create variables for a test scenario - user registration:

```python
# exercise_day1.py
# TODO: Create these variables:
# - first_name (string)
# - last_name (string)  
# - email (string)
# - age (integer)
# - is_premium (boolean)
# - account_balance (float)

# TODO: Print them all using f-strings
# Example output:
# User: John Doe (john@test.com)
# Age: 25, Premium: True
# Balance: $150.50
```

**Solution hint:** Use `type(variable)` to verify your data types!

---

## Homework (2 hours)

### Reading & Practice
1. Complete Python basics on [W3Schools - Variables](https://www.w3schools.com/python/python_variables.asp)
2. Read about [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)

### Coding Tasks
1. Create 5 different variables of each type (str, int, float, bool)
2. Write a program that calculates test pass rate from user input
3. Create a "test report" that prints formatted statistics

### Quiz Yourself
1. What's the difference between `"42"` and `42`?
2. How do you check the type of a variable? (hint: `type()`)
3. What does `f"..."` mean in Python?
4. What happens when you add `"5" + "3"`? Why?

---

[← Environment Setup](../00-environment-setup.md) | [Next: Day 2 - Control Flow →](day-02-control-flow.md)

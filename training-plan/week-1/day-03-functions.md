# Day 3: Functions - Reusable Test Helpers

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | Review Day 2 & intro |
| 20 min | Function concepts & syntax |
| 30 min | Hands-on demo (follow along) |
| 20 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Create functions with parameters
- Return values
- Build test utility functions

---

## Visual Concept

```text
┌─────────────────────────────────────────────────────────────┐
│                    FUNCTIONS                                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Function = Reusable block of code                         │
│                                                             │
│   ┌─────────────────────────────────────────────────────┐  │
│   │  def function_name(parameters):                      │  │
│   │      """What this function does"""                   │  │
│   │      # Do something                                  │  │
│   │      return result                                   │  │
│   └─────────────────────────────────────────────────────┘  │
│                                                             │
│   Example:                                                  │
│                                                             │
│   Input         Function             Output                 │
│   ┌─────┐      ┌──────────────┐     ┌─────────────────┐    │
│   │"abc"│ ───► │generate_email│ ──► │"abc@test.com"  │    │
│   └─────┘      └──────────────┘     └─────────────────┘    │
│                                                             │
│   Why use functions?                                        │
│   • Reuse code (DRY - Don't Repeat Yourself)               │
│   • Easy to test                                            │
│   • Organized & readable                                    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

```python
# test_helpers.py
# Functions you'll use in real automation

import random
import string

def generate_random_email(domain="test.com"):
    """Generate unique email for test user"""
    random_string = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"user_{random_string}@{domain}"

def generate_random_password(length=12):
    """Generate password meeting requirements"""
    chars = string.ascii_letters + string.digits + "!@#$%"
    password = ''.join(random.choices(chars, k=length))
    return password

def create_test_user():
    """Create complete test user data"""
    return {
        "email": generate_random_email(),
        "password": generate_random_password(),
        "first_name": f"Test_{random.randint(1000, 9999)}",
        "last_name": "User"
    }

def assert_equals(actual, expected, message=""):
    """Custom assertion - similar to what pytest does"""
    if actual == expected:
        print(f"✅ PASS: {message}")
        return True
    else:
        print(f"❌ FAIL: {message}")
        print(f"   Expected: {expected}")
        print(f"   Actual: {actual}")
        return False

# Test our helpers
print("Generated emails:")
for i in range(3):
    print(f"  {generate_random_email()}")

print("\nGenerated passwords:")
for i in range(3):
    print(f"  {generate_random_password()}")

print("\nTest user:")
user = create_test_user()
for key, value in user.items():
    print(f"  {key}: {value}")

# Using our assertion
print("\nTesting assertions:")
assert_equals(2 + 2, 4, "Basic math")
assert_equals("hello".upper(), "HELLO", "String uppercase")
assert_equals(len([1, 2, 3]), 3, "List length")
```

---

## Key Concepts

### Function Syntax

```python
def function_name(param1, param2="default"):
    """Docstring explaining what function does"""
    # Function body
    result = param1 + param2
    return result
```

### Parameters vs Arguments

```python
# Parameters: variables in function definition
def greet(name, greeting="Hello"):  # name, greeting are parameters
    return f"{greeting}, {name}!"

# Arguments: values passed when calling function
greet("Thai")                 # "Thai" is an argument
greet("Thai", "Hi")          # "Thai", "Hi" are arguments
greet(name="Thai")           # Keyword argument
```

### Return Values

```python
# Single return
def add(a, b):
    return a + b

# Multiple returns (tuple)
def get_user_info():
    return "John", 25, "john@test.com"

name, age, email = get_user_info()

# No return (implicitly returns None)
def print_message(msg):
    print(msg)
    # No return statement
```

---

## Practice Exercise

Create a function `validate_email(email)`:

```python
# exercise_day3.py
def validate_email(email):
    """
    Validate email format.
    
    Args:
        email: String to validate
        
    Returns:
        True if valid email format, False otherwise
    """
    # TODO: Implement
    # Must contain @
    # Must have text before and after @
    # Must have . after @
    pass

# Test your function
test_cases = [
    ("user@example.com", True),
    ("invalid", False),
    ("@domain.com", False),
    ("user@", False),
    ("", False),
]

for email, expected in test_cases:
    result = validate_email(email)
    status = "✅" if result == expected else "❌"
    print(f"{status} validate_email('{email}') = {result}")
```

---

## Homework (2 hours)

### Reading

1. [Python Functions](https://www.w3schools.com/python/python_functions.asp)
2. [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)

### Coding Tasks

1. **Test Data Generator:** Create 5 utility functions:
   - `generate_random_string(length)`
   - `generate_random_email(domain)`
   - `generate_random_phone()`
   - `generate_random_price(min, max)`
   - `generate_test_user()`

2. **Calculator Module:** Create a module with `add`, `subtract`, `multiply`, `divide` functions

3. **Validation Suite:** Create functions to validate:
   - Password strength
   - Phone number format
   - Credit card format (simple)

### Quiz Yourself

1. What's the difference between parameters and arguments?
2. What does a function return if there's no `return` statement?
3. How do you provide a default value for a parameter?
4. What are `*args` and `**kwargs` used for?

---

[← Day 2](day-02-control-flow.md) | [Next: Day 4 - Collections →](day-04-collections.md)

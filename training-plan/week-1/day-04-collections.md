# Day 4: Lists, Loops & Dictionaries - Test Data Management

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | Review Day 3 & intro |
| 25 min | Lists, dictionaries, loops theory |
| 30 min | Hands-on demo (follow along) |
| 15 min | Practice exercise |
| 10 min | Q&A & recap |

---

## Objectives

- Work with collections
- Iterate through test data
- Store structured test data

---

## Visual Concept

```text
┌─────────────────────────────────────────────────────────────┐
│              COLLECTIONS IN PYTHON                           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  LIST = Ordered collection (like array)                     │
│  ┌───────────────────────────────────────────────────┐     │
│  │ ["admin", "user1", "user2"]                        │     │
│  │    [0]      [1]      [2]                           │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
│  DICTIONARY = Key-Value pairs (like JSON object)            │
│  ┌───────────────────────────────────────────────────┐     │
│  │ {                                                  │     │
│  │   "username": "admin",                             │     │
│  │   "password": "secret",                            │     │
│  │   "role": "admin"                                  │     │
│  │ }                                                  │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
│  LIST of DICTIONARIES = Data-driven test data!              │
│  ┌───────────────────────────────────────────────────┐     │
│  │ [                                                  │     │
│  │   {"user": "admin", "pass": "123", "expect": True},│     │
│  │   {"user": "", "pass": "123", "expect": False},    │     │
│  │ ]                                                  │     │
│  └───────────────────────────────────────────────────┘     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

```python
# test_data_management.py
# Managing test data like a pro

# List of test scenarios
login_test_data = [
    {"username": "admin", "password": "Admin123!", "expected": "success"},
    {"username": "", "password": "Admin123!", "expected": "error"},
    {"username": "admin", "password": "", "expected": "error"},
    {"username": "invalid", "password": "wrong", "expected": "error"},
]

# Running data-driven tests
print("=== Data-Driven Login Tests ===\n")
passed = 0
failed = 0

for test in login_test_data:
    # Simulate test execution
    if test["username"] and test["password"]:
        if test["username"] == "admin" and test["password"] == "Admin123!":
            result = "success"
        else:
            result = "error"
    else:
        result = "error"
    
    # Verify result
    if result == test["expected"]:
        print(f"✅ PASS: username='{test['username']}'")
        passed += 1
    else:
        print(f"❌ FAIL: username='{test['username']}'")
        print(f"   Expected: {test['expected']}, Got: {result}")
        failed += 1

print(f"\n=== Results: {passed} passed, {failed} failed ===")

# Dictionary for page elements (Page Object preview)
login_page_elements = {
    "username_input": "#username",
    "password_input": "#password", 
    "login_button": "button[type='submit']",
    "error_message": ".error-message",
    "success_message": ".welcome-message"
}

print("\n=== Login Page Elements ===")
for name, selector in login_page_elements.items():
    print(f"  {name}: {selector}")
```

---

## Key Concepts

### Lists

```python
# Creating lists
test_users = ["admin", "user1", "user2"]
numbers = [1, 2, 3, 4, 5]

# Accessing elements
first = test_users[0]      # "admin"
last = test_users[-1]      # "user2"

# List methods
test_users.append("user3")          # Add to end
test_users.insert(0, "superadmin")  # Insert at index
test_users.remove("user1")          # Remove by value
popped = test_users.pop()           # Remove and return last

# List operations
length = len(test_users)
is_admin = "admin" in test_users
```

### Dictionaries

```python
# Creating dictionaries
user = {
    "username": "admin",
    "password": "secret",
    "role": "administrator"
}

# Accessing values
username = user["username"]         # Raises KeyError if missing
role = user.get("role", "user")    # Returns default if missing

# Dictionary methods
user["email"] = "admin@test.com"   # Add/update
del user["password"]               # Delete key
keys = user.keys()                 # Get all keys
values = user.values()             # Get all values
items = user.items()               # Get key-value pairs
```

### Loops

```python
# For loop with list
for user in test_users:
    print(user)

# For loop with range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# For loop with enumerate
for index, user in enumerate(test_users):
    print(f"{index}: {user}")

# For loop with dictionary
for key, value in user.items():
    print(f"{key}: {value}")

# List comprehension
emails = [f"{u}@test.com" for u in test_users]
```

---

## Practice Exercise

Create test data for product search:

```python
# exercise_day4.py
# Create test data structure containing:
# - search_term (string)
# - expected_count (integer) 
# - category_filter (string or None)

search_test_data = [
    {"search": "laptop", "expected": 5, "category": "Electronics"},
    {"search": "shirt", "expected": 10, "category": "Clothing"},
    # TODO: Add 3 more test cases
]

# Iterate through and simulate test execution
for test in search_test_data:
    # Simulate: real test would call API/UI
    mock_count = 5  # Pretend this is from actual search
    
    result = "✅ PASS" if mock_count == test["expected"] else "❌ FAIL"
    print(f"{result}: Search '{test['search']}' in {test['category']}")
```

---

## Homework (2 hours)

### Reading

1. [Python Lists](https://www.w3schools.com/python/python_lists.asp)
2. [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)
3. [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp)

### Coding Tasks

1. **Test Data Manager:** Create a class that stores:
   - List of test users (dictionaries)
   - Methods to add, remove, find users
2. **Page Elements Dictionary:** Create a dictionary storing selectors:

   ```python
   login_page = {
       "username": "#username",
       "password": "#password",
       "submit": "button[type='submit']"
   }
   ```

3. **List Comprehension Practice:**
   - Filter list of numbers to keep only even
   - Convert list of strings to uppercase
   - Create list of emails from usernames

### Quiz Yourself

1. What's the difference between list and dictionary?
2. How do you safely get a dict value that might not exist?
3. What does `enumerate()` return?
4. How do you loop through both keys and values of a dict?

---

[← Day 3](day-03-functions.md) | [Next: Day 5 - Week 1 Project →](day-05-project.md)

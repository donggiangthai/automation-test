# Day 5: Week 1 Review & Mini-Project

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 10 min | Week 1 concepts recap |
| 15 min | Review checklist walkthrough |
| 45 min | Mini-project implementation (follow along) |
| 15 min | Extensions & improvements |
| 5 min | Week 2 preview |

---

## Objectives

- Apply all Week 1 concepts in one project
- Build a reusable test data generator tool
- Review and solidify Python fundamentals

---

## Mini-Project: Test Data Generator Tool

Build a command-line tool that generates test data for your QA work.

```text
┌─────────────────────────────────────────────────────────────┐
│              TEST DATA GENERATOR                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Input: Configuration (count, types)                       │
│            │                                                │
│            ▼                                                │
│   ┌───────────────────────────┐                            │
│   │   TestDataGenerator       │                            │
│   │   - generate_user()       │                            │
│   │   - generate_product()    │                            │
│   │   - generate_order()      │                            │
│   └───────────────────────────┘                            │
│            │                                                │
│            ▼                                                │
│   Output: JSON file with test data                          │
│                                                             │
│   Uses: variables, functions, collections, loops            │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

```python
# test_data_generator.py
import random
import string
import json
from datetime import datetime, timedelta

class TestDataGenerator:
    """Generate various types of test data"""
    
    @staticmethod
    def random_string(length=10):
        return ''.join(random.choices(string.ascii_letters, k=length))
    
    @staticmethod
    def random_email():
        return f"{TestDataGenerator.random_string(8).lower()}@test.com"
    
    @staticmethod
    def random_phone():
        return f"+1{random.randint(1000000000, 9999999999)}"
    
    @staticmethod
    def random_date(start_year=2020, end_year=2025):
        start = datetime(start_year, 1, 1)
        end = datetime(end_year, 12, 31)
        delta = end - start
        random_days = random.randint(0, delta.days)
        return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")
    
    @staticmethod
    def random_price(min_val=1, max_val=1000):
        return round(random.uniform(min_val, max_val), 2)
    
    @staticmethod
    def generate_user():
        return {
            "id": random.randint(1, 99999),
            "email": TestDataGenerator.random_email(),
            "first_name": TestDataGenerator.random_string(6).capitalize(),
            "last_name": TestDataGenerator.random_string(8).capitalize(),
            "phone": TestDataGenerator.random_phone(),
            "created_at": TestDataGenerator.random_date()
        }
    
    @staticmethod
    def generate_product():
        categories = ["Electronics", "Clothing", "Books", "Home", "Sports"]
        return {
            "id": random.randint(1, 99999),
            "name": f"Product {TestDataGenerator.random_string(5)}",
            "category": random.choice(categories),
            "price": TestDataGenerator.random_price(),
            "in_stock": random.choice([True, False])
        }
    
    @staticmethod
    def generate_order(user_id=None):
        return {
            "id": random.randint(1, 99999),
            "user_id": user_id or random.randint(1, 99999),
            "products": [TestDataGenerator.generate_product() for _ in range(random.randint(1, 5))],
            "status": random.choice(["pending", "processing", "shipped", "delivered"]),
            "created_at": TestDataGenerator.random_date()
        }


def main():
    gen = TestDataGenerator()
    
    print("=== Test Data Generator ===\n")
    
    # Generate users
    print("Users:")
    users = [gen.generate_user() for _ in range(3)]
    for user in users:
        print(f"  {user['email']} - {user['first_name']} {user['last_name']}")
    
    # Generate products
    print("\nProducts:")
    products = [gen.generate_product() for _ in range(3)]
    for product in products:
        print(f"  {product['name']} - ${product['price']} ({product['category']})")
    
    # Save to JSON file
    test_data = {
        "users": users,
        "products": products,
        "orders": [gen.generate_order() for _ in range(2)]
    }
    
    with open("test_data.json", "w") as f:
        json.dump(test_data, f, indent=2)
    
    print("\n✅ Test data saved to test_data.json")


if __name__ == "__main__":
    main()
```

---

## Week 1 Review Checklist

### Variables & Types

- [ ] Create variables of different types
- [ ] Use f-strings for formatting
- [ ] Convert between types

### Control Flow

- [ ] Write if/elif/else statements
- [ ] Use comparison operators
- [ ] Apply logical operators

### Functions

- [ ] Create functions with parameters
- [ ] Use default parameter values
- [ ] Return values from functions

### Collections

- [ ] Work with lists (append, remove, iterate)
- [ ] Work with dictionaries (get, set, iterate)
- [ ] Use list comprehensions

---

## Extensions (Optional)

Try adding these features:

1. **Command-line arguments:**

   ```python
   import sys
   count = int(sys.argv[1]) if len(sys.argv) > 1 else 3
   ```

2. **Input validation:**

   ```python
   def generate_users(count):
       if count < 1 or count > 100:
           raise ValueError("Count must be 1-100")
       return [generate_user() for _ in range(count)]
   ```

3. **Export to CSV:**

   ```python
   import csv
   with open("users.csv", "w", newline="") as f:
       writer = csv.DictWriter(f, fieldnames=users[0].keys())
       writer.writeheader()
       writer.writerows(users)
   ```

---

## Homework (2 hours)

### Extend the Project

1. Add more data generators:
   - `generate_address()` - street, city, zip, country
   - `generate_credit_card()` - number (fake), expiry, cvv
   - `generate_review()` - rating, comment, date

2. Create a simple CLI menu:

   ```python
   print("1. Generate Users")
   print("2. Generate Products")
   print("3. Generate Orders")
   choice = input("Select option: ")
   ```

3. Add data validation before saving

### Week 1 Self-Assessment

Complete the checklist above - if you can check all boxes, you're ready for Week 2!

### Prepare for Week 2

1. Install pytest: `pip install pytest pytest-html`
2. Read: [pytest Getting Started](https://docs.pytest.org/en/stable/getting-started.html)
3. Preview: Think about how you would test your data generator functions

---

[← Day 4](day-04-collections.md) | [Next: Week 2 - pytest →](../week-2/day-06-pytest-intro.md)

# Day 10: Week 2 Review - Complete Test Suite

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Activity |
|------|----------|
| 10 min | Week 2 concepts recap |
| 15 min | Project requirements review |
| 45 min | Mini-project implementation |
| 15 min | Code review & improvements |
| 5 min | Week 3 preview |

---

## Objectives

- Apply all pytest features in one project
- Build a complete test suite with fixtures, parametrize, markers
- Demonstrate test organization best practices

---

## Mini-Project: Test Suite for User Management

```
┌─────────────────────────────────────────────────────────────┐
│          WEEK 2 PROJECT STRUCTURE                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   tests/                                                    │
│   ├── conftest.py          ← Fixtures (Day 7)              │
│   ├── pytest.ini           ← Markers config (Day 9)        │
│   └── test_user_management.py                              │
│       ├── TestUserCreation   @smoke                        │
│       ├── TestUserValidation @regression + @parametrize    │
│       └── TestUserCRUD       @regression                   │
│                                                             │
│   Features Used:                                            │
│   ✓ Fixtures with setup/teardown                           │
│   ✓ Parametrized validation tests                          │
│   ✓ Markers (smoke, regression)                            │
│   ✓ Exception testing (pytest.raises)                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Hands-on Demo

```python
# tests/test_user_management.py
"""
Complete test suite demonstrating pytest features
"""
import pytest

# ============ Fixtures ============

@pytest.fixture
def user_service():
    """Mock user service"""
    class UserService:
        def __init__(self):
            self.users = {}
        
        def create_user(self, email, password, name):
            if email in self.users:
                raise ValueError("User already exists")
            if not self._validate_email(email):
                raise ValueError("Invalid email format")
            if len(password) < 8:
                raise ValueError("Password too short")
            
            user_id = len(self.users) + 1
            self.users[email] = {
                "id": user_id,
                "email": email,
                "name": name,
                "active": True
            }
            return self.users[email]
        
        def get_user(self, email):
            return self.users.get(email)
        
        def delete_user(self, email):
            if email in self.users:
                del self.users[email]
                return True
            return False
        
        def _validate_email(self, email):
            return "@" in email and "." in email
    
    return UserService()


# ============ Smoke Tests ============

@pytest.mark.smoke
class TestUserCreation:
    """Critical user creation tests"""
    
    def test_create_valid_user(self, user_service):
        """User can be created with valid data"""
        user = user_service.create_user(
            email="test@example.com",
            password="Password123",
            name="Test User"
        )
        assert user["email"] == "test@example.com"
        assert user["active"] == True
    
    def test_create_user_generates_id(self, user_service):
        """Created user receives an ID"""
        user = user_service.create_user(
            email="test@example.com",
            password="Password123",
            name="Test User"
        )
        assert "id" in user
        assert user["id"] > 0


# ============ Validation Tests ============

@pytest.mark.regression
class TestUserValidation:
    """Input validation tests"""
    
    @pytest.mark.parametrize("invalid_email", [
        "invalid",
        "no-at-sign.com",
        "@nodomain",
        "spaces in@email.com",
    ])
    def test_reject_invalid_email(self, user_service, invalid_email):
        """Invalid emails are rejected"""
        with pytest.raises(ValueError, match="Invalid email"):
            user_service.create_user(invalid_email, "Password123", "Test")
    
    @pytest.mark.parametrize("short_password", [
        "short",
        "1234567",
        "",
    ])
    def test_reject_short_password(self, user_service, short_password):
        """Short passwords are rejected"""
        with pytest.raises(ValueError, match="Password too short"):
            user_service.create_user("test@example.com", short_password, "Test")
    
    def test_reject_duplicate_email(self, user_service):
        """Duplicate emails are rejected"""
        user_service.create_user("test@example.com", "Password123", "First")
        
        with pytest.raises(ValueError, match="already exists"):
            user_service.create_user("test@example.com", "Password456", "Second")


# ============ CRUD Tests ============

@pytest.mark.regression
class TestUserCRUD:
    """Create, Read, Update, Delete tests"""
    
    def test_get_existing_user(self, user_service):
        """Can retrieve created user"""
        user_service.create_user("test@example.com", "Password123", "Test")
        
        user = user_service.get_user("test@example.com")
        assert user is not None
        assert user["name"] == "Test"
    
    def test_get_nonexistent_user_returns_none(self, user_service):
        """Getting non-existent user returns None"""
        user = user_service.get_user("nobody@example.com")
        assert user is None
    
    def test_delete_existing_user(self, user_service):
        """Can delete existing user"""
        user_service.create_user("test@example.com", "Password123", "Test")
        
        result = user_service.delete_user("test@example.com")
        assert result == True
        assert user_service.get_user("test@example.com") is None
    
    def test_delete_nonexistent_user(self, user_service):
        """Deleting non-existent user returns False"""
        result = user_service.delete_user("nobody@example.com")
        assert result == False
```

---

## Run and Generate Report

```powershell
# Run all tests
pytest tests/test_user_management.py -v

# Run smoke tests only
pytest tests/test_user_management.py -m smoke -v

# Generate HTML report
pytest tests/test_user_management.py -v --html=user_tests_report.html

# Run with coverage
pip install pytest-cov
pytest tests/test_user_management.py -v --cov=. --cov-report=html
```

---

## Week 2 Review Checklist

### pytest Basics
- [ ] Write tests with meaningful assertions
- [ ] Understand pytest discovery rules
- [ ] Use pytest.raises for exception testing

### Fixtures
- [ ] Create fixtures in conftest.py
- [ ] Use fixture scopes (function, session)
- [ ] Implement cleanup with yield

### Parameterized Tests
- [ ] Use @pytest.mark.parametrize
- [ ] Create test IDs with pytest.param
- [ ] Combine multiple parametrize decorators

### Test Organization
- [ ] Use custom markers
- [ ] Configure pytest.ini
- [ ] Run tests selectively with -m

---

## Homework (2 hours)

### Extend the Project
1. Add `update_user(email, new_data)` method and tests
2. Add `list_users()` method with filters and tests
3. Implement password hashing (mock) and test it

### Week 2 Self-Assessment
Complete all checklist items. If you can check all boxes, you're ready for Week 3!

### Prepare for Week 3
1. Install Playwright: `pip install pytest-playwright && playwright install`
2. Visit [Playwright Docs](https://playwright.dev/python/)
3. Preview: Think about how to test web UIs automatically

---

[← Day 9](day-09-markers.md) | [Next: Week 3 - Playwright →](../week-3/day-11-playwright-setup.md)

[← Day 9](day-09-markers.md) | [Next: Week 3 - Playwright →](../week-3/day-11-playwright-setup.md)

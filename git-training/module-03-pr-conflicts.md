# Module 3: Pull Requests & Conflict Resolution

**Duration:** 1.5-2 hours  
**Prerequisites:** Completed Module 1 & 2  
**Goal:** Master PR workflow and confidently resolve merge conflicts

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 15 min | PR workflow introduction |
| 30 min | Creating good PRs (hands-on) |
| 30 min | Conflict resolution |
| 15 min | .gitignore for test automation |
| 15 min | Practice exercise |
| 15 min | Q&A & recap |

---

## Part 1: Pull Requests (PR) / Merge Requests (MR)

### Visual: PR Workflow

```text
┌─────────────────────────────────────────────────────────────┐
│                    PR WORKFLOW                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Create branch        git checkout -b feature/tests     │
│  2. Write/update tests   ... coding ...                    │
│  3. Commit changes       git commit -m "Add login tests"   │
│  4. Push branch          git push -u origin feature/tests  │
│  5. Create PR            On GitHub/GitLab website          │
│  6. Code review          Team reviews your code            │
│  7. Address feedback     Make changes, push again          │
│  8. Merge PR             After approval                    │
│  9. Delete branch        Clean up                          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Good PR Practices

**PR Title:**

```text
✅ Good: "Add login page E2E tests with POM pattern"
✅ Good: "Fix flaky checkout test - add explicit waits"
❌ Bad:  "Update tests"
❌ Bad:  "WIP"
```

**PR Description Template:**

```markdown
## What does this PR do?
- Adds E2E tests for login functionality
- Implements LoginPage page object

## Test Coverage
- [x] Valid login
- [x] Invalid credentials
- [x] Empty fields validation
- [x] Remember me functionality

## How to test
1. Run `pytest tests/test_login.py -v`
2. All tests should pass

## Screenshots/Videos
(Attach if relevant)

## Checklist
- [x] Tests pass locally
- [x] Code follows project conventions
- [x] No hardcoded test data
- [x] Locators are reliable (role-based preferred)
```

### PR Lifecycle Demo

```bash
# Step 1: Start from updated main
git checkout main
git pull origin main

# Step 2: Create feature branch
git checkout -b feature/checkout-tests

# Step 3: Make your changes
echo "def test_checkout(): pass" > tests/test_checkout.py
git add tests/
git commit -m "test: Add checkout test skeleton"

# Step 4: Make more changes
echo "def test_empty_cart(): pass" >> tests/test_checkout.py
git commit -am "test: Add empty cart test"

# Step 5: Push to remote
git push -u origin feature/checkout-tests

# Step 6: Go to GitHub/GitLab → Create Pull Request
# Step 7: Wait for review, make changes if needed
# Step 8: Merge PR (on website)

# Step 9: Clean up locally
git checkout main
git pull origin main
git branch -d feature/checkout-tests
```

---

## Part 2: Handling Merge Conflicts

### What is a Conflict?

When two people change **the same lines** in the same file, Git cannot automatically decide which version to keep.

```text
<<<<<<< HEAD
def test_login_success(page):
    page.goto("/login")
=======
def test_valid_login(page):
    page.goto("/auth/login")
>>>>>>> feature/rename-tests
```

**What this means:**

- `<<<<<<< HEAD`: Your current branch's version
- `=======`: Separator
- `>>>>>>> feature/rename-tests`: The other branch's version

### How to Resolve Conflicts

```bash
# Step 1: When merge fails, Git tells you which files conflict
git merge feature/other-branch
# Output: CONFLICT (content): Merge conflict in test_login.py

# Step 2: Check status
git status
# Shows: both modified: test_login.py

# Step 3: Open file in VS Code
code test_login.py
```

**In VS Code, you'll see buttons:**

- **Accept Current Change** - Keep your version
- **Accept Incoming Change** - Keep their version
- **Accept Both Changes** - Keep both
- **Compare Changes** - See side by side

```bash
# Step 4: After editing, mark as resolved
git add test_login.py

# Step 5: Complete the merge
git commit -m "Resolve merge conflict in test_login.py"
```

### Visual: Conflict Resolution

```text
┌─────────────────────────────────────────────────────────────┐
│                  CONFLICT RESOLUTION                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Before Resolution:                                         │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ <<<<<<< HEAD                                        │   │
│  │ def test_login_success(page):                       │   │
│  │     page.goto("/login")                             │   │
│  │ =======                                             │   │
│  │ def test_valid_login(page):                         │   │
│  │     page.goto("/auth/login")                        │   │
│  │ >>>>>>> feature/rename-tests                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  After Resolution (you decide):                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ def test_login_success(page):                       │   │
│  │     page.goto("/auth/login")    # Kept new URL      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Avoiding Conflicts

```text
┌─────────────────────────────────────────────────────────────┐
│                CONFLICT PREVENTION TIPS                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Pull frequently         Stay up to date with main      │
│  2. Small, focused PRs      Less chance of overlap         │
│  3. Communicate             Let team know what you're on   │
│  4. Follow conventions      Consistent patterns reduce     │
│                             conflicts                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Part 3: .gitignore for Test Automation

### Why .gitignore?

Some files should **never** be committed:

- Generated files (reports, screenshots)
- Environment-specific files (.env)
- Dependencies (venv, node_modules)
- IDE settings

### Essential .gitignore for Python Test Automation

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
.venv/
venv/
ENV/
.pytest_cache/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# Test artifacts
test-results/
screenshots/
videos/
traces/
*.html
allure-results/
allure-report/

# Environment
.env
.env.local
*.env

# OS files
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Coverage
htmlcov/
.coverage
coverage.xml

# Temporary files
tmp/
temp/
*.tmp
```

### What NOT to Ignore

```text
# Keep these in version control:
✅ pytest.ini
✅ conftest.py
✅ requirements.txt / pyproject.toml
✅ README.md
✅ .gitignore itself
✅ Page objects and test files
✅ Test data files (JSON, CSV)
```

### Creating/Updating .gitignore

```bash
# Create .gitignore
touch .gitignore

# Edit in VS Code
code .gitignore

# Already committed files won't be ignored automatically
# Remove from tracking (but keep file):
git rm --cached filename.py
git commit -m "chore: Stop tracking generated file"
```

---

## Practice Exercise

### Exercise 1: Simulate and Resolve a Conflict

```bash
cd git-practice

# Step 1: Create a file on main
echo "version = 1" > config.py
git add config.py
git commit -m "Add config file"

# Step 2: Create branch A
git checkout -b branch-a
echo "version = 2" > config.py
git commit -am "Update to version 2"

# Step 3: Go back to main, create branch B
git checkout main
git checkout -b branch-b
echo "version = 3" > config.py
git commit -am "Update to version 3"

# Step 4: Merge branch-a into main (will succeed)
git checkout main
git merge branch-a
cat config.py  # Shows "version = 2"

# Step 5: Try to merge branch-b (will CONFLICT!)
git merge branch-b
# Output: CONFLICT!

# Step 6: Open config.py - you'll see conflict markers
cat config.py

# Step 7: Resolve - edit to keep what you want
echo "version = 3" > config.py  # Or edit manually

# Step 8: Mark as resolved and commit
git add config.py
git commit -m "Resolve config version conflict"

# Step 9: Clean up
git branch -d branch-a branch-b
```

### Exercise 2: Create a .gitignore

```bash
# Step 1: Create test artifacts (that should be ignored)
mkdir test-results
touch test-results/report.html
touch debug.log

# Step 2: Check status - Git sees them
git status

# Step 3: Create .gitignore
cat > .gitignore << 'EOF'
test-results/
*.log
__pycache__/
.pytest_cache/
EOF

# Step 4: Check status again - they're ignored!
git status

# Step 5: Commit the .gitignore
git add .gitignore
git commit -m "chore: Add .gitignore"
```

### Exercise 3: PR Simulation (Pair Exercise)

If working with a partner or using GitHub:

```bash
# Person A:
git checkout -b feature/test-a
echo "def test_a(): pass" > test_a.py
git add . && git commit -m "Add test A"
git push -u origin feature/test-a
# Create PR on GitHub

# Person B:
git checkout -b feature/test-b
echo "def test_b(): pass" > test_b.py
git add . && git commit -m "Add test B"
git push -u origin feature/test-b
# Create PR on GitHub

# Both PRs can be merged to main without conflict!
```

---

## Key Takeaways

1. **PRs are checkpoints** - Never push directly to main
2. **Good PR descriptions** save reviewer time
3. **Conflicts are normal** - Don't panic, resolve carefully
4. **Use .gitignore** - Keep the repo clean

---

## Homework

1. Practice creating a conflict and resolving it
2. Create a comprehensive .gitignore for your test project
3. Write a PR description for an imaginary test addition

---

[← Module 2](module-02-branching-collaboration.md) | [Back to Index](README.md) | [Next: Module 4 - Best Practices →](module-04-advanced-tools.md)

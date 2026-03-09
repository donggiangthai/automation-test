# Module 2: Branching & Collaboration

**Duration:** 1.5-2 hours  
**Prerequisites:** Completed Module 1  
**Goal:** Master branching and remote repository workflows

---

## Session Outline

| Time | Activity |
|------|----------|
| 15 min | Why branching? Concept introduction |
| 30 min | Branch commands (hands-on) |
| 30 min | Working with remote repositories |
| 30 min | Practice exercise |
| 15 min | Q&A & recap |

---

## Part 1: Branching Strategy

### Why Branches?

```
┌─────────────────────────────────────────────────────────────┐
│                    BRANCH WORKFLOW                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  main ─────●─────●─────●─────●─────●─────●───────►         │
│                   \           /                             │
│  feature/login     ●────●────●                              │
│                                                             │
│  • main: Always stable, deployable code                     │
│  • feature/*: Work in progress, can break                   │
│  • Merge when feature is complete and tested               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Real-World Scenario

```
Without branches:
  Team member A: "Don't touch main, I'm working!"
  Team member B: "But I need to add tests!"
  Result: Conflicts, broken code, frustration

With branches:
  Team member A: Works on feature/api-tests
  Team member B: Works on feature/ui-tests
  Both: Merge when ready, main stays stable
```

### Branch Commands

```bash
# List all branches
git branch           # Local branches
git branch -a        # All branches (including remote)

# Create and switch to new branch
git checkout -b feature/login-tests

# Switch between branches
git checkout main
git checkout feature/login-tests

# Modern alternative (Git 2.23+)
git switch main
git switch -c feature/new-tests    # Create and switch

# Delete branch (after merging)
git branch -d feature/login-tests  # Safe delete
git branch -D feature/login-tests  # Force delete
```

### Naming Convention for Test Automation

```bash
# Feature branches
feature/login-tests
feature/cart-page-object
feature/api-testing

# Bug fix branches
fix/flaky-checkout-test
fix/locator-update

# Improvement branches
improve/test-data-factory
improve/wait-strategies

# Experiment branches
experiment/parallel-execution
```

---

## Part 2: Working with Remote (GitHub/GitLab)

### Visual: Local vs Remote

```
┌─────────────────────────────────────────────────────────────┐
│                     YOUR LOCAL MACHINE                       │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  main ─────●─────●─────●                              │  │
│  │  feature/login ──────●────●                           │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                    │                    ▲
         git push   │                    │  git pull
                    ▼                    │
┌─────────────────────────────────────────────────────────────┐
│                     REMOTE (GitHub)                          │
│  ┌───────────────────────────────────────────────────────┐  │
│  │  origin/main ────●─────●─────●                        │  │
│  │  origin/feature/login ───────●                        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### Common Remote Commands

```bash
# View remote repositories
git remote -v

# Add remote repository
git remote add origin git@github.com:username/repo.git

# Fetch latest from remote (doesn't merge)
git fetch origin

# Pull latest changes (fetch + merge)
git pull origin main

# Push your branch
git push origin feature/login-tests

# Push and set upstream (first push of new branch)
git push -u origin feature/login-tests

# After -u, you can just use:
git push
git pull
```

### Sync Workflow (Important!)

```bash
# ALWAYS sync before starting new work!

# Step 1: Go to main
git checkout main

# Step 2: Get latest from remote
git pull origin main

# Step 3: Create your feature branch (from updated main)
git checkout -b feature/new-tests

# ... do your work, make commits ...

# Step 4: Before creating PR, sync again
git checkout main
git pull origin main
git checkout feature/new-tests
git merge main                    # Bring main's changes into your branch

# Step 5: Push your branch
git push -u origin feature/new-tests
```

### Visual: Daily Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                   DAILY GIT WORKFLOW                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Morning:                                                   │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ git checkout main                                    │   │
│  │ git pull origin main                                 │   │
│  │ git checkout -b feature/todays-work                  │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  During Work:                                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ # Make changes...                                    │   │
│  │ git add .                                            │   │
│  │ git commit -m "test: Add checkout tests"             │   │
│  │ # Repeat as needed                                   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  End of Day:                                                │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ git push -u origin feature/todays-work               │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Practice Exercise

### Exercise 1: Branching Basics

```bash
# Use the git-practice folder from Module 1
cd git-practice

# Step 1: Create and switch to new branch
git checkout -b feature/login-tests
git branch  # Verify you're on the new branch

# Step 2: Add new test file
echo "def test_login(): pass" > test_login.py
git add test_login.py
git commit -m "test: Add login test placeholder"

# Step 3: Switch back to main
git checkout main
ls  # Notice test_login.py is NOT here

# Step 4: Switch back to feature branch
git checkout feature/login-tests
ls  # Now test_login.py IS here

# Step 5: Merge feature into main
git checkout main
git merge feature/login-tests
ls  # Now test_login.py is in main too!

# Step 6: Delete the feature branch (cleanup)
git branch -d feature/login-tests
git branch  # Only main remains
```

### Exercise 2: Create Multiple Branches

```bash
# Create branch A, add a file
git checkout -b feature/cart-tests
echo "def test_cart(): pass" > test_cart.py
git add test_cart.py
git commit -m "test: Add cart test"

# Go back to main
git checkout main

# Create branch B (from main), add different file
git checkout -b feature/search-tests
echo "def test_search(): pass" > test_search.py
git add test_search.py
git commit -m "test: Add search test"

# Now you have:
# main: test_example.py, test_login.py
# feature/cart-tests: + test_cart.py
# feature/search-tests: + test_search.py

# List all branches
git branch

# Merge both into main
git checkout main
git merge feature/cart-tests
git merge feature/search-tests

# Check result
ls  # All test files present

# Cleanup
git branch -d feature/cart-tests feature/search-tests
```

### Exercise 3: Remote Simulation (if GitHub available)

```bash
# Create a repository on GitHub (web interface)
# Then:

# Add remote
git remote add origin git@github.com:your-username/git-practice.git

# Push main
git push -u origin main

# Create a new branch and push
git checkout -b feature/api-tests
echo "def test_api(): pass" > test_api.py
git add test_api.py
git commit -m "test: Add API test"
git push -u origin feature/api-tests

# Check GitHub - you'll see both branches!
```

---

## Key Takeaways

1. **Branch early, branch often** - Branches are cheap
2. **Keep main clean** - Only merge tested, working code
3. **Sync before branching** - Always start from updated main
4. **Use meaningful names** - `feature/login-tests` not `branch1`

---

## Common Mistakes to Avoid

| Mistake | Solution |
|---------|----------|
| Forgetting to switch branches | Always check `git branch` before committing |
| Creating branch from wrong base | `git checkout main && git pull` first |
| Pushing without pulling | Run `git pull` before `git push` |
| Deleting unmerged branch | Use `-d` (safe) not `-D` (force) |

---

## Homework

1. Create 2 feature branches with different test files
2. Merge them both to main
3. Practice switching between branches
4. If you have GitHub, practice push/pull

---

[← Module 1](module-01-setup-basics.md) | [Back to Index](README.md) | [Next: Module 3 - PRs & Conflicts →](module-03-pr-conflicts.md)

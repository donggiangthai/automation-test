# Module 4: Best Practices & Tools

**Duration:** 1.5-2 hours  
**Prerequisites:** Completed Modules 1-3  
**Goal:** Master Git best practices and tooling for efficient daily work

---

## Session Outline

| Time | Activity |
| ------ | ---------- |
| 20 min | Commit message conventions |
| 25 min | Troubleshooting common issues |
| 30 min | VS Code Git integration (hands-on) |
| 20 min | Advanced tips & quick reference |
| 25 min | Final exercise & Q&A |

---

## Part 1: Best Practices for Test Code

### Commit Message Convention

```bash
# Format: <type>: <short description>

# Types for test automation:
test:     Add/update tests
fix:      Fix broken test or bug
refactor: Restructure code (no behavior change)
docs:     Documentation only
chore:    Maintenance (deps, config)
```

**Examples:**

```bash
git commit -m "test: Add login page E2E tests"
git commit -m "test: Add product search tests with data-driven approach"
git commit -m "fix: Update locator for submit button"
git commit -m "fix: Handle flaky cart test with explicit wait"
git commit -m "refactor: Extract common waits to base page"
git commit -m "refactor: Move test data to fixtures"
git commit -m "docs: Add README for test setup"
git commit -m "chore: Update Playwright version"
```

### Commit Frequency

```text
✅ Good: Commit after completing a logical unit
   - "Add LoginPage page object"
   - "Add test_valid_login test"
   - "Add test_invalid_credentials test"

❌ Bad: One huge commit
   - "Add all login tests" (500 lines changed)

❌ Bad: Too granular
   - "Add import"
   - "Add class"
   - "Add method"
```

### Branch Lifecycle

```bash
# 1. Start fresh
git checkout main
git pull

# 2. Create feature branch
git checkout -b feature/cart-tests

# 3. Work in small commits
git add tests/test_cart.py
git commit -m "test: Add empty cart test"

git add pages/cart_page.py
git commit -m "refactor: Add CartPage page object"

# 4. Push and create PR
git push -u origin feature/cart-tests

# 5. After PR is merged, clean up
git checkout main
git pull
git branch -d feature/cart-tests
```

---

## Part 2: Troubleshooting Common Issues

### Issue: "Permission denied (publickey)"

```bash
# SSH key not set up properly
ssh -T git@github.com  # Test connection

# Solution: Follow SSH setup from Module 1
# Or check your key is added:
ssh-add -l
```

### Issue: "Your branch is behind"

```bash
# Remote has changes you don't have
git pull origin main

# If you have local changes:
git stash                 # Save changes temporarily
git pull origin main
git stash pop            # Restore your changes
```

### Issue: "Cannot push - rejected"

```bash
# Remote has changes you need first
git pull --rebase origin main
git push

# If conflicts occur during rebase:
# Resolve them, then:
git add .
git rebase --continue
```

### Issue: "Detached HEAD"

```bash
# You checked out a commit instead of branch
git status  # Shows "HEAD detached at abc123"

# Solution: Go back to a branch
git checkout main

# If you want to keep changes:
git checkout -b my-new-branch
```

### Issue: "Accidentally committed to main"

```bash
# Move commit to new branch
git branch feature/my-work   # Create branch at current position
git reset --hard HEAD~1      # Move main back one commit
git checkout feature/my-work # Switch to branch with your work
```

### Issue: "Added file that should be ignored"

```bash
# Remove from Git but keep the file
git rm --cached filename.py
git commit -m "chore: Remove file from tracking"

# Make sure it's in .gitignore
echo "filename.py" >> .gitignore
```

---

## Part 3: VS Code Git Integration

### Built-in Git Features

```text
┌─────────────────────────────────────────────────────────────┐
│                  VS CODE GIT PANEL                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Source Control (Ctrl+Shift+G)                              │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  💬 Message box (type commit message here)          │   │
│  │  ✓ Commit (Ctrl+Enter)                              │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  Changes:                                            │   │
│  │    📄 test_login.py  +  (click + to stage)          │   │
│  │    📄 conftest.py    +                              │   │
│  ├─────────────────────────────────────────────────────┤   │
│  │  Staged Changes:                                     │   │
│  │    📄 test_cart.py   -  (click - to unstage)        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Actions in VS Code

| Action | How to Do It |
| -------- | -------------- |
| Open Source Control | `Ctrl+Shift+G` |
| Stage file | Click `+` next to file |
| Unstage file | Click `-` next to staged file |
| Stage all | Click `+` on "Changes" header |
| Commit | Type message → `Ctrl+Enter` |
| View diff | Click on file name |
| Discard changes | Right-click → Discard Changes |

### Status Bar

```text
┌─────────────────────────────────────────────────────────────┐
│  Left side of VS Code status bar:                           │
│                                                             │
│  🔀 main ↑2 ↓3                                              │
│  │    │   │   │                                             │
│  │    │   │   └── 3 commits to pull                        │
│  │    │   └────── 2 commits to push                        │
│  │    └────────── Current branch name                      │
│  └─────────────── Click to switch branches                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### GitLens Extension (Recommended)

Install "GitLens" from VS Code extensions for:

```text
┌─────────────────────────────────────────────────────────────┐
│  GitLens Features:                                          │
│                                                             │
│  • Line blame - See who changed each line                  │
│  • File history - Full history of any file                 │
│  • Compare branches - Visual diff                          │
│  • Interactive rebase - GUI for complex operations         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Part 4: Quick Reference Card

### Daily Commands

| Command | What It Does |
| --------- | -------------- |
| `git status` | Check current state |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save changes |
| `git push` | Upload to remote |
| `git pull` | Download latest |

### Branch Commands

| Command | What It Does |
| --------- | -------------- |
| `git branch` | List branches |
| `git checkout -b name` | Create & switch |
| `git checkout main` | Switch to main |
| `git merge branch` | Merge branch |
| `git branch -d name` | Delete branch |

### History Commands

| Command | What It Does |
| --------- | -------------- |
| `git log --oneline` | Compact history |
| `git diff` | See changes |
| `git blame file` | Who changed what |
| `git show abc123` | View commit |

### Undo Commands

| Command | What It Does |
| --------- | -------------- |
| `git checkout -- file` | Discard changes |
| `git reset HEAD file` | Unstage file |
| `git reset --soft HEAD~1` | Undo commit (keep changes) |
| `git revert abc123` | Undo commit (safe) |

### Useful Aliases

```bash
# Add these to your Git config
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"

# Now you can use:
git st     # Instead of: git status
git co     # Instead of: git checkout
git lg     # Beautiful log view
```

---

## Final Practice Exercise

### Complete Workflow Exercise

```bash
# This exercise covers everything you've learned!

# 1. Setup
cd git-practice
git checkout main
git pull origin main 2>/dev/null || true

# 2. Create feature branch with proper naming
git checkout -b feature/final-exercise

# 3. Create test file with proper structure
cat > test_final.py << 'EOF'
import pytest

def test_example_positive():
    """Test positive scenario"""
    assert 1 + 1 == 2

def test_example_negative():
    """Test negative scenario"""
    assert not (1 + 1 == 3)
EOF

# 4. Stage with intention
git add test_final.py
git status  # Verify what's staged

# 5. Commit with proper message
git commit -m "test: Add final exercise tests"

# 6. Add another commit
cat >> test_final.py << 'EOF'

@pytest.mark.smoke
def test_smoke():
    """Smoke test"""
    assert True
EOF

git commit -am "test: Add smoke test marker"

# 7. View your history
git log --oneline

# 8. Merge to main
git checkout main
git merge feature/final-exercise

# 9. Clean up
git branch -d feature/final-exercise

# 10. Verify
git log --oneline -5
cat test_final.py

echo "✅ Exercise complete! You've mastered Git basics!"
```

---

## Summary: What You've Learned

| Module | Key Skills |
| -------- | ------------ |
| Module 1 | Git setup, 3 states, basic workflow |
| Module 2 | Branching, remote, sync workflow |
| Module 3 | PRs, conflict resolution, .gitignore |
| Module 4 | Best practices, troubleshooting, tools |

---

## Next Steps

1. **Practice daily** - Use Git for all your test code
2. **Learn advanced topics** - Rebase, cherry-pick, stash
3. **Contribute to open source** - Real-world Git experience
4. **Teach others** - Best way to solidify knowledge

---

## Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Skills](https://skills.github.com/)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - Fixing mistakes
- [Git Cheat Sheet (GitHub)](https://education.github.com/git-cheat-sheet-education.pdf)

---

### Congratulations

You've completed the Git training! 🎉

---

[← Module 3](module-03-pr-conflicts.md) | [Back to Index](README.md)

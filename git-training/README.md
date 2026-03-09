# Git Training for QA Automation Engineers

**Audience:** QA Engineers starting with automation testing  
**Total Duration:** 4 modules × 1.5-2 hours each  
**Prerequisites:** None - we start from scratch!

---

## Training Modules

| Module | Title | Duration | Topics |
|--------|-------|----------|--------|
| [Module 1](module-01-setup-basics.md) | Installation & Core Concepts | 1.5-2h | Git setup, 3 states, basic workflow |
| [Module 2](module-02-branching-collaboration.md) | Branching & Collaboration | 1.5-2h | Branches, remote, sync workflow |
| [Module 3](module-03-pr-conflicts.md) | Pull Requests & Conflicts | 1.5-2h | PR workflow, conflict resolution, .gitignore |
| [Module 4](module-04-advanced-tools.md) | Best Practices & Tools | 1.5-2h | Commit conventions, troubleshooting, VS Code |

---

## Why Git Matters for Testers

| Without Git | With Git |
|-------------|----------|
| "test_login_v2_final_FINAL.py" | Clean history of all changes |
| Lost code when computer crashes | Code safe in remote repository |
| "Who changed this and broke tests?" | Clear blame and history |
| Emailing code to teammates | Seamless collaboration |
| Manual backups | Automatic versioning |

---

## Quick Reference

### Daily Commands

| Command | What It Does |
|---------|--------------|
| `git status` | Check current state |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Save changes |
| `git push` | Upload to remote |
| `git pull` | Download latest |

### Branch Commands

| Command | What It Does |
|---------|--------------|
| `git branch` | List branches |
| `git checkout -b name` | Create & switch |
| `git checkout main` | Switch to main |
| `git merge branch` | Merge branch |
| `git branch -d name` | Delete branch |

---

## Learning Path

```
Module 1                Module 2               Module 3               Module 4
┌──────────────┐       ┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│  Setup &     │       │  Branching   │       │  PRs &       │       │  Best        │
│  Basics      │──────►│  & Remote    │──────►│  Conflicts   │──────►│  Practices   │
└──────────────┘       └──────────────┘       └──────────────┘       └──────────────┘
     Day 1                  Day 2                  Day 3                  Day 4
```

---

## How to Use This Training

### Session Structure (each module)

```
┌───────────────────────────────────────────────────┐
│  15 min   │  Concept Introduction                 │
├───────────┼───────────────────────────────────────┤
│  30 min   │  Demo + Follow Along                  │
├───────────┼───────────────────────────────────────┤
│  30 min   │  Guided Practice                      │
├───────────┼───────────────────────────────────────┤
│  15 min   │  Exercise (Self-Practice)             │
├───────────┼───────────────────────────────────────┤
│  15 min   │  Q&A + Recap                          │
└───────────┴───────────────────────────────────────┘
```

### Tips for Success

1. **Practice daily** - 10-15 minutes of Git usage builds muscle memory
2. **Don't fear mistakes** - Git is designed to recover from errors
3. **Use `git status` often** - It tells you what to do next
4. **Ask questions** - No question is too basic

---

[Start Module 1 →](module-01-setup-basics.md)

# Module 1: Installation & Core Concepts

**Duration:** 1.5-2 hours  
**Goal:** Install Git, understand core concepts, make your first commit

---

## Session Outline

| Time | Activity |
|------|----------|
| 15 min | Introduction to version control |
| 30 min | Installation & setup (hands-on) |
| 30 min | Core concepts & first commit |
| 30 min | Practice exercise |
| 15 min | Q&A & recap |

---

## Part 1: Installation & Setup

### Install Git

**Windows:**
```powershell
# Using winget (recommended)
winget install Git.Git

# Verify installation
git --version
```

**macOS:**
```bash
# Git comes with Xcode Command Line Tools
xcode-select --install

# Or using Homebrew
brew install git
```

### First-Time Configuration

```bash
# Set your identity (use your real name and email)
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"

# Set default branch name to 'main'
git config --global init.defaultBranch main

# Set VS Code as default editor
git config --global core.editor "code --wait"

# Enable colored output
git config --global color.ui auto

# Verify settings
git config --list
```

### SSH Key Setup (for GitHub/GitLab)

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@company.com"

# Start SSH agent (Windows PowerShell)
Get-Service -Name ssh-agent | Set-Service -StartupType Manual
Start-Service ssh-agent

# Start SSH agent (macOS/Linux)
eval "$(ssh-agent -s)"

# Add your key
ssh-add ~/.ssh/id_ed25519

# Copy public key to clipboard (Windows)
Get-Content ~/.ssh/id_ed25519.pub | Set-Clipboard

# Copy public key to clipboard (macOS)
pbcopy < ~/.ssh/id_ed25519.pub

# Then add this key to your GitHub/GitLab account settings
```

---

## Part 2: Core Concepts

### The Three States of Git

```
┌─────────────────────────────────────────────────────────────┐
│                     GIT WORKFLOW                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Working Directory    Staging Area      Repository         │
│  (Your files)         (Index)           (.git folder)      │
│                                                             │
│       📁                  📋                 📦             │
│        │                   │                  │             │
│        │── git add ──────► │                  │             │
│        │                   │── git commit ──► │             │
│        │◄── git checkout ──│                  │             │
│        │◄─────────────────────────────────────│             │
│                                                             │
│  Edit files here      Stage changes      Permanent history │
│                       before commit                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Key Terms

| Term | What It Means | Analogy |
|------|---------------|---------|
| **Repository (Repo)** | Project folder tracked by Git | A project folder with history |
| **Commit** | Snapshot of your code at a point in time | Save game checkpoint |
| **Branch** | Independent line of development | Parallel universe |
| **Remote** | Repository on a server (GitHub, GitLab) | Cloud backup |
| **Clone** | Download a repository | Copy project from cloud |
| **Pull** | Download latest changes | Sync from cloud |
| **Push** | Upload your changes | Sync to cloud |

### Visual: Git Mental Model

```
                    ┌─────────────────────────────────┐
                    │         REMOTE (GitHub)          │
                    │   origin/main                    │
                    └─────────────────────────────────┘
                              ▲           │
                         push │           │ pull/clone
                              │           ▼
┌──────────────────────────────────────────────────────────────┐
│                     YOUR COMPUTER                            │
│  ┌────────────┐    ┌────────────┐    ┌────────────────────┐ │
│  │  Working   │───►│  Staging   │───►│  Local Repository  │ │
│  │  Directory │add │   Area     │commit│  (.git folder)   │ │
│  └────────────┘    └────────────┘    └────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## Part 3: Daily Git Commands

### Starting a New Project

```bash
# Option 1: Create new repository
mkdir my-automation-project
cd my-automation-project
git init

# Option 2: Clone existing repository
git clone git@github.com:company/automation-tests.git
cd automation-tests
```

### The Basic Workflow

```bash
# 1. Check status (do this often!)
git status

# 2. See what changed
git diff

# 3. Stage files for commit
git add filename.py           # Add specific file
git add tests/                # Add entire folder
git add .                     # Add all changes (be careful!)
git add -p                    # Interactive: choose what to add

# 4. Commit with meaningful message
git commit -m "Add login page tests"

# 5. Push to remote
git push
```

### Checking History

```bash
# View commit history
git log

# Compact one-line history
git log --oneline

# See who changed what line (blame)
git blame tests/test_login.py

# See changes in a specific commit
git show abc1234
```

### Undoing Mistakes

```bash
# Undo changes in working directory (before staging)
git checkout -- filename.py      # Discard changes in one file
git checkout -- .                # Discard all changes (CAREFUL!)

# Unstage files (after git add, before commit)
git reset HEAD filename.py       # Unstage one file
git reset HEAD                   # Unstage all files

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes) - DANGEROUS!
git reset --hard HEAD~1

# Create a new commit that undoes a previous commit (safe)
git revert abc1234
```

---

## Practice Exercise

### Exercise 1: Initialize and First Commit

```bash
# Step 1: Create a new test project
mkdir git-practice
cd git-practice
git init

# Step 2: Create a test file
echo "def test_example(): assert True" > test_example.py

# Step 3: Check status
git status
# You should see test_example.py as "untracked"

# Step 4: Stage the file
git add test_example.py
git status
# You should see it as "Changes to be committed"

# Step 5: Make your first commit
git commit -m "test: Add example test"

# Step 6: Check history
git log --oneline
# You should see your commit!
```

### Exercise 2: Make Changes and Commit

```bash
# Step 1: Edit the file
echo "def test_login(): pass" >> test_example.py

# Step 2: See the diff
git diff

# Step 3: Stage and commit
git add test_example.py
git commit -m "test: Add login test placeholder"

# Step 4: Check history
git log --oneline
# You should see 2 commits now
```

### Exercise 3: Undo Changes

```bash
# Step 1: Make a change you don't want
echo "MISTAKE" >> test_example.py

# Step 2: Check status
git status

# Step 3: Discard the change
git checkout -- test_example.py

# Step 4: Verify
cat test_example.py
# "MISTAKE" should be gone
```

---

## Key Takeaways

1. **Git has 3 states:** Working Directory → Staging → Repository
2. **Always use `git status`** - It tells you what's happening
3. **Commit often** - Small, logical commits are better
4. **Messages matter** - Write meaningful commit messages

---

## Homework

1. Create 3 more test files and commit them
2. Practice `git log`, `git diff`, `git status`
3. Try making a mistake and undoing it

---

[← Back to Index](README.md) | [Next: Module 2 - Branching →](module-02-branching-collaboration.md)

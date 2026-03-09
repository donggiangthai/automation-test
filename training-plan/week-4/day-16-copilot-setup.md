# Day 16: GitHub Copilot Setup & Basics

**Duration:** 1.5 hours session + 2 hours self-study

---

## Session Outline

| Time | Topic | Activity |
| ------ | ------- | ---------- |
| 0:00-0:10 | Introduction to AI-Assisted Testing | Lecture |
| 0:10-0:25 | GitHub Copilot Setup & Configuration | Demo |
| 0:25-0:45 | Key Features: Inline, Chat, Commands | Hands-on |
| 0:45-1:00 | Using Copilot for Test Writing | Practice |
| 1:00-1:20 | Practice Exercise: First AI Tests | Hands-on |
| 1:20-1:30 | Q&A & Homework Review | Discussion |

---

## Objectives

- Install and configure GitHub Copilot
- Learn basic interactions
- Understand AI-assisted development concepts

---

## Visual Concept: AI-Assisted Testing Workflow

```text
┌─────────────────────────────────────────────────────────────┐
│                   AI-Assisted Testing                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Developer                     Copilot                     │
│   ┌─────────┐                  ┌─────────┐                  │
│   │ Write   │ ──── context ──► │ Analyze │                  │
│   │ Comment │                  │ Intent  │                  │
│   └─────────┘                  └────┬────┘                  │
│        ▲                            │                       │
│        │                            ▼                       │
│        │                       ┌─────────┐                  │
│        │                       │ Generate│                  │
│        │                       │ Code    │                  │
│        │                       └────┬────┘                  │
│        │                            │                       │
│   ┌────┴────┐                       ▼                       │
│   │ Review  │ ◄── suggestion ──┌─────────┐                  │
│   │ Accept  │                  │ Present │                  │
│   └─────────┘                  │ Options │                  │
│                                └─────────┘                  │
│                                                             │
│   Interaction Methods:                                      │
│   • Tab = Accept   • Esc = Dismiss   • Alt+] = Next        │
│   • Ctrl+L = Chat  • Ctrl+I = Inline • /commands            │
└─────────────────────────────────────────────────────────────┘
```

---

## Setup GitHub Copilot

### Prerequisites

1. **GitHub account** with Copilot access
2. **VS Code** installed
3. Active **Copilot subscription** (or trial)

### Installation

```bash
# In VS Code:
# 1. Open Extensions (Ctrl+Shift+X)
# 2. Search "GitHub Copilot"
# 3. Install extensions:
#    - GitHub Copilot
#    - GitHub Copilot Chat
```

### Configuration

```json
// settings.json
{
    "github.copilot.enable": {
        "*": true,
        "markdown": true,
        "yaml": true
    },
    "github.copilot.inlineSuggest.enable": true
}
```

---

## Key Features

### 1. Inline Suggestions

```python
# Type a comment and Copilot suggests code
# Example: Start typing after the comment

def calculate_order_total(items):
    # Calculate total price including tax
    # ← Copilot suggests implementation here
```

### 2. Copilot Chat (Ctrl+L)

```text
You: How do I write a pytest fixture?
Copilot: Here's a basic pytest fixture...
```

### 3. Inline Chat (Ctrl+I)

```python
# Select code → Ctrl+I → "Explain this"
# Select code → Ctrl+I → "Add type hints"
```

---

## Essential Shortcuts

| Action | Windows/Linux | Mac |
| -------- | --------------- | ----- |
| Accept suggestion | Tab | Tab |
| Dismiss suggestion | Esc | Esc |
| Open Chat panel | Ctrl+L | Cmd+L |
| Inline chat | Ctrl+I | Cmd+I |
| Next suggestion | Alt+] | Option+] |
| Previous suggestion | Alt+[ | Option+[ |

---

## Copilot Modes

### /explain

```text
/explain what does this function do?
```

### /fix

```text
/fix this test is failing
```

### /tests

```text
/tests generate tests for this function
```

### /doc

```text
/doc add documentation
```

---

## Practice Exercise: First AI-Assisted Tests (20 min)

**Goal:** Write your first tests using GitHub Copilot

```python
# tests/test_copilot_intro.py
"""First test file using GitHub Copilot assistance."""

# Task 1: Write a comment describing a simple calculator test
# Let Copilot suggest the implementation

# Task 2: Use Ctrl+I to "Add type hints" to a function

# Task 3: Use /tests command to generate tests for:
def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Task 4: Ask Copilot Chat to explain pytest fixtures
```

---

## Homework

### Reading

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code + Copilot Tips](https://code.visualstudio.com/docs/copilot/overview)

### Coding Tasks

1. **Copilot Exploration**: Explore all Copilot Chat slash commands (/explain, /fix, /tests, /doc)
2. **Test Generation**: Write 5 pytest tests with Copilot assistance for a simple utility module
3. **Workflow Document**: Create a personal note documenting your preferred Copilot shortcuts and patterns

### Quiz Yourself

- What's the difference between Tab completion and Chat in Copilot?
- When should you use inline chat (Ctrl+I) vs Chat panel (Ctrl+L)?
- Name 3 slash commands available in Copilot Chat

---

[← Week 3](../week-3/day-15-project.md) | [Next: Day 17 - Effective Prompting →](day-17-prompting.md)

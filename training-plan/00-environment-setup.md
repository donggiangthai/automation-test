# Day 0: Environment Setup (Pre-Training)

Complete these steps before Day 1.

---

## 1. Install Python

```powershell
# Download from python.org or use winget
winget install Python.Python.3.13

# Verify installation
python --version
pip --version
```

---

## 2. Install VS Code

```powershell
winget install Microsoft.VisualStudioCode

# Install extensions:
# - Python (Microsoft)
# - Pylance
# - GitHub Copilot
# - GitHub Copilot Chat
```

---

## 3. Configure VS Code for Windows

Settings to verify:

- Terminal: Select "Command Prompt" or "PowerShell" as default
- Python interpreter: Select Python 3.13

---

## 4. Create Project Structure

```powershell
# Open Command Prompt or PowerShell
cd Desktop
mkdir automation-training
cd automation-training
mkdir tests pages utils data
```

---

## 5. Keyboard Shortcuts Reference (Windows)

| Action | Shortcut |
|--------|----------|
| Copy | `Ctrl+C` |
| Paste | `Ctrl+V` |
| Cut | `Ctrl+X` |
| Save file | `Ctrl+S` |
| Open file | `Ctrl+O` |
| Quick open (VS Code) | `Ctrl+P` |
| Command palette | `Ctrl+Shift+P` |
| Toggle terminal | `` Ctrl+` `` |
| DevTools (Browser) | `F12` or `Ctrl+Shift+I` |

---

## Verification Checklist

- [ ] Python 3.13 installed and `python --version` works
- [ ] VS Code installed with Python extension
- [ ] GitHub Copilot extension installed and signed in
- [ ] Project folder created with subfolders
- [ ] Can create and run a simple Python file

---

## Test Your Setup

Create a file `hello.py` in your project:

```python
print("Hello, QA Automation!")
print(f"Python version: {__import__('sys').version}")
```

Run it:
```powershell
python hello.py
```

Expected output:
```
Hello, QA Automation!
Python version: 3.13.x (...)
```

---

[← Back to Overview](README.md) | [Next: Day 1 - Variables →](week-1/day-01-variables.md)

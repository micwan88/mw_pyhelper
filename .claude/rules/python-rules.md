---
paths:
  - "**/*.py"
---

# Python Environment Rules

- Always use `uv` as package manager
- Always generate uv lock file after modify package
- Use `uv run --locked` to execute Python program
- Use `pytest` for test and separated integration test / unittest (offline) in different folders say `/tests/unit/xxx`, `/tests/integration/xxx`
- test file location should align or with similar path as their target test object. i.e. `/tests/unit/package_name_a/package_name_b/test_xxxx.py` means the test related to object `codebase_path/package_name_a/package_name_b/xxxx.py`

# Python Coding Rules

- Always make program as a function and try to make it re-usable. (i.e. make `main` function and call it under '__main__')
- Always use type hints if possible
- Setup the logger in the early main process if any
- Use logger instead of 'print' statement
- Try make 'hardcode' value to be declare as constants rather just hardcode inline or even make it configurable
- Don't declare inline import statement, should declare at the top
- Don't declare nested function if they can be avoided, try making functions that can be reused by other python program

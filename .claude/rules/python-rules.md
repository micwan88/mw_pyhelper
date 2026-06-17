---
paths:
  - "**/*.py"
---

# Python Environment Rules

- Always use `uv` as package manager
- Always generate uv lock file after modify package
- Use `uv run --locked` to execute Python program
- Use `pytest` for test and separated integration test / unittest (offline) in different folders say `/tests/unit/packagename/xxx`, `/tests/integration/packagename/xxx`

# Python Coding Rules

- Always make program as a function and try to make it re-usable. (i.e. make `main` function and call it under '__main__')
- Setup the logger in the early main process if any
- Use logger instead of 'print' statement
- Try make 'hardcode' value to be declare as constants rather just hardcode inline or even make it configurable
- Please don't declare inline import statement, should declare at the top
- Always use type hints if possible

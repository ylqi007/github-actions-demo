# Demo 02 - Run Python on Push

## Goal

Automatically run a Python program whenever code is pushed.

---

## Files

```text
hello.py

.github/workflows/python-demo.yml
```

---

## Workflow

```yaml
name: Python Demo

on:
  push:
  workflow_dispatch:

jobs:
  run-python:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: python --version

      - run: python hello.py
```

---

## What I Learned

### push

Automatically triggers the workflow after every push.

---

### uses

Runs an existing GitHub Action.

Examples:

```
actions/checkout
actions/setup-python
```

---

### run

Executes shell commands.

Example:

```yaml
run: python hello.py
```

---

### checkout

Downloads the repository to the runner.

Without checkout:

```
python hello.py
```

will fail because the repository files are unavailable.

---

### setup-python

Installs/configures Python.

```yaml
with:
  python-version: "3.12"
```

---

### with

Passes parameters to an action.

---

## Execution Flow

```
Push

↓

Workflow

↓

Ubuntu Runner

↓

Checkout

↓

Setup Python

↓

Run hello.py
```

---

## Common Commands

```bash
python --version
python hello.py
```

---

## Node.js Warning

The warning

```
Node.js 20 is deprecated
```

only affects GitHub Actions internally.

It does **NOT** affect Python execution.

---

## Key Takeaways

- Workflows can run automatically.
- `uses` and `run` serve different purposes.
- `checkout` downloads repository files.
- `setup-python` configures Python.
- GitHub executes code in a temporary runner.
# Demo 03 - Python Dependencies

## Goal

Learn how to declare, install, and use third-party Python packages in GitHub Actions.

---

## Files

```text
hello.py
requirements.txt
.github/workflows/python-demo.yml
```

---

## Dependency Definition

The project dependencies are declared in `requirements.txt`:

```text
requests==2.32.5
```

The version is pinned with `==` so the same package version is installed in different environments.

`requirements.txt` only declares dependencies. It does not install them automatically.

---

## Python Program

The Python program imports and uses the third-party `requests` package:

```python
import requests

response = requests.get(
    "https://api.github.com",
    timeout=10,
)

print(f"GitHub API status code: {response.status_code}")

response.raise_for_status()

data = response.json()
print(f"Current user API URL: {data['current_user_url']}")
```

Because `requests` is not part of the Python standard library, it must be installed before running the program.

---

## Workflow

```yaml
name: Python Demo

on:
  push:
  workflow_dispatch:

jobs:
  run-python:
    runs-on: ubuntu-24.04

    steps:
      - name: Download repository code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Show Python version
        run: python --version

      - name: Upgrade pip
        run: python -m pip install --upgrade pip

      - name: Install dependencies
        run: python -m pip install -r requirements.txt

      - name: Run Python program
        run: python hello.py
```

---

## Execution Flow

```text
Workflow starts
      ↓
Checkout repository
      ↓
Set up Python 3.12
      ↓
Upgrade pip
      ↓
Read requirements.txt
      ↓
Install dependencies
      ↓
Run hello.py
```

---

## Key Concepts

### `requirements.txt`

A dependency manifest used to list the Python packages required by a project.

```text
requests==2.32.5
```

---

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

The `-r` option tells pip to read package requirements from a file.

---

### `python -m pip`

Using:

```bash
python -m pip
```

instead of:

```bash
pip
```

ensures that pip belongs to the currently selected Python interpreter.

---

### Pinned Version

```text
requests==2.32.5
```

The `==` operator requires an exact package version.

This improves consistency between local development and GitHub Actions.

---

### Transitive Dependencies

Installing `requests` also installs packages that `requests` depends on:

```text
requests
├── certifi
├── charset-normalizer
├── idna
└── urllib3
```

These additional packages are called transitive dependencies.

---

### Fresh Runner Environment

Each GitHub-hosted runner starts from a clean environment.

Dependencies installed during one workflow run are not automatically available in the next run.

Therefore, the workflow must install dependencies every time it runs.

---

## Errors Encountered

### Invalid Package Version

The original dependency version was:

```text
requests==2.34.2
```

The installation failed with:

```text
No matching distribution found for requests==2.34.2
```

The version did not exist.

The dependency was corrected to:

```text
requests==2.32.5
```

---

### Dependency Not Installed

The Python program initially failed with:

```text
ModuleNotFoundError: No module named 'requests'
```

The workflow had a `requirements.txt` file, but it did not include an installation step.

The issue was fixed by adding:

```yaml
- name: Install dependencies
  run: python -m pip install -r requirements.txt
```

This demonstrates that declaring a dependency and installing a dependency are two separate operations.

---

## Result

After the dependencies were installed, the program successfully called the GitHub API:

```text
Hello from Python!
This program is running inside GitHub Actions
GitHub API status code: 200
Current user API URL: https://api.github.com/user
```

The workflow completed successfully:

```text
Job succeeded
```

---

## Key Takeaways

* Third-party packages must be declared in `requirements.txt`.
* Declaring dependencies does not install them automatically.
* `python -m pip install -r requirements.txt` installs the project dependencies.
* Package versions must exist and should be pinned for consistent builds.
* One direct dependency may install several transitive dependencies.
* GitHub Actions runners start from clean environments.
* Dependencies must be installed before the Python program runs.

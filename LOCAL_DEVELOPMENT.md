# Local Development

This document describes how to develop and test this project locally before pushing changes to GitHub.

---

# Development Workflow

The recommended development process is:

```text
Modify code
      ↓
Run Python locally
      ↓
Run GitHub Actions locally with act
      ↓
Verify everything works
      ↓
Create ONE commit
      ↓
Push to GitHub
```

This keeps the Git history clean and avoids creating many commits only for testing.

---

# Python Virtual Environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
python -m pip install -r requirements.txt
```

Deactivate the environment when finished:

```bash
deactivate
```

---

# Local Python Testing

Run the program directly:

```bash
python hello.py
```

This verifies:

* Python syntax
* Business logic
* Third-party dependencies
* API requests

It does **not** verify the GitHub Actions workflow.

---

# GitHub Actions Local Testing

This project uses **act** to simulate GitHub Actions locally.

Run the workflow:

```bash
act push \
  -W .github/workflows/python-demo.yml \
  -j run-python \
  -P ubuntu-24.04=catthehacker/ubuntu:act-latest \
  --container-architecture linux/amd64
```

This executes the workflow without creating commits or pushing to GitHub.

The workflow executed by `act` is the same workflow defined under:

```text
.github/workflows/
```

---

# Why Docker?

`act` simulates GitHub-hosted runners using Docker containers.

Each workflow execution runs inside a temporary container.

```text
Create Container
       ↓
Checkout Repository
       ↓
Setup Python
       ↓
Install Dependencies
       ↓
Run Program
       ↓
Destroy Container
```

Docker must be running before using `act`.

Verify Docker:

```bash
docker info
```

---

# Why `python -m pip`?

Prefer:

```bash
python -m pip install -r requirements.txt
```

instead of:

```bash
pip install -r requirements.txt
```

Using `python -m pip` guarantees that `pip` belongs to the currently selected Python interpreter.

---

# Common Errors

## Invalid Package Version

Error:

```text
No matching distribution found
```

Cause:

The package version specified in `requirements.txt` does not exist.

Example:

```text
requests==2.34.2
```

Fix:

Use a valid version:

```text
requests==2.32.5
```

---

## Dependency Not Installed

Error:

```text
ModuleNotFoundError
```

Cause:

The workflow did not install dependencies before running the Python program.

Fix:

```bash
python -m pip install -r requirements.txt
```

---

## Unsupported Platform

Error:

```text
Skipping unsupported platform
```

Cause:

`act` could not find a Docker image matching the runner label.

For this project:

```yaml
runs-on: ubuntu-24.04
```

Use:

```bash
-P ubuntu-24.04=catthehacker/ubuntu:act-latest
```

---

## Docker Not Running

Error:

```text
failed to connect to the docker API
```

Cause:

Docker Desktop is not running.

Verify:

```bash
docker info
```

---

# Notes

* Every GitHub Actions runner starts from a clean environment.
* Dependencies must be installed for every workflow run.
* Local testing should be completed before creating a commit.
* `act` is a simulator. The final verification should always be performed by GitHub Actions after pushing to GitHub.

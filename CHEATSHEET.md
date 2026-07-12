# GitHub Actions Demo Cheatsheet

Quick reference for developing and testing this repository.

## Python Virtual Environment

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

Deactivate it:

```bash
deactivate
```

Check the active Python:

```bash
which python
python --version
```

## Python Dependencies

Upgrade pip:

```bash
python -m pip install --upgrade pip
```

Install project dependencies:

```bash
python -m pip install -r requirements.txt
```

List installed packages:

```bash
python -m pip list
```

Show information about a package:

```bash
python -m pip show requests
```

## Run Python Locally

Run the Python demo:

```bash
python hello.py
```

## Docker

Check whether Docker is running:

```bash
docker info
```

Test Docker:

```bash
docker run --rm hello-world
```

View running containers:

```bash
docker ps
```

View all containers:

```bash
docker ps -a
```

## act

Check the installed version:

```bash
act --version
```

List available workflows and jobs:

```bash
act -l
```

Simulate all workflows triggered by `push`:

```bash
act push
```

Run the Python workflow:

```bash
act push \
  -W .github/workflows/python-demo.yml \
  -j run-python \
  -P ubuntu-24.04=catthehacker/ubuntu:act-latest \
  --container-architecture linux/amd64
```

Run with verbose logs:

```bash
act push \
  -W .github/workflows/python-demo.yml \
  -j run-python \
  -P ubuntu-24.04=catthehacker/ubuntu:act-latest \
  --container-architecture linux/amd64 \
  -v
```

Simulate a manual workflow trigger:

```bash
act workflow_dispatch \
  -W .github/workflows/python-demo.yml \
  -j run-python \
  -P ubuntu-24.04=catthehacker/ubuntu:act-latest \
  --container-architecture linux/amd64
```

## Git Review

Check changed files:

```bash
git status
```

Review unstaged changes:

```bash
git diff
```

Review staged changes:

```bash
git diff --staged
```

View recent commits:

```bash
git log --oneline --decorate -10
```

## Commit and Push

Stage selected files:

```bash
git add README.md hello.py requirements.txt
```

Stage all changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Add Python dependency demo"
```

Push to GitHub:

```bash
git push
```

## Recommended Workflow

```text
Modify files
    ↓
Run Python locally
    ↓
Run the workflow with act
    ↓
Review git status and git diff
    ↓
Create one commit
    ↓
Push to GitHub
    ↓
Verify the real GitHub Actions run
```

## Common Errors

### `No matching distribution found`

The requested package version probably does not exist.

Check `requirements.txt` and use a valid version:

```text
requests==2.32.5
```

### `ModuleNotFoundError`

Install the project dependencies:

```bash
python -m pip install -r requirements.txt
```

Also confirm that the Workflow installs dependencies before running Python.

### `Skipping unsupported platform`

Provide a Docker image mapping that matches `runs-on`:

```bash
-P ubuntu-24.04=catthehacker/ubuntu:act-latest
```

### `failed to connect to the docker API`

Start Docker Desktop and verify:

```bash
docker info
```

### Apple Silicon architecture warning

Add:

```bash
--container-architecture linux/amd64
```

## Key Files

```text
.github/workflows/main.yml
.github/workflows/python-demo.yml
docs/
hello.py
requirements.txt
README.md
LOCAL_DEVELOPMENT.md
CHEATSHEET.md
```

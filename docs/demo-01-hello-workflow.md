# Demo 01 - Hello GitHub Actions

## Goal

Create the first GitHub Actions workflow and run it manually.

---

## Files

```text
.github/workflows/main.yml
```

---

## Workflow

```yaml
name: Hello GitHub Actions

on:
  workflow_dispatch:

jobs:
  say-hello:
    runs-on: ubuntu-latest

    steps:
      - run: echo "Hello GitHub Actions!"
      - run: uname -a
      - run: date
```

---

## What I Learned

### Workflow

A workflow is an automation process defined in a YAML file.

```
Workflow
└── Job
    └── Steps
```

---

### workflow_dispatch

Allows a workflow to be started manually from the GitHub Actions page.

---

### Job

A collection of steps executed on the same runner.

---

### Runner

GitHub automatically creates a temporary virtual machine.

```
ubuntu-latest
```

---

### Step

Each command inside a job.

---

## Execution Flow

```
Click Run Workflow

↓

Create Ubuntu Runner

↓

Execute Steps

↓

Destroy Runner
```

---

## Commands Used

```bash
echo
uname -a
date
```

---

## Key Takeaways

- GitHub Actions uses YAML workflows.
- A workflow consists of Jobs.
- A Job consists of Steps.
- GitHub provides temporary runners.
- Workflows can be started manually.
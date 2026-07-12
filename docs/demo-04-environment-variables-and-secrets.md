# Demo 04 - Environment Variables and GitHub Secrets

## Goal

Learn how to pass configuration and sensitive information to a GitHub Actions workflow securely.

---

## Files

```text
environment_demo.py
.github/workflows/environment-demo.yml
```

---

## Why Environment Variables?

Applications often require configuration that changes between environments.

Examples:

* Application environment
* API endpoint
* Log level

Instead of hardcoding values, they should be provided through environment variables.

Example:

```text
APP_ENV=github-actions
```

Python reads them using:

```python
import os

app_env = os.getenv("APP_ENV")
```

---

## Why GitHub Secrets?

Sensitive values should never be committed to source control.

Examples:

* API Keys
* Access Tokens
* Passwords
* Webhook URLs

GitHub provides **Repository Secrets** to store these values securely.

The workflow accesses them using:

```yaml
${{ secrets.DEMO_SECRET }}
```

---

## Workflow

```yaml
name: Environment Variables and Secrets Demo

on:
  push:
    paths:
      - "environment_demo.py"
      - ".github/workflows/environment-demo.yml"
  workflow_dispatch:

jobs:
  environment-demo:
    runs-on: ubuntu-24.04

    steps:
      - name: Download repository code
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Run environment demo
        env:
          APP_ENV: github-actions
          DEMO_SECRET: ${{ secrets.DEMO_SECRET }}
        run: python environment_demo.py
```

---

## Python Program

The application reads the required environment variables:

```python
import os

app_env = os.getenv("APP_ENV")
secret = os.getenv("DEMO_SECRET")
```

A helper function validates that required variables exist before the application continues.

If a required variable is missing, the program exits with a non-zero status code.

---

## Environment Variable Flow

```text
Workflow
      │
      ▼
env:
APP_ENV=github-actions
      │
      ▼
Runner Environment
      │
      ▼
Python
os.getenv("APP_ENV")
```

---

## Secret Flow

```text
Repository Secret
DEMO_SECRET
        │
        ▼
${{ secrets.DEMO_SECRET }}
        │
        ▼
Workflow Step
        │
        ▼
Runner Environment
        │
        ▼
Python
os.getenv("DEMO_SECRET")
```

---

## Job-level vs Step-level Environment Variables

Environment variables can be defined at different scopes.

### Job-level

Available to every step in the job.

```yaml
jobs:
  demo:
    env:
      APP_ENV: github-actions
```

### Step-level

Available only to a specific step.

```yaml
- name: Run application
  env:
    APP_ENV: github-actions
    DEMO_SECRET: ${{ secrets.DEMO_SECRET }}
```

Step-level variables are useful when only one step requires a specific value, especially for secrets.

---

## Best Practices

### Use Environment Variables For

* Environment names
* API URLs
* Feature flags
* Log levels

### Use GitHub Secrets For

* API Keys
* Tokens
* Passwords
* Credentials

---

## Never Print Secrets

Avoid:

```python
print(secret)
```

Instead:

```python
print("DEMO_SECRET is configured successfully.")
```

This confirms that the secret exists without exposing its value.

---

## Errors Encountered

### Missing Required Environment Variable

If a required variable is not provided:

```text
Error: required environment variable 'APP_ENV' is missing.
```

The program exits immediately with a non-zero exit code.

---

### Missing `return` Statement

During development, the helper function accidentally omitted:

```python
return value
```

As a result:

```text
Application environment: None
```

even though `os.getenv()` successfully read the environment variable.

This bug demonstrated that reading the environment variable and returning the value are two separate operations.

---

## Result

The workflow successfully received both the environment variable and the GitHub Secret.

Example output:

```text
Application environment: github-actions
DEMO_SECRET is configured successfully.
The application can safely use the secret.
```

---

## Local Testing Command
```shell
act push \
  -W .github/workflows/environment-demo.yml \
  -j environment-demo \
  -P ubuntu-24.04=catthehacker/ubuntu:act-latest \
  --container-architecture linux/amd64 \
  -s DEMO_SECRET
```

---

## Key Takeaways

* Environment variables separate configuration from application code.
* GitHub Secrets securely store sensitive values.
* Python reads environment variables using `os.getenv()`.
* Validate required configuration before running the application.
* Never hardcode or print secrets.
* Step-level environment variables are useful for limiting the scope of sensitive values.

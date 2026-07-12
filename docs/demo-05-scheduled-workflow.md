# Demo 05 - Scheduled Workflows

## Goal

Learn how to run GitHub Actions workflows automatically using Cron schedules.

---

## Files

```text
scheduled_demo.py
.github/workflows/scheduled-demo.yml
```

---

## Workflow

```yaml
name: Scheduled Workflow Demo

on:
  schedule:
    - cron: "37 23 * * 1-5"

  workflow_dispatch:

jobs:
  scheduled-demo:
    runs-on: ubuntu-24.04

    steps:
      - name: Download repository code
        uses: actions/checkout@v6

      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: "3.12"

      - name: Run scheduled demo
        run: python scheduled_demo.py
```

---

## Python Program

The program prints:

- Trigger event
- Current UTC time
- Current Seattle time

Example:

```python
event_name = os.getenv("GITHUB_EVENT_NAME", "local")

utc_now = datetime.now(timezone.utc)
seattle_now = utc_now.astimezone(
    ZoneInfo("America/Los_Angeles")
)
```

---

## Schedule Trigger

A workflow can be started automatically using:

```yaml
on:
  schedule:
```

GitHub creates a **schedule event**, which starts the workflow automatically.

The workflow itself does **not** wait until the scheduled time.

---

## Cron Expression

GitHub Actions uses standard POSIX Cron syntax.

```
┌──────── minute (0-59)
│ ┌────── hour (0-23)
│ │ ┌──── day of month (1-31)
│ │ │ ┌── month (1-12)
│ │ │ │ ┌ day of week (0-6)
│ │ │ │ │
37 23 * * 1-5
```

Meaning:

- Minute: 37
- Hour: 23 (UTC)
- Every day
- Every month
- Monday through Friday

---

## Common Examples

Every day at 08:15 UTC

```text
15 8 * * *
```

Every Monday at 17:30 UTC

```text
30 17 * * 1
```

Every weekday at 23:37 UTC

```text
37 23 * * 1-5
```

Every 30 minutes

```text
*/30 * * * *
```

---

## UTC Time

GitHub Actions schedules are always evaluated in UTC.

During daylight saving time:

```
UTC 23:37
↓

Seattle 16:37 PDT
```

During winter:

```
UTC 23:37
↓

Seattle 15:37 PST
```

---

## Multiple Triggers

A workflow can support multiple triggers.

Example:

```yaml
on:
  schedule:
    - cron: "37 23 * * 1-5"

  workflow_dispatch:
```

This allows:

- automatic execution
- manual execution for testing

---

## Local Testing

`act` cannot simulate the GitHub Scheduler.

Instead, it simulates the **schedule event**.

Run:

```bash
act schedule \
  -W .github/workflows/scheduled-demo.yml \
  -j scheduled-demo \
  -P ubuntu-24.04=catthehacker/ubuntu:act-latest \
  --container-architecture linux/amd64
```

Expected output:

```text
Trigger event: schedule
```

This verifies that:

- the workflow is valid
- the schedule event is handled correctly
- the Python program runs successfully

It does **not** verify that GitHub will execute the workflow at the specified time.

---

## Real Schedule Testing

To verify Cron:

1. Push the workflow to the default branch.
2. Wait until the scheduled time.
3. Check the Actions page.

The workflow should start automatically without any manual action.

---

## Troubleshooting

### 1. `isoformat` vs `isoformat()`

**Problem**

The workflow printed:

```text
Current UTC time: <built-in method isoformat of datetime.datetime object ...>
```

**Cause**

The `isoformat` method was referenced instead of being called.

Incorrect:

```python
print(utc_now.isoformat)
```

Correct:

```python
print(utc_now.isoformat())
```

---

### 2. `act schedule` does not wait for Cron

**Problem**

I expected `act schedule` to wait until the scheduled Cron time.

**Explanation**

`act` does **not** include GitHub's cloud scheduler.

Instead, it directly simulates a `schedule` event.

```
act schedule
        │
        ▼
schedule event
        ▼
Workflow starts immediately
```

To verify the actual Cron schedule, the workflow must be pushed to GitHub and allowed to run automatically.

---

### 3. GitHub Actions schedules use UTC

GitHub evaluates all Cron expressions in **UTC**, not the local time zone.

Example:

```
23:37 UTC
```

In Seattle:

- Summer (PDT): **16:37**
- Winter (PST): **15:37**

Always convert your local time to UTC before writing the Cron expression.

---

### 4. Scheduled workflows only run from the default branch

GitHub only executes scheduled workflows that exist on the repository's **default branch** (typically `main`).

Workflows on feature branches are ignored by the scheduler.

---

### 5. Scheduled workflows may be delayed

GitHub does not guarantee that scheduled workflows start at the exact scheduled minute.

A workflow scheduled for:

```
23:37 UTC
```

may actually start a few minutes later during periods of high platform load.

---

## Key Takeaways

- `schedule` automatically starts workflows.
- GitHub Actions uses UTC for all Cron schedules.
- `workflow_dispatch` is useful for manual testing.
- `act schedule` simulates a schedule event but not the GitHub Scheduler.
- Scheduled workflows only run from the default branch.
- Scheduled workflows may be delayed during periods of high GitHub Actions load.
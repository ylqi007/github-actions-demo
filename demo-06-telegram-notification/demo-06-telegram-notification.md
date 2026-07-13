# Demo 06 — Daily Telegram Notification with GitHub Actions

> **Goal**
>
> Build a production-style GitHub Actions workflow that automatically sends a Telegram notification every morning at **8:45 AM Pacific Time**.

---

# 1. Introduction

This is the first demo in this repository that integrates GitHub Actions with a real external service.

Unlike previous demos that mainly focused on workflow syntax or GitHub Actions features, this demo introduces a complete automation pipeline.

```
GitHub Actions
        │
        ▼
Load Secrets
        │
        ▼
Generate Date & Time
        │
        ▼
Load Random Quote
        │
        ▼
Build Telegram Message
        │
        ▼
HTTP POST
        │
        ▼
Telegram Bot API
        │
        ▼
Telegram Notification
```

This project demonstrates how GitHub Actions can automate real-world tasks rather than simply executing shell commands.

---

# 2. Learning Objectives

After completing this demo, I should understand:

## GitHub Actions

* schedule trigger
* workflow_dispatch
* GitHub Context
* GitHub Secrets
* Runner Environment
* Environment Variables

## Bash

* Variables
* Command substitution
* String interpolation
* File operations
* Random file selection
* Multi-line message construction

## HTTP

* GET Request
* POST Request
* HTTP Parameters
* JSON Response

## Telegram

* BotFather
* Bot Token
* Chat ID
* Telegram Bot API

## Local Development

* act
* Docker Runner
* Local Secret Management

---

# 3. Final Result

Every morning Telegram receives something similar to:

```
🌅 早上好！今日寄语

✅ 自律不是限制，而是给未来的自己更多选择。

📅 Sunday, July 12, 2026
🕗 08:45:00 AM PDT

📦 Repository：github-actions-demo
🌿 Branch：main
👤 Trigger：schedule
🔢 Run Number：27
```

---

# 4. Project Structure

```
.github/
└── workflows/
    └── telegram-daily-notification.yml

demo-06-telegram-notification/
├── README.md
├── demo-06-telegram-notification-github-actions.md
├── quotes.txt
└── scripts/
    └── send-telegram-message.sh
```

---

# 5. Architecture

```
GitHub Schedule

        │

        ▼

Runner starts

        │

        ▼

Load Secrets

        │

        ▼

Generate current date/time

        │

        ▼

Randomly select one quote

        │

        ▼

Construct message

        │

        ▼

POST request

        │

        ▼

Telegram Bot API

        │

        ▼

Telegram Message
```

---

# 6. Telegram Fundamentals

## What is Telegram Bot?

A Telegram Bot is a special Telegram account controlled by software instead of a human.

Bots can:

* Receive messages
* Send messages
* Respond to commands
* Call APIs
* Integrate with automation workflows

---

## BotFather

Telegram provides an official bot called **BotFather**.

BotFather is responsible for:

* Creating bots
* Managing bots
* Resetting Bot Tokens
* Configuring bot settings

Command used:

```
/newbot
```

---

## Bot Token

Example:

```
123456789:AAxxxxxxxxxxxxxxxxxxxx
```

The Bot Token acts like a password.

Never commit it into Git.

Instead:

```
GitHub Secrets
```

---

## Chat ID

Telegram does NOT send messages by username.

Instead it sends messages using

```
chat_id
```

The correct value is

```
message.chat.id
```

NOT

```
update_id

message_id

from.id
```

---

# 7. Telegram Bot API

This demo uses

```
sendMessage
```

Endpoint

```
POST

https://api.telegram.org/bot<TOKEN>/sendMessage
```

Parameters

```
chat_id

text
```

Example

```
curl \
  --request POST \
  https://api.telegram.org/bot<TOKEN>/sendMessage \
  --data-urlencode "chat_id=xxxx" \
  --data-urlencode "text=Hello"
```

---

# 8. GitHub Secrets

Sensitive information should never be committed into source control.

Secrets used in this demo:

```
TELEGRAM_BOT_TOKEN

TELEGRAM_CHAT_ID
```

Workflow:

```yaml
env:
  TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
```

Benefits:

* encrypted
* hidden in logs
* secure
* repository scoped

---

# 9. GitHub Context

GitHub automatically exposes workflow metadata.

Useful examples:

Repository

```
github.event.repository.name
```

Branch

```
github.ref_name
```

Trigger

```
github.event_name
```

Run Number

```
github.run_number
```

These values allow the notification to include execution information automatically.

---

# 10. Bash Techniques

## Command Substitution

```
current_date="$(date)"
```

Output of a command becomes a variable.

---

## Variables

```
quote="Hello"

echo "$quote"
```

---

## Random Line

```
shuf -n 1 quotes.txt
```

Randomly selects one line.

---

## String Interpolation

```
message+="📦 ${repository}"
```

Variables are expanded automatically.

---

## Why We Avoided printf

Initially the notification message was built using

```
printf
```

Example

```
printf "...%s...%s..." \
    "$a" \
    "$b"
```

Although this works, it becomes difficult to maintain.

Problems encountered:

* parameters easily become misaligned
* adding one new field shifts every placeholder
* debugging becomes difficult

Instead, we switched to string concatenation:

```
message="..."
message+="..."
message+=$'\n'
```

Advantages:

* much easier to read
* easier to maintain
* easier to debug
* less error-prone

---

# 11. Time Zone

GitHub Scheduled Workflow always uses

```
UTC
```

Our desired schedule

```
08:45 AM PDT
```

Therefore we convert time using

```
TZ=America/Los_Angeles
```

Example

```
current_time="$(TZ=America/Los_Angeles date '+%I:%M:%S %p %Z')"
```

---

# 12. Local Testing

Instead of pushing every change to GitHub, we use

```
act
```

Advantages

* much faster iteration
* local debugging
* no unnecessary commits

Command

```
act workflow_dispatch \
  -W .github/workflows/telegram-daily-notification.yml \
  --secret-file .secrets
```

---

# 13. Troubleshooting

## Problem 1

### Error

```
dquote>
```

### Cause

Unclosed quotation mark.

### Solution

Press

```
Ctrl + C
```

Re-enter the command.

---

## Problem 2

### Error

```
400 chat not found
```

### Cause

Incorrect Chat ID.

### Solution

Use

```
message.chat.id
```

---

## Problem 3

### Error

```
result:[]
```

### Cause

No message had been sent to the bot.

### Solution

Open the bot.

Click

```
START
```

Send

```
Hello
```

Run

```
getUpdates
```

again.

---

## Problem 4

### Error

```
quotes.txt
No such file
```

### Cause

Wrong file path.

### Solution

Verify

* actions/checkout executed
* file exists
* working directory is correct

---

## Problem 5

### Error

```
wanted EOF
```

### Cause

Incorrect heredoc indentation.

### Solution

Stop using heredoc.

Use normal Bash string construction.

---

## Problem 6

### Error

Notification fields shifted.

Example

```
Repository became Branch

Branch became Trigger
```

### Cause

printf placeholders (%s) and parameters were inconsistent.

### Solution

Use string concatenation instead.

---

## Problem 7

### Error

Current time empty.

### Cause

Variable assignment failed.

### Solution

Print variables using

```
echo
```

before sending.

---

## Problem 8

### Error

Run Number empty.

### Cause

act does not fully emulate GitHub Context.

### Solution

Use fallback values locally.

GitHub Actions will populate

```
github.run_number
```

correctly.

---

# 14. Best Practices

✔ Never commit Bot Tokens.

✔ Store credentials in GitHub Secrets.

✔ Keep shell scripts under the scripts directory.

✔ Store reusable data (quotes) in separate files.

✔ Prefer readable Bash over clever Bash.

✔ Add debug output before making HTTP requests.

✔ Test locally with act before pushing.

---

# 15. Possible Improvements

This demo can be extended in many directions.

## AI Quote

Generate a motivational quote using an LLM instead of reading from quotes.txt.

---

## Stock Market Reminder

Integrate Yahoo Finance.

Example

```
QQQ
Above MA200

NVDA
Below MA200
```

---

## Weather

Send today's weather.

---

## Calendar

Send today's meetings.

---

## News

Send AI news summary.

---

## Daily Dashboard

Combine

* weather
* stock market
* calendar
* motivational quote

into one morning notification.

---

# 16. Knowledge Map

```
GitHub Actions
        │
        ├── schedule
        ├── workflow_dispatch
        ├── Context
        ├── Secrets
        │
        ▼
Runner
        │
        ▼
Bash
        │
        ├── Variables
        ├── Files
        ├── Strings
        └── HTTP
                │
                ▼
Telegram Bot API
                │
                ▼
Telegram
```

---

# 17. Key Takeaways

Before this demo, GitHub Actions was primarily a tool for running scripts.

After this demo, it became a practical automation platform capable of interacting with external services through secure credentials and HTTP APIs.

This project introduced several important engineering concepts:

* integrating third-party APIs
* managing secrets securely
* building reusable shell scripts
* debugging automation workflows
* testing locally with act
* understanding GitHub Context
* handling time zones correctly

Most importantly, this is the first workflow in this repository that performs a real-world task with immediate user value.

It also serves as the foundation for future automation projects, such as stock monitoring, AI-generated daily reports, weather notifications, and other scheduled workflows.

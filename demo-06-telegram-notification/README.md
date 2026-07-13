# Demo 06 — Daily Telegram Notification with GitHub Actions

## Overview

In this demo, we build our first **end-to-end automation workflow** using GitHub Actions.

Every morning at **8:45 AM Pacific Time**, GitHub Actions automatically sends a Telegram notification containing:

* 🌅 A daily greeting
* 💡 A randomly selected motivational quote
* 📅 Current date
* 🕗 Current time
* 📦 Repository information
* 🌿 Current branch
* 👤 Trigger type
* 🔢 Workflow run number

This demo is much more than simply sending a Telegram message. It demonstrates how GitHub Actions interacts with external services through HTTP APIs, securely manages credentials, processes data in Bash, and automates repetitive daily tasks.

---

# Learning Objectives

After completing this demo, you should understand:

## GitHub Actions

* Scheduled workflows (`schedule`)
* Manual workflows (`workflow_dispatch`)
* Workflow execution lifecycle
* Environment variables
* GitHub Context
* GitHub Secrets

## Bash

* Variable assignment
* String interpolation
* Multi-line strings
* File operations
* Random file selection
* Environment variables
* Basic

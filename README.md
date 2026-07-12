# GitHub Actions Demo

A collection of small, incremental demos for learning GitHub Actions from scratch.

## Learning Progress

* ✅ **Demo 01** - Manually trigger a workflow with `workflow_dispatch`
* ✅ **Demo 02** - Automatically run a Python program on `push`
* ✅ **Demo 03** - Install and use Python dependencies with `requirements.txt`
* ✅ **Demo 04** - Use environment variables and GitHub Secrets
* ✅ **Demo 05** - Scheduled Workflows (Cron)

## Key Concepts Learned

* Workflow
* Trigger (`push`, `workflow_dispatch`)
* Job
* Runner
* Step
* `run`
* `uses`
* `actions/checkout`
* `actions/setup-python`
* `requirements.txt`
* `python -m pip`
* Direct and transitive dependencies

## Repository Structure

```text
github-actions-demo/
├── .github/
│   └── workflows/
│       ├── main.yml
│       └── python-demo.yml
├── docs/
│   ├── demo-01-hello-workflow.md
│   ├── demo-02-run-python.md
│   └── demo-03-python-dependencies.md
├── hello.py
├── requirements.txt
└── README.md
```

## Demo Documentation

* [Demo 01 - Hello GitHub Actions](docs/demo-01-hello-workflow.md)
* [Demo 02 - Run Python on Push](docs/demo-02-run-python.md)
* [Demo 03 - Python Dependencies](docs/demo-03-python-dependencies.md)
* [Demo 04 - Environment Variables and Secrets](docs/demo-04-environment-variables-and-secrets.md)
* - [Demo 05 - Scheduled Workflows](docs/demo-05-scheduled-workflow.md)

## Current Workflow

The Python workflow performs the following steps:

```text
Push or manual trigger
        ↓
Checkout repository
        ↓
Set up Python
        ↓
Install dependencies
        ↓
Run Python program
```

## Next Demo

- Run workflows automatically on a schedule with cron

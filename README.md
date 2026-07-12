# github-actions-demo

A collection of small, incremental demos for learning GitHub Actions from scratch.

## Learning Progress

* ✅ **Demo 1** - Manually trigger a workflow (`workflow_dispatch`)
* ✅ **Demo 2** - Automatically run a Python program on every `push`

## Key Concepts Learned

* Workflow
* Trigger (`push`, `workflow_dispatch`)
* Job
* Runner (`ubuntu-latest`)
* Step
* `run`
* `uses`
* `actions/checkout`
* `actions/setup-python`

## Repository Structure

```text
.github/
└── workflows/
    ├── main.yml
    └── python-demo.yml

hello.py
README.md
```

## Next Demo

* Install Python dependencies (`requirements.txt`)
* Run programs that use third-party libraries (e.g. `requests`, `pandas`)
* Understand how GitHub Actions manages project dependencies

# Code Quality & Formatting Standard

This repository uses automated tools to enforce coding standards and ensure consistent formatting.
Quality checks are automatically enforced on `git commit` via pre-commit hooks.

## Auto-Detected Tooling

- **Python Linter & Formatter:** `Ruff` (replaces Black, isort, Flake8).
- **Commit Linter:** `commitlint` (enforces Conventional Commits).

## Environment Setup

Run this once after cloning the project:

```bash
pip install -e ".[dev]"
pre-commit install
pre-commit install --hook-type commit-msg
```

## Manual Execution Commands

**Run all checks on ALL files repository-wide:**

```bash
pre-commit run --all-files
```

**Run checks ONLY on staged files:**

```bash
pre-commit run
```

**Run Ruff directly (without pre-commit):**

```bash
ruff check .      # Linting
ruff check --fix . # Linting & auto-fixing
ruff format .     # Formatting
```

## Maintenance & Cache

Update hooks to their latest versions:

```bash
pre-commit autoupdate
```

Clear tool caches:

```bash
pre-commit clean
```

## Emergency Bypassing

If you must skip the pre-commit checks (e.g., for an urgent hotfix), you can bypass them by appending the `--no-verify`
flag:

```bash
git commit -m "fix(urgent): patch prod issue" --no-verify
```

*Warning: Use this sparingly. CI pipelines will still run quality checks and block non-compliant code.*

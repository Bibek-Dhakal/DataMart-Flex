# Contributing to DataMart-Flex

First, thank you for your interest in contributing to DataMart-Flex!

## Development Setup

1. Clone the repository.
2. Install Python dependencies: `pip install -e ".[dev,notebooks]"`
3. Install pre-commit hooks: `pre-commit install`
4. Copy `.env.example` to `.env` and adjust the variables if necessary.

## Code Quality

This project enforces code quality standards using Ruff and automated Pre-commit hooks.
Please review `docs/code_quality.md` for specific instructions on how to run linting and formatting.

## Commit Guidelines (Strictly Enforced)

This project uses **Automated Versioning & Changelog Generation** powered by `release-please`.
Because of this, **ALL commit messages must strictly adhere to the Conventional Commits specification**.

### Commit Format

```text
type(optional-scope): description in imperative mood
```

### Allowed Types

* `feat:` A new feature (triggers a Minor release).
* `fix:` A bug fix (triggers a Patch release).
* `feat!:` or `fix!:` A breaking change (triggers a Major release).
* `docs:`, `chore:`, `style:`, `refactor:`, `perf:`, `test:` - Maintenance tasks that generally do not trigger a release
  on their own, but may be grouped into the changelog.

**Example:**
`feat(etl): add DuckDB aggregation script for Fact_Orders`

### Pull Requests

All pull requests will be squashed and merged, or rebased. Ensure your PR title also follows the Conventional Commits
format, as the PR title will become the squashed commit message in the `main` branch.

When your PR is merged, `release-please` will automatically update the pending Release PR draft, tracking the
appropriate version bump.

# Testing Strategy

## Overview

DataMart-Flex focuses on data integrity testing and pipeline unit testing.

## Execution

Run the test suite using `pytest`:

```bash
pytest
```

## Coverage

To view the coverage report:

```bash
pytest --cov=src --cov-report=html
```

*(Note: Test suites are to be implemented as the project scales. Currently, you can run Pytest to ensure structural
integrity and zero syntax failures).*

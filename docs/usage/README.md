# Usage & Operation Guide

## Executing the Pipeline

The primary entry point to generate the Data Mart is the `src/pipeline.py` script.
This script coordinates:

1. Generating raw transactional data (`src/generate_mock_data.py`).
2. Creating and populating the dimensional model in DuckDB (`src/build_star_schema.py`).

### Command

```bash
python -m src.pipeline
```

## Environment Variables

The application relies on `.env` configuration. Ensure this file is created from `.env.example`.

| Variable                | Default Value          | Description                                          |
|-------------------------|------------------------|------------------------------------------------------|
| `ENVIRONMENT`           | `development`          | Operating context.                                   |
| `DUCKDB_PATH`           | `data/datamart.duckdb` | Output path for the DuckDB analytical database file. |
| `MOCK_NUM_CUSTOMERS`    | `5000`                 | Number of mock customers to generate.                |
| `MOCK_NUM_PRODUCTS`     | `200`                  | Number of mock products to generate.                 |
| `MOCK_NUM_TRANSACTIONS` | `100000`               | Number of raw fact transactions to generate.         |

## BI & Analytics Hub Integration

Once the `.duckdb` database file is generated, it serves as the central data mart for BI applications.

- **[Loading DuckDB into Power BI](loading-duck-db-in-power-BI.md)**: A step-by-step guide to installing the ODBC
  driver, configuring the read-only connection string, and importing the tables without lock errors.
- **[DAX Measures & Semantic Layer](../architecture/dax_measures.md)**: Explicit BI calculations (Revenue, Time
  Intelligence, YoY) to build inside your dashboard once the data is loaded.

---

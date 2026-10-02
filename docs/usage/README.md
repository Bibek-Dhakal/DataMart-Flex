# Usage & Operation Guide

## Executing the Pipeline

The primary entry point to generate the Data Mart is the `src/pipeline.py` script.
This script coordinates:

1. Generating raw transactional data (`src/generate_mock_data.py`).
2. Creating and populating the dimensional model in DuckDB (`src/build_star_schema.py`).

### Command

```bash
python src/pipeline.py
```

## Environment Variables

The application relies on `.env` configuration. Ensure this file is created from `.env.example`.

| Variable | Default Value | Description |
|---|---|---|
| `ENVIRONMENT` | `development` | Operating context. |
| `DUCKDB_PATH` | `data/datamart.duckdb` | Output path for the DuckDB analytical database file. |
| `MOCK_NUM_CUSTOMERS` | `5000` | Number of mock customers to generate. |
| `MOCK_NUM_PRODUCTS` | `200` | Number of mock products to generate. |
| `MOCK_NUM_TRANSACTIONS`| `100000` | Number of raw fact transactions to generate. |

# DataMart-Flex

**DataMart-Flex** is an Enterprise Star-Schema Data Mart and Self-Serve BI Analytics Hub pipeline. It addresses
cross-functional analytics fragmentation by establishing a centralized, Kimball-methodology dimensional model.

## Core Features

- **Automated Data Pipeline:** Generates mock transactional data and transforms it using high-performance SQL (DuckDB)
  into a clean star schema.
- **Enterprise Star-Schema:** Centralized `Fact_Orders` connected to `Dim_Customers`, `Dim_Products`, `Dim_Date`, and
  `Dim_Channels` via strict 1-to-Many relationships.
- **Advanced BI Measures:** Explicit DAX/LOD measure documentation for building responsive, executive self-serve
  dashboards (YTD, QTD, MoM, Rolling Averages).

## Quick Start

```bash
# 1. Install dependencies
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -e ".[dev,notebooks]"

# 2. Run the Pipeline
python src/pipeline.py
```

This will output `data/datamart.duckdb` containing the fully materialized star schema.

## Documentation Index

- [Architecture & Design](docs/architecture/README.md)
- [Data Dictionary](docs/architecture/data_dictionary.md)
- [DAX & BI Measures](docs/architecture/dax_measures.md)
- [Code Quality & Standards](docs/code_quality.md)
- [Usage & Environment](docs/usage/README.md)
- [Testing Strategy](docs/testing/README.md)
- [Roadmap](docs/roadmap/README.md)

## License

MIT License.

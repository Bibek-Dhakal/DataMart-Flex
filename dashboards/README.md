# BI Analytics Showcase

This directory contains the final Business Intelligence artifacts connected to the **DataMart-Flex** star schema.

## Power BI Integration

The primary showcase is built using Microsoft Power BI, utilizing the explicit DAX measures defined in
the [DAX & BI Measures](../docs/architecture/dax_measures.md) documentation.

### How to Use the `.pbix` File

1. Run the Python ETL pipeline (`python -m src.pipeline`) from the project root to generate your local
   `data/datamart.duckdb` database.
2. Ensure you have the **DuckDB ODBC Driver** installed on your system to allow Power BI to interface directly with the
   database file.
3. Open the `.pbix` file located in this folder.
4. If prompted to refresh or update credentials, edit the Data Source settings to point to your local absolute path of
   `datamart.duckdb`.

*(Optional: Add a screenshot of the dashboard below by dropping an image file into this folder and uncommenting the line
below)*
<!-- ![Power BI Dashboard Preview](preview.png) -->

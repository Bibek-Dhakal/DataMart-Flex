# Architecture Documentation

This directory contains technical design documents, data models, and BI semantic definitions.

## Index

- [Data Dictionary](data_dictionary.md): Exhaustive mapping of tables, relationships, and columns in the star schema.
- [DAX Measures](dax_measures.md): The explicit DAX/LOD measures required for the BI Visualization Layer.

## System Flow Diagram

```mermaid
graph TD;
    A[Raw Transactions & APIs] --> B[Python Ingestion Layer];
    B --> C[(Staging Database)];
    C --> D[DuckDB SQL Transformation];
    D --> E[Fact_Orders];
    D --> F[Dim_Customers];
    D --> G[Dim_Products];
    D --> H[Dim_Date];
    D --> I[Dim_Channels];
    E --> J[Power BI / Tableau Hub];
    F --> J;
    G --> J;
    H --> J;
    I --> J;
```

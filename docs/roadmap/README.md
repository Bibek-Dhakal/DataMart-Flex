# Project Roadmap

## Phase 1: MVP (Completed)

- [x] Initial Repository Setup (Conventional Commits, Pre-commit).
- [x] Mock Data Generation Scripts.
- [x] DuckDB Star Schema Transformation Pipeline.
- [x] Data Dictionary and DAX Definitions.

## Phase 2: Orchestration & BI Integration

- [ ] Migrate scheduling to Apache Airflow or GitHub Actions cron triggers.
- [ ] Export automated reporting endpoints for Tableau/Power BI ingestion.
- [ ] Implement dbt (Data Build Tool) on top of DuckDB for more robust testing and modeling.

## Phase 3: Analytics Expansion

- [ ] Integrate SST 1 (Automated Customer Cohort Retention) into `Dim_Customers`.
- [ ] Integrate SST 2 (Statistical A/B Testing Outcomes) into a new `Fact_Experiments` table.

# BI Layer: Explicit DAX Measures

To maintain performance and standard definitions across the Enterprise Self-Serve BI Analytics Hub, **implicit measures
are strictly forbidden**.

Use the following explicit DAX measures (Power BI) in your visualization layer.

### 1. Base Aggregations

```dax
Total Revenue = SUM(Fact_Orders[sales_amount])

Total Cost = SUM(Fact_Orders[cost_amount])

Gross Margin $ = [Total Revenue] - [Total Cost]

Gross Margin % = DIVIDE([Gross Margin $], [Total Revenue], 0)

Total Orders = DISTINCTCOUNT(Fact_Orders[order_id])

Total Units Sold = SUM(Fact_Orders[quantity])
```

### 2. Time Intelligence (Period-over-Period)

```dax
-- Year-to-Date
YTD Revenue = TOTALYTD([Total Revenue], Dim_Date[full_date])

-- Quarter-to-Date
QTD Revenue = TOTALQTD([Total Revenue], Dim_Date[full_date])

-- Previous Month Revenue
Prev Month Revenue = CALCULATE([Total Revenue], DATEADD(Dim_Date[full_date], -1, MONTH))

-- Month-over-Month Growth %
MoM Revenue Growth = DIVIDE([Total Revenue] - [Prev Month Revenue], [Prev Month Revenue], 0)
```

### 3. Advanced & Rolling Metrics

```dax
-- Rolling 90-Day Revenue Average
Rolling 90D Revenue =
CALCULATE(
    [Total Revenue],
    DATESINPERIOD(Dim_Date[full_date], MAX(Dim_Date[full_date]), -90, DAY)
) / 90

-- Active Customers (Customers with at least 1 purchase in selected period)
Active Customers = CALCULATE(DISTINCTCOUNT(Fact_Orders[customer_key]), Fact_Orders[sales_amount] > 0)
```

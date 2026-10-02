import os

import duckdb
from dotenv import load_dotenv

load_dotenv()


def build_data_mart():
    db_path = os.getenv("DUCKDB_PATH", "data/datamart.duckdb")
    print(f"Building Star Schema in {db_path}...")

    # Connect to DuckDB
    con = duckdb.connect(db_path)

    # 1. Dim_Date Construction (Generated purely via SQL in DuckDB)
    con.execute(
        """
        CREATE OR REPLACE TABLE Dim_Date AS
        SELECT
            CAST(strftime(date_seq, '%Y%m%d') AS INT) AS date_key,
            date_seq::DATE AS full_date,
            EXTRACT(year FROM date_seq) AS year,
            EXTRACT(quarter FROM date_seq) AS quarter,
            EXTRACT(month FROM date_seq) AS month_num,
            strftime(date_seq, '%b') AS month_name,
            CASE WHEN EXTRACT(isodow FROM date_seq) IN (6, 7) THEN TRUE ELSE FALSE END AS is_weekend
        FROM generate_series(DATE '2020-01-01', DATE '2030-12-31', INTERVAL 1 DAY) AS t(date_seq);
    """
    )

    # 2. Dim_Customers
    con.execute(
        """
        CREATE OR REPLACE TABLE Dim_Customers AS
        SELECT * FROM read_csv_auto('data/raw_customers.csv');
    """
    )

    # 3. Dim_Products
    con.execute(
        """
        CREATE OR REPLACE TABLE Dim_Products AS
        SELECT * FROM read_csv_auto('data/raw_products.csv');
    """
    )

    # 4. Dim_Channels
    con.execute(
        """
        CREATE OR REPLACE TABLE Dim_Channels AS
        SELECT * FROM read_csv_auto('data/raw_channels.csv');
    """
    )

    # 5. Fact_Orders
    con.execute(
        """
        CREATE OR REPLACE TABLE Fact_Orders AS
        SELECT
            t.order_id,
            t.customer_key,
            t.product_key,
            CAST(strftime(CAST(t.transaction_date AS DATE), '%Y%m%d') AS INT) AS date_key,
            t.channel_key,
            t.quantity,
            t.unit_price,
            (t.quantity * t.unit_price) AS sales_amount,
            t.cost_amount,
            t.discount_amount
        FROM read_csv_auto('data/raw_transactions.csv') t;
    """
    )

    print("Star Schema modeling complete. Fact and Dimension tables are loaded.")
    con.close()


if __name__ == "__main__":
    build_data_mart()

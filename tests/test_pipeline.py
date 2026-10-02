import os
import tempfile
from unittest import mock

import duckdb
import pandas as pd

from src.build_star_schema import build_data_mart
from src.generate_mock_data import generate_data
from src.pipeline import run_pipeline


def test_generate_mock_data():
    with tempfile.TemporaryDirectory() as tmp_dir:
        generate_data(10, 5, 20, output_dir=tmp_dir)

        assert os.path.exists(os.path.join(tmp_dir, "raw_customers.csv"))
        assert os.path.exists(os.path.join(tmp_dir, "raw_products.csv"))
        assert os.path.exists(os.path.join(tmp_dir, "raw_channels.csv"))
        assert os.path.exists(os.path.join(tmp_dir, "raw_transactions.csv"))

        df = pd.read_csv(os.path.join(tmp_dir, "raw_transactions.csv"))
        assert len(df) == 20


def test_build_star_schema():
    with tempfile.TemporaryDirectory() as tmp_dir:
        # First generate data context
        generate_data(10, 5, 20, output_dir=tmp_dir)

        db_path = os.path.join(tmp_dir, "datamart.duckdb")
        with mock.patch.dict(os.environ, {"DUCKDB_PATH": db_path}):
            build_data_mart(data_dir=tmp_dir)

            assert os.path.exists(db_path)

            # Verify tables exist and schema mapped cleanly
            con = duckdb.connect(db_path)
            tables = [row[0] for row in con.execute("SHOW TABLES").fetchall()]
            assert "Dim_Date" in tables
            assert "Dim_Customers" in tables
            assert "Dim_Products" in tables
            assert "Dim_Channels" in tables
            assert "Fact_Orders" in tables
            con.close()


def test_run_pipeline():
    with tempfile.TemporaryDirectory() as tmp_dir:
        db_path = os.path.join(tmp_dir, "datamart.duckdb")
        env_vars = {
            "MOCK_NUM_CUSTOMERS": "10",
            "MOCK_NUM_PRODUCTS": "5",
            "MOCK_NUM_TRANSACTIONS": "20",
            "DATA_DIR": tmp_dir,
            "DUCKDB_PATH": db_path,
        }

        # Test full pipeline end-to-end integration via mocked environment config
        with mock.patch.dict(os.environ, env_vars):
            run_pipeline()

            assert os.path.exists(os.path.join(tmp_dir, "raw_transactions.csv"))
            assert os.path.exists(db_path)

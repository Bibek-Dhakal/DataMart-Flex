import os

from dotenv import load_dotenv

from src.build_star_schema import build_data_mart
from src.generate_mock_data import generate_data


def run_pipeline():
    load_dotenv()

    num_customers = int(os.getenv("MOCK_NUM_CUSTOMERS", 5000))
    num_products = int(os.getenv("MOCK_NUM_PRODUCTS", 200))
    num_txns = int(os.getenv("MOCK_NUM_TRANSACTIONS", 100000))

    print("=== DataMart-Flex Pipeline Started ===")
    generate_data(num_customers=num_customers, num_products=num_products, num_transactions=num_txns)

    build_data_mart()
    print("=== DataMart-Flex Pipeline Completed Successfully ===")


if __name__ == "__main__":
    run_pipeline()

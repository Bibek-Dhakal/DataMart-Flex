import os
import random

import pandas as pd
from dotenv import load_dotenv
from faker import Faker

load_dotenv()
fake = Faker()


def generate_data(
    num_customers: int, num_products: int, num_transactions: int, output_dir: str = "data"
):
    print(
        f"Generating mock data: {num_customers} customers, {num_products} products, "
        f"{num_transactions} tens..."
    )
    os.makedirs(output_dir, exist_ok=True)

    # 1. Customers
    customers = []
    segments = ["Enterprise", "SMB", "Consumer"]
    for _ in range(num_customers):
        customers.append(
            {
                "customer_key": fake.uuid4(),
                "full_name": fake.name(),
                "segment": random.choice(segments),
                "country": fake.country(),
                "signup_date": fake.date_between(start_date="-3y", end_date="today").strftime(
                    "%Y-%m-%d"
                ),
            }
        )
    df_customers = pd.DataFrame(customers)
    df_customers.to_csv(f"{output_dir}/raw_customers.csv", index=False)

    # 2. Products
    products = []
    categories = {
        "Electronics": ["Laptops", "Smartphones", "Tablets", "Audio"],
        "Apparel": ["T-Shirts", "Jackets", "Shoes", "Accessories"],
        "Home": ["Furniture", "Kitchen", "Decor"],
    }
    for _ in range(num_products):
        cat = random.choice(list(categories.keys()))
        subcat = random.choice(categories[cat])
        products.append(
            {
                "product_key": fake.uuid4(),
                "product_name": fake.catch_phrase(),
                "category": cat,
                "subcategory": subcat,
                "base_cost": round(random.uniform(10.0, 500.0), 2),
            }
        )
    df_products = pd.DataFrame(products)
    df_products.to_csv(f"{output_dir}/raw_products.csv", index=False)

    # 3. Channels
    channels = [
        {"channel_key": "CH01", "channel_name": "Organic Search", "campaign": "Always On"},
        {"channel_key": "CH02", "channel_name": "Paid Social", "campaign": "Summer Sale"},
        {"channel_key": "CH03", "channel_name": "Direct", "campaign": "None"},
        {"channel_key": "CH04", "channel_name": "Email", "campaign": "Newsletter Q3"},
    ]
    df_channels = pd.DataFrame(channels)
    df_channels.to_csv(f"{output_dir}/raw_channels.csv", index=False)

    # 4. Transactions
    transactions = []
    cust_keys = df_customers["customer_key"].tolist()
    prod_keys = df_products["product_key"].tolist()
    chan_keys = df_channels["channel_key"].tolist()

    for _ in range(num_transactions):
        p_key = random.choice(prod_keys)
        base_cost = df_products.loc[df_products["product_key"] == p_key, "base_cost"].values[0]
        markup = random.uniform(1.2, 2.5)
        unit_price = round(base_cost * markup, 2)
        quantity = random.randint(1, 5)

        transactions.append(
            {
                "order_id": fake.uuid4(),
                "customer_key": random.choice(cust_keys),
                "product_key": p_key,
                "channel_key": random.choice(chan_keys),
                "transaction_date": fake.date_between(start_date="-2y", end_date="today").strftime(
                    "%Y-%m-%d"
                ),
                "quantity": quantity,
                "unit_price": unit_price,
                "discount_amount": round(random.uniform(0, 10.0), 2)
                if random.random() > 0.8
                else 0.0,
                "cost_amount": round(base_cost * quantity, 2),
            }
        )
    df_transactions = pd.DataFrame(transactions)
    df_transactions.to_csv(f"{output_dir}/raw_transactions.csv", index=False)

    print("Mock data generation complete.")


if __name__ == "__main__":
    generate_data(100, 20, 1000)

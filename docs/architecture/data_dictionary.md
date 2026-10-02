# Enterprise Star-Schema Data Dictionary

DataMart-Flex follows the **Kimball Dimensional Modeling Methodology**. All tables maintain strict unidirectional
1-to-Many filtering from Dimension tables to Fact tables.

## 1. Fact Table: `Fact_Orders`

Captures the transactional events at the grain of a single line item order.

| Column Name | Data Type | Key Type | Description |
|---|---|---|---|
| `order_id` | VARCHAR | Primary Key | Unique identifier for the transaction. |
| `customer_key` | VARCHAR | Foreign Key | Links to `Dim_Customers`. |
| `product_key` | VARCHAR | Foreign Key | Links to `Dim_Products`. |
| `date_key` | INT | Foreign Key | Links to `Dim_Date` (Format: YYYYMMDD). |
| `channel_key` | VARCHAR | Foreign Key | Links to `Dim_Channels`. |
| `quantity` | INT | Measure | Number of units purchased. |
| `unit_price` | DECIMAL | Measure | Price per single unit at the time of purchase. |
| `sales_amount` | DECIMAL | Measure | Total revenue (`quantity * unit_price`). |
| `cost_amount` | DECIMAL | Measure | Total cost of goods sold. |
| `discount_amount` | DECIMAL | Measure | Any applied discount value. |

## 2. Dimension Table: `Dim_Customers`

Contains attributes related to purchasing users.

| Column Name | Data Type | Description |
|---|---|---|
| `customer_key` | VARCHAR | Surrogate/Primary key for the customer. |
| `full_name` | VARCHAR | Customer's full name. |
| `segment` | VARCHAR | Customer grouping (e.g., Enterprise, SMB, Consumer). |
| `country` | VARCHAR | Billing country. |
| `signup_date` | DATE | Date the customer first registered. |

## 3. Dimension Table: `Dim_Products`

Product catalog hierarchy.

| Column Name | Data Type | Description |
|---|---|---|
| `product_key` | VARCHAR | Surrogate/Primary key for the product. |
| `product_name` | VARCHAR | Name of the product. |
| `category` | VARCHAR | High-level grouping (e.g., Electronics, Apparel). |
| `subcategory` | VARCHAR | Granular grouping (e.g., Laptops, T-Shirts). |
| `base_cost` | DECIMAL | Standard unit cost. |

## 4. Dimension Table: `Dim_Date`

Standard calendar table for Time Intelligence capabilities.

| Column Name | Data Type | Description |
|---|---|---|
| `date_key` | INT | Primary key (YYYYMMDD). |
| `full_date` | DATE | The actual date value. |
| `year` | INT | Year (e.g., 2024). |
| `quarter` | INT | Quarter (1, 2, 3, 4). |
| `month_num` | INT | Month number (1-12). |
| `month_name` | VARCHAR | Month text (Jan, Feb...). |
| `is_weekend` | BOOLEAN | True if Saturday or Sunday. |

## 5. Dimension Table: `Dim_Channels`

Marketing and acquisition channels.

| Column Name | Data Type | Description |
|---|---|---|
| `channel_key` | VARCHAR | Surrogate/Primary key for the channel. |
| `channel_name` | VARCHAR | E.g., Organic Search, Paid Social, Direct. |
| `campaign` | VARCHAR | Specific campaign identifier. |

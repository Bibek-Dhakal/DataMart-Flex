## How to Connect Power BI to DuckDB (`.duckdb` File)

Importing data into Power BI from a local DuckDB `.duckdb` file requires configuring the official DuckDB ODBC driver and
passing **`access_mode=read_only`** in the connection string to prevent file lock errors when loading multiple tables
simultaneously.

---

### Step 1: Install the DuckDB ODBC Driver

1. Download the official 64-bit DuckDB ODBC driver for Windows.
2. Run the installer and complete the setup wizard.

---

### Step 2: Configure the Windows ODBC Data Source

1. Press `Win + S` on Windows, search for **ODBC Data Sources (64-bit)**, and open it.
2. Under the **User DSN** tab, click **Add...**
3. Select **DuckDB Driver** from the list and click **Finish**.
4. In the configuration window:

* **Data Source Name:** Enter `DataMart-Flex_DB`.
* **Database:** Enter the path to your file (e.g., `d:\00_projects\datamart-flex\data\datamart.duckdb`).

5. Click **Finish**, then click **OK** to save and exit.

---

### Step 3: Load Data into Power BI Desktop

1. Open **Power BI Desktop**.
2. Go to **Home** $\rightarrow$ **Get data** $\rightarrow$ **More...** $\rightarrow$ **Other** $\rightarrow$ **ODBC**,
   then click **Connect**.
3. In the ODBC dialog:

* Select **`DataMart-Flex_DB`** from the Data Source Name (DSN) dropdown.
* Expand **Advanced options**.
* In the **Connection string (non-credential properties)** field, paste :

```text
Driver={DuckDB Driver};Database={{ABSOLUTE_PATH_TO_YOUR_DUCK_DB_FILE}};access_mode=read_only;

```

Example:

```text
Driver={DuckDB Driver};Database=d:\00_projects\datamart-flex\data\datamart.duckdb;access_mode=read_only;

```

4. Click **OK**.
5. On the credentials prompt screen:

* Select **Custom** from the left-hand menu.
* Leave the credential fields blank (DuckDB does not use ODBC credentials).
* Click **Connect**.


6. In the **Navigator** window, check the tables you want to import (`Dim_Customers`, `Dim_Date`, `Dim_Products`,
   `Fact_Orders`).
7. Click **Load** to import all database tables into Power BI.

---

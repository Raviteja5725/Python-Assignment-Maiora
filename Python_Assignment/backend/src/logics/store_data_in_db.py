import pandas as pd
import sqlite3
import os

# Database file
DB_FILE = "sales_data.db"
TABLE_NAME = "sales_data"

# CSV file paths (Replace with actual paths)
CSV_FILES = {
    "A": "src/files/order_region_a.csv",
    "B": "src/files/order_region_b.csv"
}

# Create SQLite connection
def get_db_connection():
    return sqlite3.connect(DB_FILE)

# Function to load and transform data
def load_and_transform_data():
    all_data = []
    
    for region, file_path in CSV_FILES.items():
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV file not found: {file_path}")
        
        df = pd.read_csv(file_path)
        df["region"] = region 
        df["total_sales"] = df["QuantityOrdered"] * df["ItemPrice"]  
        df["net_sales"] = df["total_sales"] - df["PromotionDiscount"]  
        df = df[df["net_sales"] > 0]  
        all_data.append(df)
    
    return pd.concat(all_data, ignore_index=True)

# Function to store transformed data in SQLite
def store_data_in_db():
    df = load_and_transform_data()
    conn = get_db_connection()
    df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
    conn.close()

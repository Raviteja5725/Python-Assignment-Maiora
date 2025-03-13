from src.logics.store_data_in_db import get_db_connection


async def get_average_sales():
    TABLE_NAME = "sales_data"  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT AVG(total_sales) FROM {TABLE_NAME}")
    avg_sales = cursor.fetchone()[0]
    conn.close()
    return {"average_sales": avg_sales}
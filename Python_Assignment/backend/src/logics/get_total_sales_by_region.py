from src.logics.store_data_in_db import get_db_connection

async def get_total_sales_by_region():
    
    TABLE_NAME = "sales_data"  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT region, SUM(total_sales) FROM {TABLE_NAME} GROUP BY region")
    result = cursor.fetchall()
    conn.close()
    return {"sales_by_region": result}
from src.logics.store_data_in_db import get_db_connection

async def get_total_records():
    TABLE_NAME = "sales_data"  
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM {TABLE_NAME}")
    count = cursor.fetchone()[0]
    conn.close()
    return {"total_records": count}

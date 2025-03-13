from src.logics.store_data_in_db import get_db_connection

async def get_check_duplicates():
    TABLE_NAME = "sales_data"
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT OrderId, COUNT(*) FROM {TABLE_NAME} GROUP BY OrderId HAVING COUNT(*) > 1")
    duplicates = cursor.fetchall()
    conn.close()
    return {"duplicate_orders": duplicates}   
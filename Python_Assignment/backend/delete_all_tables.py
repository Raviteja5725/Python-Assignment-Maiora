import asyncpg
import asyncio

DB_DETAILS = {
    "host": "192.168.0.112",
    "port": "5432",
    "user": "postgres",
    "password": "postgres",
    "database": "archive_raviteja"
}

async def drop_all_tables():
    conn = await asyncpg.connect(**DB_DETAILS)
    try:
        # Get all table names
        tables = await conn.fetch("""
            SELECT tablename FROM pg_tables
            WHERE schemaname = 'public';
        """)
        
        # Drop each table
        for table in tables:
            table_name = table['tablename']
            print(f"Dropping table: {table_name}")
            await conn.execute(f'DROP TABLE IF EXISTS "{table_name}" CASCADE;')
        
        print("All tables dropped successfully.")
    finally:
        await conn.close()

asyncio.run(drop_all_tables())

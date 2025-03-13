import requests
from src.logics.store_data_in_db import get_db_connection

async def connect_sqllite_db():
    url = "https://v2.jokeapi.dev/joke/Any?amount=100"
    response = requests.get(url)
    if response.status_code == 200:
        jokes_data = response.json().get("jokes", [])
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS jokes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                category TEXT,
                type TEXT,
                joke TEXT,
                setup TEXT,
                delivery TEXT,
                nsfw BOOLEAN,
                political BOOLEAN,
                sexist BOOLEAN,
                safe BOOLEAN,
                lang TEXT
            )
        """)
        for joke in jokes_data:
            cursor.execute("""
                INSERT INTO jokes (category, type, joke, setup, delivery, nsfw, political, sexist, safe, lang)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                joke.get("category"),
                joke.get("type"),
                joke.get("joke") if joke.get("type") == "single" else None,
                joke.get("setup") if joke.get("type") == "twopart" else None,
                joke.get("delivery") if joke.get("type") == "twopart" else None,
                joke.get("flags", {}).get("nsfw", False),
                joke.get("flags", {}).get("political", False),
                joke.get("flags", {}).get("sexist", False),
                joke.get("safe", False),
                joke.get("lang")
            ))
        conn.commit()
        conn.close()
        return {"message": "Jokes fetched and stored successfully"}
    return {"error": "Failed to fetch jokes"}
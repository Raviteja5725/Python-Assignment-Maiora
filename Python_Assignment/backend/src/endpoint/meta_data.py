from fastapi import FastAPI, HTTPException,APIRouter, Depends, Response, Request
from pydantic import BaseModel
# from src.connection.connect_db import get_database_url,create_db_engine
from src.schamas.basemodels.schemas import meta_data
from src.schamas.orm_models.model import Joke
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, Session
from src.connection.test_coonection import test_db_connection
from src.connection.connect_db import initialize_database, get_db, get_database_url
from src.logics.store_data_in_db import store_data_in_db,get_db_connection
from src.logics.connect_sqllite_db import connect_sqllite_db
from src.logics.get_total_records import get_total_records
from src.logics.get_total_sales_by_region import get_total_sales_by_region
from src.logics.get_check_duplicates import get_check_duplicates
from src.logics.get_average_sales import get_average_sales

import requests

app = FastAPI()


@app.post("/test-connection/")
async def meta_db_connection(db_details: meta_data):
    print(db_details)
    return  await test_db_connection(db_details)   

# API to fetch jokes and store in SQLite
@app.get("/fetch-jokes_sqllite_db/")
async def fetch_jokes():
    return await connect_sqllite_db()
    

@app.get("/fetch-jokes_oracledb/")
def fetch_jokes(db: Session = Depends(get_db)):
    
    url = "https://v2.jokeapi.dev/joke/Any?amount=100"
    response = requests.get(url)
    if response.status_code == 200:
        jokes_data = response.json().get("jokes", [])
        for joke in jokes_data:
            db_joke = Joke(
                category=joke.get("category"),
                type=joke.get("type"),
                joke=joke.get("joke") if joke.get("type") == "single" else None,
                setup=joke.get("setup") if joke.get("type") == "twopart" else None,
                delivery=joke.get("delivery") if joke.get("type") == "twopart" else None,
                nsfw=joke.get("flags", {}).get("nsfw", False),
                political=joke.get("flags", {}).get("political", False),
                sexist=joke.get("flags", {}).get("sexist", False),
                safe=joke.get("safe", False),
                lang=joke.get("lang")
            )
            db.add(db_joke)
        db.commit()
        return {"message": "Jokes fetched and stored successfully"}
    return {"error": "Failed to fetch jokes"}

# API to load sales-data
@app.post("/load-sales-data/")
def load_sales_data():
    try:
        store_data_in_db()
        return {"message": "Sales data loaded successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# API to get total number of records

@app.get("/total-records/")
async def total_records():
    
    return await get_total_records()
   

# API to get total sales by region
@app.get("/total-sales-by-region/")
async def total_sales_by_region():
    return await get_total_sales_by_region()
   

# API to get average sales per transaction
@app.get("/average-sales/")
async def average_sales():
    
    return await get_average_sales()
   

# API to check duplicate OrderIds
@app.get("/check-duplicates/")
async def check_duplicates():
    
    return await get_check_duplicates()
   
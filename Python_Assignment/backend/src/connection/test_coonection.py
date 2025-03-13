from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import json
import os
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from src.schamas.orm_models.model import Base

async def   test_db_connection(db_details):
    try:
        db_url = f"postgresql://{db_details.username}:{db_details.psswrd}@{db_details.host}:{db_details.port}/{db_details.databaseName}"
        engine = create_engine(db_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        
        # Test connection
        with engine.connect() as connection:
            connection.execute(text("SELECT 1")) 

        # Create tables if not exist
        Base.metadata.create_all(bind=engine)
       
        # Prepare metadata_config
        metadata_config = {
            "metadata_config": db_details.dict()
        }

        # Save to properties.json
        json_path = os.path.abspath('src/connection/properties.json')
        with open(json_path, "w") as file:
            json.dump(metadata_config, file, indent=4)
       
        return {"message": "Connection successful!", "database": db_details.databaseName}
    except OperationalError:
        raise HTTPException(status_code=400, detail="Failed to connect to the database.")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,Session
from src.schamas.basemodels.schemas import meta_data
from sqlalchemy.engine import Engine
import json
import os


engine = None
SessionLocal = None

def load_db_config():
    
    """Read database details from properties.json"""
    
    json_path = os.path.abspath('src/connection/properties.json')
    with open(json_path, "r") as file:
        data = json.load(file)
    return data["metadata_config"]

def get_database_url(config):
    
    """Generate the database connection URL dynamically"""
    
    if config["databaseType"].lower() == "oracle":
        return f"oracle+cx_oracle://{config['username']}:{config['psswrd']}@{config['host']}:{config['port']}/{config['databaseName']}"
    elif config["databaseType"].lower() == "sqlite":
        return f"sqlite:///{config['databaseName']}.db"
    elif config["databaseType"].lower() == "postgresql":
        return f"postgresql://{config['username']}:{config['psswrd']}@{config['host']}:{config['port']}/{config['databaseName']}"
    else:
        raise ValueError("Unsupported database type")


def initialize_database():
    
    """Initialize the database connection dynamically from JSON"""
    global engine, SessionLocal
    if engine is None:  # Avoid re-initializing if already set
        config = load_db_config()  
        database_url = get_database_url(config)
        engine = create_engine(database_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Provide a database session, ensuring DB is initialized"""
    initialize_database() 

    if engine is None or SessionLocal is None:
        raise ValueError("Database session is not initialized. Call initialize_database() first.")
    
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

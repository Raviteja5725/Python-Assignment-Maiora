
from pydantic import BaseModel

class meta_data(BaseModel):
    databaseType: str
    host: str
    port: str
    username: str
    psswrd: str
    databaseName: str
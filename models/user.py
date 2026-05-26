from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    name: str
    id : str 
    description: str | None = None
    date_created: datetime 

class User(BaseModel):
    username: str
    id : str
    email: str
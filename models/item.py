from pydantic import BaseModel
from datetime import datetime


class Item(BaseModel):
    name: str
    id : str 
    description: str | None = None
    date_created: datetime 
    category: str  

class ItemCreate(BaseModel):
    name: str 
    description: str | None = None
    category: str 
    



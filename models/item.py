from pydantic import BaseModel, ConfigDict
from datetime import datetime


class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    category: str


class ItemRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str
    name: str
    description: str | None = None
    category: str
    date_created: datetime

    



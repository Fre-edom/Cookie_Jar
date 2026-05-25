from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import uuid

class Item(BaseModel):
    name: str
    id : str 
    description: str | None = None

class User(BaseModel):
    username: str
    id : str
    email: str

app = FastAPI()

items = []
users = []


@app.get("/")
async def root():
    return {"message": "I am working!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/about")
async def about():
    return {"app": "about page", "version": "1.0.0"}  

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}", "description": f"Item {item_id}."}   

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "username": f"user{user_id}", "email": f"user{user_id}@mail.com"}

@app.get("/search")
async def search(q: str):
    return {"query": q, "results": [f"Result for {q} 1", f"Result for {q} 2", f"Result for {q} 3"]}

@app.post("/items/")
async def create_item(Item: Item):
    items.append(Item)
    id = str(uuid.uuid4())
    return Item

@app.post("/users/")
async def create_user(User: User):
    users.append(User)
    id = str(uuid.uuid4())
    return User

@app.put("/items/{item_id}")
async def update_item(item_id: int, Item: Item):
    return {"item_id": item_id, **Item.dict()}

@app.put("/users/{user_id}")
async def update_user(user_id: int, User: User):
    return {"user_id": user_id, **User.dict()}

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):    
    return {"user_id": user_id, "status": "deleted"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):    
    return {"item_id": item_id, "status": "deleted"}


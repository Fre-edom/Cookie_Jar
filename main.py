from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import uuid
from models import Item, User


app = FastAPI()

#items = []

items = {
        "rr": {"name": "mylist", "description": "a random list", "id": "rr", "date_created": "2024-06-01T12:00:00Z"}
         }
users = []




#******************************************************************* Define general get API endpoints ************************************************************************
@app.get("/")
async def root():
    return {"message": "I am working!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/home")
async def home():
    return {"message": "Welcome home!"}

@app.get("/about")
async def about():
    return {"app": "about page", "version": "1.0.0"}  



@app.get("/search")
async def search(q: str):
    return {"query": q, "results": [f"Result for {q} 1", f"Result for {q} 2", f"Result for {q} 3"]}


#******************************************************************* Define item and user get API endpoints ************************************************************************
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}   

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id, "username": f"user{user_id}", "email": f"user{user_id}@mail.com"}


#******************************************************************* Define post API endpoints ************************************************************************
@app.post("/items/")
async def create_item(item: Item):
  #  items.append(item)
    item.id = str(uuid.uuid4())
    items[item.id] = item
    return item

@app.post("/users/")
async def create_user(User: User):
    users.append(User)
    id = str(uuid.uuid4())
    return User

#******************************************************************* Define put API endpoints ************************************************************************
@app.put("/items/{item_id}")
async def update_item(item_id: str, Item: Item):
    return {"item_id": item_id, **Item.dict()}

@app.put("/users/{user_id}")
async def update_user(user_id: str, User: User):
    return {"user_id": user_id, **User.dict()}



#******************************************************************* Define delete API endpoints ************************************************************************
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):    
    return {"user_id": user_id, "status": "deleted"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: str):    
    return {"item_id": item_id, "status": "deleted"}


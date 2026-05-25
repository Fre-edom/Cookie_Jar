from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


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
async def create_item(name: str, description: str = None):
    return {"name": name, "description": description}

@app.post("/users/")
async def create_user(username: str, email: str):
    return {"username": username, "email": email}

@app.put("/items/{item_id}")
async def update_item(item_id: int, name: str = None, description: str = None):
    return {"item_id": item_id, "name": name, "description": description}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):    
    return {"item_id": item_id, "status": "deleted"}


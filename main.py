from fastapi import FastAPI

# Vercel searches for this 'app' variable
app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI on Vercel"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


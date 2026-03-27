# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn app:app --reload

from fastapi import FastAPI

app = FastAPI()


# With just the Query Parameters
@app.get("/items")
async def get_items(count: int = 2, name: str = None):
    return {"count": count, "name": name}


# With both Path and Query Parameters
@app.get("/item/{item_id}")
async def get_item(item_id: int, count: int = 2, name: str = None):
    return {"item_id": item_id, "count": count, "name": name}

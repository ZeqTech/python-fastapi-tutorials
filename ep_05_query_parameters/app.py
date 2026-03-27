# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn app:app --reload
# - go to http://localhost:8000/docs

from enum import Enum
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


# With List Query Parameters
@app.get("/items")
async def get_item_list(items: list[str] | None = None):
    return {"items": items}


# With Enum Query Parameters
class Fruit(Enum):
    APPLE = "apple"
    BANANA = "banana"
    PEAR = "pear"


@app.get("/fruits/")
async def read_items(fruit: Fruit):
    query_items = {"fruit": fruit.value}
    return query_items

# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn app_enum:app --reload

from enum import Enum

from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Tutorial",
)

class Fruit(Enum):
    apple = "apple"
    banana = "banana"
    orange = "orange"


@app.get("/fruits/{fruit}")
async def get_fruit(fruit: Fruit):
    return {"fruit": fruit.value}

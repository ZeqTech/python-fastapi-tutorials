# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn extracted.app:app --reload

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

AnnotatedItemID = Annotated[
    str,
    Path(
        ...,
        title="The String ID of the Item to get",
        max_length=5,
        examples=["abc", "def"],
    ),
]

AnnotatedItemAmount = Annotated[
    int, Path(..., title="The number of items to get", ge=1, le=99)
]


@app.get("/items/{item_id}/{amount}")
async def get_item(item_id: AnnotatedItemID, amount: AnnotatedItemAmount):
    return {"item_id": item_id, "amount": amount}

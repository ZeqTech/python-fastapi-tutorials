# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn app:app --reload
# - go to http://localhost:8000/docs

from typing import Annotated
from pydantic import AfterValidator
from fastapi import FastAPI, Query

app = FastAPI()


# The Base way of using Query Parameters
@app.get("/v1/items")
async def get_items_v1(
    q: str | None,
):
    return {"q": q}


# Using Query with default values and validations
@app.get("/v2/items")
async def get_items_v2(
    q: str | None = Query(default=None, title="Query string", max_length=50),
):
    return {"q": q}


# Using Query with type annotations and validations
@app.get("/v3/items")
async def get_items_v3(
    q: Annotated[str | None, Query(title="Query string", max_length=50)],
):
    return {"q": q}


# Using Query with type annotations and custom validations
def check_id(value: str) -> str:
    if not value.startswith(("isbn-", "imdb-")):
        raise ValueError("ID must start with 'isbn-' or 'imdb-'")
    return value


@app.get("/v4/items")
async def get_items_v4(
    id: Annotated[str | None, AfterValidator(check_id)],
):
    return {"id": id}


# Using Query with type annotations and custom validations and Query Class
@app.get("/v5/items")
async def get_items_v5(
    id: Annotated[
        str | None, AfterValidator(check_id), Query(title="Query string", max_length=50)
    ],
):
    return {"id": id}

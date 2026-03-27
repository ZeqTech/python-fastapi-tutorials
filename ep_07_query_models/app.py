# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn app:app --reload
# - go to http://localhost:8000/docs

from typing import Annotated
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field

app = FastAPI()


class FilterParams(BaseModel):
    model = {"extra": "forbid"} # Remove this line to allow extra fields in the query parameters
    
    limit: int = Field(default=100, ge=1, le=100, description="Number of items to return")
    offset: int = Field(default=0, ge=0, description="The offset for pagination")


@app.get("/items")
async def get_item(params: Annotated[FilterParams, Query()]):
    return {"limit": params.limit, "offset": params.offset}

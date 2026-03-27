# https://www.youtube.com/@zeqtech
#
# Run this file with:
# - uvicorn inline.app:app --reload

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/users/{user_id}/posts/{post_id}")
async def get_item(
    user_id: Annotated[int, Path(title="The ID of the user", ge=1)],
    post_id: Annotated[int, Path(title="The ID of the post", ge=1, le=100)],
    count: int = 2,
    name: str = None,
):
    return {"user_id": user_id, "post_id": post_id, "count": count, "name": name}

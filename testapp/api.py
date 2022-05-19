"""A simple test api using FastAPI"""
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

apiapp = FastAPI()


class BodyModel(BaseModel):
    """Simple pydantic model for the FastAPI body"""
    name: str
    value: float


@apiapp.post("/exercise/{path}")
async def exercise_function(
    path: str,
    query: int = 1,
    body: Union[BodyModel, None] = None
) -> dict:
    """A test API POST method

    Parameters
    ----------
    path : str
        the URL path being called
    query : int, optional
        a query parameter, by default 1
    body : Union[BodyModel, None], optional
        The request body if provided, by default None

    Returns
    -------
    dict
        Just returns the provided parameters
    """
    return {"path": path, "query": query, "body": body}


@apiapp.get("/items/{item_id}")
async def get_items(
    item_id: int,
    query: int = 1,
) -> dict:
    """A test API GET Method
    """
    return {"data": f"Gotten {item_id} with query param {query}"}

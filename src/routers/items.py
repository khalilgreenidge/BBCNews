from typing import Union
from fastapi import APIRouter
from Models.Item import Item


router = APIRouter(prefix="/items", tags=["items"], responses={404: {"body": "item not found"}})


@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.put("/")
def read_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags=["items"],
    responses={404: {"description": "Not found"}},
)


@router.get("/items")
async def read_items():
    return {}

# @router.get("/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in fake_items_db:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"name": fake_items_db[item_id]["name"], "item_id": item_id}

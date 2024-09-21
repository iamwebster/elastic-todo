from fastapi import APIRouter 


router = APIRouter(
    prefix="/items"
)


@router.get("")
async def get_items():
    pass 


@router.post("")
async def create_items():
    pass 


@router.get("/{item_id}")
async def get_detail_item(item_id: int):
    pass 


@router.put("/{item_id}")
async def update_item(item_id: int):
    pass 


@router.delete("/{item_id}")
async def delete_item(item_id: int):
    pass 

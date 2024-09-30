from fastapi import APIRouter, status, Depends

from elasticsearch import AsyncElasticsearch

from src.api.dependency import get_es
from src.api.schemas.user_schemas import UserBase, UserResponse
from src.service.user_service import get_users_data, create_user_in_db


router = APIRouter(
    tags=["User"],
    prefix="/users"
)


@router.get("", response_model=list[UserResponse])
async def get_all_users(es: AsyncElasticsearch = Depends(get_es)):
    users_data = await get_users_data(es)
    return users_data


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserBase, es: AsyncElasticsearch = Depends(get_es)):
    user_id = await create_user_in_db(
        es=es, user_data=user_data
    )
    return {"user_id": user_id} 

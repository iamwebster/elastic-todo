from elasticsearch import AsyncElasticsearch 

from src.config import USERS_INDEX
from src.api.schemas.user_schemas import UserBase
from src.utils.project_utils import get_current_datetime_with_tz


def map_to_user_list(users_data: dict) -> list[dict]:
    list_of_users_data = [] 
    if not users_data["hits"]["hits"]:
        return list_of_users_data
    
    for user_data in users_data["hits"]["hits"]:
        parsed_user_data = {
            "id": user_data["_id"],
            "name": user_data["_source"]["personal"]["name"],
            "phone": user_data["_source"]["contacts"]["phone"],
            "created_at": user_data["_source"]["created_at"]
        }
        if user_data["_source"]["personal"].get("surname"):
            parsed_user_data["surname"] = user_data["_source"]["personal"]["surname"]
        if user_data["_source"]["personal"].get("age"):
            parsed_user_data["age"] = user_data["_source"]["personal"]["age"]
        if user_data["_source"]["contacts"].get("email"):
            parsed_user_data["email"] = user_data["_source"]["contacts"]["email"]

        list_of_users_data.append(parsed_user_data)
    return list_of_users_data

async def get_users_data(es: AsyncElasticsearch):
    users_data = await es.search(index=USERS_INDEX)
    return map_to_user_list(users_data)


def get_user_payload(user_data: UserBase) -> dict:
    payload = {
        "personal": {
            "name": user_data.name,
        },
        "contacts": {
            "phone": "8493021834",
        },
        "created_at": get_current_datetime_with_tz()
    }

    if user_data.surname:
        payload["personal"]["surname"] = user_data.surname
    if user_data.age:
        payload["personal"]["age"] = user_data.age
    if user_data.email:
        payload["contacts"]["email"] = user_data.email

    return payload

async def create_user_in_db(es: AsyncElasticsearch, user_data: UserBase) -> str:
    user_payload = get_user_payload(user_data)
    es_response = await es.index(index=USERS_INDEX, body=user_payload)
    return es_response["_id"]

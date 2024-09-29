from elasticsearch import AsyncElasticsearch 

from src.config import USERS_INDEX


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

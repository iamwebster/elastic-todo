from elasticsearch import AsyncElasticsearch 

from src.config import USERS_INDEX


async def map_to_user_list(users_data: dict):
    pass 

async def get_users_data(es: AsyncElasticsearch):
    query = {
        "query": {
            "match_all": {}
        }
    }
    users_data = es.search(index=USERS_INDEX, body=query)
    return map_to_user_list(users_data)

from fastapi import Request
from elasticsearch import AsyncElasticsearch


async def get_es(request: Request) -> AsyncElasticsearch:
    return request.app.state.es_client

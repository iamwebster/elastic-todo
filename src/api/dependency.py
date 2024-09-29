from elasticsearch import AsyncElasticsearch

from src.config import elastic_config


async def get_es():
    elastic_cred = elastic_config.get_cred()
    es = await AsyncElasticsearch(**elastic_cred)
    try:
        yield es
    finally:
        await es.close()
from contextlib import asynccontextmanager 

from elasticsearch import AsyncElasticsearch
from fastapi import FastAPI

from src.api import user_endpoint
from src.config import elastic_conf


@asynccontextmanager
async def lifespan(app: FastAPI):
    elastic_cred = elastic_conf.get_cred()
    app.state.es_client = AsyncElasticsearch(**elastic_cred)
    yield 
    await app.state.es_client.close()

app = FastAPI(
    lifespan=lifespan
)
app.include_router(user_endpoint.router)


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("src.main:app", reload=True)

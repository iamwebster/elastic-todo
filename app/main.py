from fastapi import FastAPI

from app.api import item_endpoint 


application = FastAPI()
application.include_router(item_endpoint.router)

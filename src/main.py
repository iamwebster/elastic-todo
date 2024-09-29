from fastapi import FastAPI

from src.api import user_endpoint


app = FastAPI()
app.include_router(user_endpoint.router)


if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("src.main:app", reload=True)

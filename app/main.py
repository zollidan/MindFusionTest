from fastapi import Depends, FastAPI

from .routers import index_routes, users

app = FastAPI()

app.include_router(users.router)
app.include_router(index_routes.router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}



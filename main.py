import uvicorn
from fastapi import FastAPI
from Config.Connection import prisma_connection


def init_app():
    apps = FastAPI(
        title="Lemon code 21",
        description="Fast API",
        version="1.0.0"
    )

    @apps.on_event("startup")
    async def startup():
        await prisma_connection.connect()

    @apps.on_event("shutdown")
    async def shutdown():
        await prisma_connection.disconnect()

    @apps.get('/')
    def home():
        return "welcome home!"

    from Controller import post

    apps.include_router(post.router)

    return apps


app = init_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8888, reload=True)


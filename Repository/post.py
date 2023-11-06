from Model.post import CreatePost
from Config.Connection import prisma_connection

class PostRepository:

    @staticmethod
    async def get_all():
        return await prisma_connection.prisma.post.find_many()

    @staticmethod
    async def create(post: CreatePost):
        return await prisma_connection.prisma.post.create({
            "post": post.post,
            "description": post.description
        })

    @staticmethod
    async def get_by_id(post_id: int):
        return await prisma_connection.prisma.post.find_first(where={"id": post_id})

    @staticmethod
    async def delete(post_id: int):
        await prisma_connection.prisma.post.delete(where={"id": post_id})

    @staticmethod
    async def update(post_id: int, post: CreatePost):
        await prisma_connection.prisma.post.update(where={"id": post_id}, data={
            "post": post.post,
            "description": post.description
        })

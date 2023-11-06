from Repository.post import PostRepository
from Model.post import CreatePost


class PostService:

    @staticmethod
    async def get_all():
        return await PostRepository.get_all()

    @staticmethod
    async def get_by_id(post_id: int):
        return await PostRepository.get_by_id(post_id)

    @staticmethod
    async def delete(post_id: int):
        return await PostRepository.delete(post_id)

    @staticmethod
    async def create(data: CreatePost):
        return await PostRepository.create(data)

    @staticmethod
    async def update(post_id: int, data: CreatePost):
        return await PostRepository.update(post_id, data)

from pydantic import BaseModel
from prisma import Prisma


class CreatePost(BaseModel):
    post: str
    description: str


class RetrievePost(BaseModel):
    id: int
    post: str
    description: str

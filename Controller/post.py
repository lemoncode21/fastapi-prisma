from fastapi import APIRouter, Path
from schema import ResponseSchema
from Service.post import PostService
from Model.post import CreatePost

router = APIRouter(
    prefix="/post",
    tags=['post'],
)


@router.get("", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_all_post():
    result = await PostService.get_all()
    return ResponseSchema(detail="Successfully get all data!", result=result)


@router.get("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id_post(post_id: int = Path(..., alias="id")):
    result = await PostService.get_by_id(post_id)
    return ResponseSchema(detail="Successfully get by id data!", result=result)


@router.post("", response_model=ResponseSchema, response_model_exclude_none=True)
async def create_post(create_data: CreatePost):
    await PostService.create(create_data)
    return ResponseSchema(detail="Successfully created data!")


@router.delete("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def get_by_id_post(post_id: int = Path(..., alias="id")):
    await PostService.delete(post_id)
    return ResponseSchema(detail="Successfully deleted data!")


@router.patch("/{id}", response_model=ResponseSchema, response_model_exclude_none=True)
async def update_person(post_id: int = Path(..., alias="id"), *, update_form: CreatePost):
    await PostService.update(post_id, update_form)
    return ResponseSchema(detail="Successfully updated data!")

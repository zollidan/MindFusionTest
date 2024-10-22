from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


@router.get('/users')
async def users_list():
    return ([{"users":"list"}, {"users":"list"}, {"users":"list"}, {"users":"list"}, ])
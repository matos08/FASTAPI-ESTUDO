from fastapi import APIRouter
from app.models.user_models import User
from app.services.user_service import create_user, get_user

# Este arquivo conterá a definição das rotas e manipuladores relacionados aos usuários da API.

router = APIRouter()


@router.post("/users/")
async def create_new_user(user: User):
    return create_user(user)


@router.get("/users/{user_id}")
async def read_user(user_id: int):
    return get_user(user_id)

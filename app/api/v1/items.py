from fastapi import APIRouter
from app.models.item_models import Item
from app.services.item_service import create_item, get_item

# Este arquivo conterá a definição das rotas e manipuladores relacionados aos itens da API.

router = APIRouter()


# criar dados
@router.post("/items/")
async def create_new_item(item: Item):
    return create_item(item)


# ler dados
@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return get_item(item_id)

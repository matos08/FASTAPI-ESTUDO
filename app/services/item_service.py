from app.models.item_models import Item


# Este arquivo conterá a lógica de negócios relacionada aos itens.

def create_item(item: Item):
    # Lógica para criar um item
    return {"message": "Item created successfully"}


def get_item(item_id: int):
    # Lógica para obter um item por ID
    return {"item_id": item_id, "name": "Sample Item"}

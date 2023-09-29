from pydantic import BaseModel


# Este arquivo conterá a definição do modelo de dados Pydantic para itens.
class Item(BaseModel):
    name: str
    description: str = None
    price: float

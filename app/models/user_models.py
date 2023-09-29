from pydantic import BaseModel


# Este arquivo conterá a definição do modelo de dados Pydantic para usuários.

class User(BaseModel):
    username: str
    email: str
    address: str

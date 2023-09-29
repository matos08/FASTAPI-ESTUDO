from fastapi import FastAPI
from app.api.v1 import items, users

# Este é o arquivo de entrada do aplicativo, onde você cria a instância do FastAPI e monta as rotas.

app = FastAPI()

app.include_router(items.router, prefix="/v1")
app.include_router(users.router, prefix="/v1")

from app.models.user_models import User


# Este arquivo conterá a lógica de negócios relacionada aos usuários.

def create_user(user: User):
    # Lógica para criar um usuário
    return {"message": "User created successfully"}


def get_user(user_id: int):
    # Lógica para obter um usuário por ID
    return {"user_id": user_id, "username": "sampleuser"}

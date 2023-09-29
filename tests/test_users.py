def test_create_user(client):
    response = client.post("/v1/users/", json={"username": "testuser", "email": "test@example.com"})
    assert response.status_code == 200
    assert response.json() == {"message": "User created successfully"}


def test_get_user(client):
    response = client.get("/v1/users/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1, "username": "sampleuser"}

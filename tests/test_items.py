def test_create_item(client):
    response = client.post("/v1/items/", json={"name": "Test Item"})
    assert response.status_code == 200
    assert response.json() == {"message": "Item created successfully"}


def test_get_item(client):
    response = client.get("/v1/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Sample Item"}

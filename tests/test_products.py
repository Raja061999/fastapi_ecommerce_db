from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_product():
    response = client.post("/products/", json={
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10
    })
    assert response.status_code == 200
    assert "id" in response.json()

def test_list_products():
    client.post("/products/", json={
        "name": "Test Product",
        "description": "Test Description",
        "price": 100.0,
        "quantity": 10
    })
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0
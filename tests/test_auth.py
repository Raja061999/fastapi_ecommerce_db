from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_signup():
    response = client.post("/auth/signup", json={"username": "testuser", "password": "password123"})
    assert response.status_code == 200
    assert "username" in response.json()

def test_login():
    client.post("/auth/signup", json={"username": "testuser", "password": "password123"})
    response = client.post("/auth/login", params={"username": "testuser", "password": "password123"})
    assert response.status_code == 200
    assert "access_token" in response.json()
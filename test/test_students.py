from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_student():
    # Get token first
    login_response = client.post("/auth/login", data={"username": "admin", "password": "secret"})
    token = login_response.json()["access_token"]
    
    response = client.post(
        "/students/",
        json={"name": "Alice", "age": 22, "email": "alice@example.com"},
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 201
    assert response.json()["email"] == "alice@example.com"
import os
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_image():
    file_path = "tests/test_image.jpg"
    with open(file_path, "rb") as image:
        response = client.post(
            "/images/upload",
            files={"file": ("test_image.jpg", image, "image/jpeg")}
        )
    assert response.status_code == 200
    assert "url" in response.json()


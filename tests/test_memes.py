import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import Meme
from app.schemas import MemeCreate

SQLALCHEMY_DATABASE_URL = "postgresql://sasha:123@db/memes"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_meme(test_db):
    response = client.post(
        "/memes/",
        json={"title": "Test Meme", "description": "This is a test meme", "image_url": "http://example.com/image.jpg"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Meme"

def test_read_memes(test_db):
    response = client.get("/memes/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_read_meme(test_db):
    response = client.get("/memes/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Meme"

def test_update_meme(test_db):
    response = client.put(
        "/memes/1",
        json={"title": "Updated Test Meme", "description": "Updated description"}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Meme"

def test_delete_meme(test_db):
    response = client.delete("/memes/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Meme"

import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["version"] == "0.1.0"


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_get_items_empty():
    """Test getting items when database is empty"""
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == []


def test_create_item():
    """Test creating a new item"""
    item_data = {
        "name": "Test Item",
        "description": "A test item",
        "price": 29.99,
        "is_available": True
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert data["id"] == 1


def test_get_item():
    """Test getting a specific item"""
    # First create an item
    item_data = {
        "name": "Test Item",
        "price": 29.99
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Then get the item
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["id"] == item_id


def test_get_item_not_found():
    """Test getting a non-existent item"""
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_update_item():
    """Test updating an item"""
    # First create an item
    item_data = {
        "name": "Original Item",
        "price": 29.99
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Then update the item
    update_data = {
        "name": "Updated Item",
        "price": 39.99
    }
    response = client.put(f"/items/{item_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == update_data["name"]
    assert data["price"] == update_data["price"]
    assert data["id"] == item_id


def test_update_item_not_found():
    """Test updating a non-existent item"""
    update_data = {
        "name": "Updated Item",
        "price": 39.99
    }
    response = client.put("/items/999", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_delete_item():
    """Test deleting an item"""
    # First create an item
    item_data = {
        "name": "Item to Delete",
        "price": 29.99
    }
    create_response = client.post("/items", json=item_data)
    item_id = create_response.json()["id"]
    
    # Then delete the item
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert "deleted successfully" in data["message"]
    
    # Verify the item is deleted
    get_response = client.get(f"/items/{item_id}")
    assert get_response.status_code == 404


def test_delete_item_not_found():
    """Test deleting a non-existent item"""
    response = client.delete("/items/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"


def test_create_item_minimal():
    """Test creating an item with minimal data"""
    item_data = {
        "name": "Minimal Item",
        "price": 19.99
    }
    response = client.post("/items", json=item_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == item_data["name"]
    assert data["price"] == item_data["price"]
    assert data["description"] is None
    assert data["is_available"] is True


def test_api_documentation_available():
    """Test that API documentation is available"""
    response = client.get("/docs")
    assert response.status_code == 200


def test_redoc_available():
    """Test that ReDoc documentation is available"""
    response = client.get("/redoc")
    assert response.status_code == 200 
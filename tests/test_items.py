#from fastapi.testclient import TestClient
#from main import app

#client = TestClient(app)

def test_create_product(client):
    product={
            "product_name": "keyboard",
            "category": "Electronics",
            "quantity": 10,
            "price": 1500.0
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 201

    data = response.json()

    assert data["product_id"] is not None
    assert data["product_name"] == product["product_name"]
    assert data["category"] == product["category"]
    assert data["quantity"] == product["quantity"]
    assert data["price"] == product["price"]

def test_read_product(client, product):
    product_id = product["product_id"]

    response = client.get(f"/products/{product_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["product_id"] == product_id

    assert all(
        field in data
        for field in ["product_name", "category","quantity", "price"]
    )

def test_read_all_products(client):
    response = client.get("/products/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for product in data:
        assert all(
            field in product
            for field in [
                "product_id",
                "product_name",
                "category",
                "quantity",
                "price"
            ]
        )

def test_update_product(client, product):
    product_id = product["product_id"]

    updated_product = {
        "product_name": "updated Keyboard",
        "category": "Electronics",
        "quantity": 20,
        "price": 1800.0
    }

    response = client.put(
        f"/products/{product_id}",
        json = updated_product
    )

    assert response.status_code == 200

    data = response.json()

    assert data["product_id"] == product_id
    assert data["product_name"] == updated_product["product_name"]
    assert data["category"] == updated_product["category"]
    assert data["quantity"] == updated_product["quantity"]
    assert data["price"] == updated_product["price"]

def test_delete_product(client, product):
    product_id = product["product_id"]

    response  = client.delete(f"/products/{product_id}")

    assert response.status_code == 204

    response = client.get(f"/products/{product_id}")

    assert response.status_code == 404

def test_search_existing_product(client, product):
    response = client.get(
        "/products/search",
        params = {"product_name": product["product_name"]}
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    for product in data:
        assert "keyboard" in product["product_name"].lower()

def test_search_unexisting_product(client):
    response = client.get(
        "/products/search",
        params = {"product_name": "NonexistentProductXYZ"}
    )

    assert response.status_code == 200
    assert response.json() == []

def test_read_nonexistent_product(client):
    response = client.get("/products/999999")

    assert response.status_code == 404

def test_update_nonexistent_product(client):
    updated_product = {
        "product_name": "Keyboard",
        "category": "Electronics",
        "quantity": 10,
        "price": 1500.0
    }

    response = client.put(
        "/products/999999",
        json=updated_product
    )

    assert response.status_code == 404

def test_delete_nonexistent_product(client):
    response = client.delete("/products/999999")

    assert response.status_code == 404

def test_create_product_negative_quantity(client):
    product = {
        "product_name": "Keyboard",
        "category": "Electronics",
        "quantity": -5,
        "price": 1500.0
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 422

def test_create_product_negative_price(client):
    product = {
        "product_name": "Mouse",
        "category": "Electronics",
        "quantity": 10,
        "price": -100.0
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 422

def test_create_product_missing_name(client):
    product = {
        "category": "Electronics",
        "quantity": 10,
        "price": 1500.0
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 422

def test_search_empty_product_name(client):
    response = client.get(
        "/products/search",
        params={"product_name": ""}
    )

    assert response.status_code == 422

def test_search_whitespace_product_name(client):
    response = client.get(
        "/products/search",
        params={"product_name": "   "}
    )

    assert response.status_code == 200

def test_create_product_zero_quantity(client):
    product = {
        "product_name": "Out of Stock Mouse",
        "category": "Electronics",
        "quantity": 0,
        "price": 500.0
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 201
    assert response.json()["quantity"] == 0

def test_create_product_zero_price(client):
    product = {
        "product_name": "Free Sample",
        "category": "Samples",
        "quantity": 5,
        "price": 0
    }

    response = client.post("/products/", json=product)

    assert response.status_code == 422

def test_create_duplicate_product_names(client, product):
    duplicate = {
        "product_name": product["product_name"],
        "category": "Electronics",
        "quantity": 5,
        "price": 500.0
    }

    response = client.post("/products/", json=duplicate)

    assert response.status_code == 201

def test_update_product_quantity_to_zero(client, product):
    update_data = {
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": 0,
        "price": product["price"]
    }

    response = client.put(
        f"/products/{product['product_id']}",
        json=update_data
    )

    assert response.status_code == 200
    assert response.json()["quantity"] == 0

def test_update_product_negative_quantity(client, product):
    update_data = {
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": -1,
        "price": product["price"]
    }

    response = client.put(
        f"/products/{product['product_id']}",
        json=update_data
    )

    assert response.status_code == 422

def test_update_product_zero_price(client, product):
    update_data = {
        "product_name": product["product_name"],
        "category": product["category"],
        "quantity": product["quantity"],
        "price": 0
    }

    response = client.put(
        f"/products/{product['product_id']}",
        json=update_data
    )

    assert response.status_code == 422

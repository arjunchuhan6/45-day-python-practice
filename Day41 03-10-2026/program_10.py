"""A small, clean FastAPI project with endpoint tests.

This example combines:

* GET, POST, PUT, and DELETE routes.
* Request validation for invalid data.
* API-key authentication for a protected route.
* Automated tests using FastAPI's TestClient.

Run the tests from the repository root with:

    py -m pytest "Day41 03-10-2026/program_10.py"

Start the API directly with:

    py "Day41 03-10-2026/program_10.py"

Then open http://127.0.0.1:8000/docs to view the interactive documentation.
"""

from typing import Annotated

from fastapi import Depends, FastAPI, Header, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel


EXPECTED_API_KEY = "project-test-key"


class ProductCreate(BaseModel):
    """Fields required when creating a product."""

    name: str
    price: float


class Product(ProductCreate):
    """Product returned by the API."""

    id: int


app = FastAPI(
    title="Product Management API",
    description="A small example project covering common API tests.",
    version="1.0.0",
)


products: dict[int, Product] = {
    1: Product(id=1, name="Notebook", price=4.99),
}


def verify_api_key(
    x_api_key: Annotated[str | None, Header()] = None,
) -> str:
    """Allow access only when the expected API key is provided."""

    if x_api_key != EXPECTED_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
        )

    return x_api_key


@app.get("/products/{product_id}", response_model=Product, tags=["Products"])
def get_product(product_id: int) -> Product:
    """Return one product by ID."""

    product = products.get(product_id)
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product


@app.post(
    "/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
    tags=["Products"],
)
def create_product(product_data: ProductCreate) -> Product:
    """Create and return a product."""

    product_id = max(products, default=0) + 1
    product = Product(id=product_id, **product_data.model_dump())
    products[product_id] = product
    return product


@app.put("/products/{product_id}", response_model=Product, tags=["Products"])
def update_product(product_id: int, product_data: ProductCreate) -> Product:
    """Update and return an existing product."""

    if product_id not in products:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    product = Product(id=product_id, **product_data.model_dump())
    products[product_id] = product
    return product


@app.delete("/products/{product_id}", tags=["Products"])
def delete_product(product_id: int) -> dict[str, int | str]:
    """Delete a product and return a confirmation message."""

    if products.pop(product_id, None) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return {"id": product_id, "message": "Product deleted successfully"}


@app.get(
    "/admin/products",
    dependencies=[Depends(verify_api_key)],
    tags=["Authentication"],
)
def list_products_for_admin() -> dict[str, list[Product]]:
    """Return all products for an authenticated request."""

    return {"products": list(products.values())}


client = TestClient(app)


def reset_products() -> None:
    """Restore the in-memory data before tests that change it."""

    products.clear()
    products[1] = Product(id=1, name="Notebook", price=4.99)


# GET test: retrieve the seeded product.
def test_get_product() -> None:
    """A valid GET request should return the requested product."""

    reset_products()
    response = client.get("/products/1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"id": 1, "name": "Notebook", "price": 4.99}


# POST test: create a new product.
def test_post_product() -> None:
    """A valid POST request should create a product."""

    reset_products()
    response = client.post(
        "/products",
        json={"name": "Pen", "price": 1.5},
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"id": 2, "name": "Pen", "price": 1.5}


# PUT test: update an existing product.
def test_put_product() -> None:
    """A valid PUT request should update the product."""

    reset_products()
    response = client.put(
        "/products/1",
        json={"name": "Large Notebook", "price": 7.5},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "name": "Large Notebook",
        "price": 7.5,
    }


# DELETE test: remove an existing product.
def test_delete_product() -> None:
    """A valid DELETE request should remove the product."""

    reset_products()
    response = client.delete("/products/1")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "message": "Product deleted successfully",
    }
    assert client.get("/products/1").status_code == status.HTTP_404_NOT_FOUND


# Invalid-data test: verify missing fields and incorrect types are rejected.
def test_invalid_product_data() -> None:
    """Invalid request data should return HTTP 422."""

    reset_products()
    missing_price = client.post("/products", json={"name": "Pen"})
    wrong_price_type = client.post(
        "/products",
        json={"name": "Pen", "price": "cheap"},
    )

    assert missing_price.status_code == 422
    assert wrong_price_type.status_code == 422


# Authentication test: verify that a missing API key is rejected.
def test_authentication_requires_api_key() -> None:
    """A protected route should reject a request without an API key."""

    response = client.get("/admin/products")

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Invalid or missing API key"}


# Authentication test: verify that the correct API key grants access.
def test_authentication_accepts_valid_api_key() -> None:
    """A protected route should accept the correct API key."""

    reset_products()
    response = client.get(
        "/admin/products",
        headers={"X-API-Key": EXPECTED_API_KEY},
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "products": [{"id": 1, "name": "Notebook", "price": 4.99}],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
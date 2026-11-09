"""Document a FastAPI endpoint and test its generated OpenAPI metadata.

Run this example from the repository root with:

    py -m pytest "Day41 03-10-2026/program_9.py"

FastAPI uses the route metadata to generate interactive documentation at
``/docs`` and an OpenAPI schema at ``/openapi.json``.
"""

from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel


class Product(BaseModel):
    """Response model shown in the generated API documentation."""

    id: int
    name: str
    price: float


app = FastAPI(
    title="Product API",
    description="A small API used to demonstrate endpoint documentation.",
    version="1.0.0",
)


@app.get(
    "/products/{product_id}",
    response_model=Product,
    summary="Get a product",
    description="Return product details for the requested product ID.",
    response_description="The requested product details.",
    tags=["Products"],
)
def get_product(product_id: int) -> Product:
    """Return an example product."""

    return Product(id=product_id, name="Notebook", price=4.99)


client = TestClient(app)


# Testing step 1: call the documented endpoint with a valid product ID.
def test_documented_endpoint() -> None:
    """The documented endpoint should return the product details."""

    response = client.get("/products/1")

    # Expected result: HTTP 200 and a response matching the Product model.
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Notebook",
        "price": 4.99,
    }


# Testing step 2: inspect the OpenAPI schema generated from route metadata.
def test_openapi_documents_endpoint() -> None:
    """The OpenAPI schema should contain the endpoint documentation."""

    response = client.get("/openapi.json")
    endpoint = response.json()["paths"]["/products/{product_id}"]["get"]

    # Expected result: summary, description, tag, and response docs are present.
    assert response.status_code == 200
    assert endpoint["summary"] == "Get a product"
    assert endpoint["description"] == (
        "Return product details for the requested product ID."
    )
    assert endpoint["tags"] == ["Products"]
    assert endpoint["responses"]["200"]["description"] == (
        "The requested product details."
    )


# Testing step 3: verify the interactive Swagger UI documentation is available.
def test_swagger_docs_is_available() -> None:
    """FastAPI should expose the interactive documentation page."""

    response = client.get("/docs")

    # Expected result: HTTP 200 and an HTML Swagger UI page.
    assert response.status_code == 200
    assert "Swagger UI" in response.text


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
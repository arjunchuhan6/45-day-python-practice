# program 8 write readme

This folder contains small examples for testing Python functions and FastAPI
routes. The examples are intentionally simple so that each testing idea is
easy to see.

## What is included?

| File | Topic |
|---|---|
| `program_1.py` | A basic FastAPI `GET` test |
| `program_2.py` | A simple test with Python's `unittest` |
| `program_3.py` | A FastAPI `POST` test |
| `program_4.py` | A FastAPI `PUT` test |
| `program_5.py` | A FastAPI `DELETE` test |
| `program_6.py` | Tests for invalid request data |
| `program_7.py` | API-key authentication tests |
| `program_9.py` | API endpoint documentation and OpenAPI tests |
| `program_10.py` | Complete product API project with all tests |

Every FastAPI example uses `TestClient`. This means the tests can call the
routes directly; a separate Uvicorn server is not needed while testing.

## Install the packages

Use Python 3.10 or newer. From the repository root, install the packages with:

```powershell
py -m pip install fastapi uvicorn pytest httpx
```

If `py` is not available on your computer, use `python` instead.

## How a FastAPI test works

The examples follow the same basic process:

1. Create a FastAPI application.
2. Add a route.
3. Create a `TestClient`.
4. Send a request with `client.get()`, `client.post()`, `client.put()`,
   or `client.delete()`.
5. Check the response status code.
6. Check the response JSON when necessary.

## Program details

### 1. GET - `program_1.py`

Route:

```text
GET /welcome
```

The test expects a `200 OK` response:

```json
{
  "message": "Arjun"
}
```

The FastAPI examples can also be started directly as small development
servers. Each one uses the same `if __name__ == "__main__":` entry point:

```powershell
py "Day41 03-10-2026/program_1.py"
```

For example, to start the documented API:

```powershell
py "Day41 03-10-2026/program_9.py"
```

Then open `http://127.0.0.1:8000/docs` in a browser. Stop the server with
`Ctrl+C`. Run the files with pytest when you want to execute their tests.

### 2. Unit testing - `program_2.py`

This file uses Python's built-in `unittest` module to test:

```python
add_numbers(2, 3)
```

The expected result is `5`.

Run it directly:

```powershell
py "Day41 03-10-2026/program_2.py"
```

It can also be run with pytest:

```powershell
py -m pytest "Day41 03-10-2026/program_2.py" -q
```

### 3. POST - `program_3.py`

Route:

```text
POST /users
```

Valid request:

```json
{
  "name": "Arjun"
}
```

The expected result is:

- Status: `201 Created`
- Body: `{"name": "Arjun"}`

The second test sends `{}`. Since `name` is required, FastAPI returns `422`.

### 4. PUT - `program_4.py`

Route:

```text
PUT /users/{user_id}
```

Example request:

```text
PUT /users/1
```

```json
{
  "name": "Arjun Updated"
}
```

The expected result is a `200 OK` response:

```json
{
  "id": 1,
  "name": "Arjun Updated"
}
```

The second test uses `/users/invalid`. Because `user_id` must be an integer,
FastAPI returns `422`.

### 5. DELETE - `program_5.py`

Route:

```text
DELETE /users/{user_id}
```

Example request:

```text
DELETE /users/1
```

Expected response:

```json
{
  "id": 1,
  "message": "User deleted successfully"
}
```

The response status is `200 OK`. A non-numeric ID is rejected with `422`.

### 6. Invalid data - `program_6.py`

This example checks that invalid input is rejected before the route runs.
The user model expects both a string `name` and an integer `age`.

| Request | Why it is invalid | Expected status |
|---|---|---:|
| `{"name": "Arjun"}` | `age` is missing | `422` |
| `{"name": "Arjun", "age": "twenty"}` | `age` is not an integer | `422` |
| `GET /users/invalid` | `user_id` is not an integer | `422` |

### 7. Authentication - `program_7.py`

Route:

```text
GET /protected
```

The route expects this header:

```text
X-API-Key: test-api-key
```

The tests cover all three common cases:

| Request | Expected result |
|---|---|
| Correct API key | `200 OK` and an authenticated message |
| No API key | `401 Unauthorized` |
| Wrong API key | `401 Unauthorized` |

`test-api-key` is only an example value for learning. A real application
should keep credentials outside the source code and use a secure secret
management system.

### 8. API documentation - `program_9.py`

This example shows how FastAPI documents an endpoint automatically. The
`GET /products/{product_id}` route includes a summary, description, response
description, response model, and `Products` tag.

FastAPI makes the documentation available at:

- `http://127.0.0.1:8000/docs` for the interactive Swagger UI.
- `http://127.0.0.1:8000/redoc` for ReDoc.
- `http://127.0.0.1:8000/openapi.json` for the generated OpenAPI schema.

The tests check the endpoint response, the OpenAPI metadata, and the
availability of the Swagger UI page.

### 9. Complete project - `program_10.py`

This file brings the main ideas together in one small Product Management API.
It uses an in-memory dictionary, so it is easy to run and understand without
setting up a database.

Available routes:

| Method | Route | Purpose | Authentication |
|---|---|---|---|
| `GET` | `/products/{product_id}` | Get one product | No |
| `POST` | `/products` | Create a product | No |
| `PUT` | `/products/{product_id}` | Update a product | No |
| `DELETE` | `/products/{product_id}` | Delete a product | No |
| `GET` | `/admin/products` | List all products | `X-API-Key` |

The file tests successful GET, POST, PUT, and DELETE requests, invalid product
data, missing authentication, and valid authentication. Start it with:

```powershell
py "Day41 03-10-2026/program_10.py"
```

Then visit `http://127.0.0.1:8000/docs`.

## Run the tests

Run one file:

```powershell
py -m pytest "Day41 03-10-2026/program_7.py" -q
```

Run the complete project:

```powershell
py -m pytest "Day41 03-10-2026/program_10.py" -q
```

Run all eight completed files:

```powershell
py -m pytest `
  "Day41 03-10-2026/program_1.py" `
  "Day41 03-10-2026/program_2.py" `
  "Day41 03-10-2026/program_3.py" `
  "Day41 03-10-2026/program_4.py" `
  "Day41 03-10-2026/program_5.py" `
  "Day41 03-10-2026/program_6.py" `
  "Day41 03-10-2026/program_7.py" `
  "Day41 03-10-2026/program_9.py" -q
```

There are 17 tests in total:

- 1 in `program_1.py`
- 1 in `program_2.py`
- 2 in `program_3.py`
- 2 in `program_4.py`
- 2 in `program_5.py`
- 3 in `program_6.py`
- 3 in `program_7.py`
- 3 in `program_9.py`

## Why the folder command may find no tests

The files use names such as `program_3.py`, while pytest normally looks for
files named `test_*.py` or `*_test.py`. For that reason, run the files
explicitly as shown above instead of running only:

```powershell
py -m pytest "Day41 03-10-2026"
```

## Final checklist

Before adding another endpoint, make sure:

- The route and HTTP method are written down.
- A normal request is tested.
- The success status code is checked.
- The response body is checked where appropriate.
- Missing or incorrectly typed data is tested.
- Authentication is tested for protected routes.
- The test comments explain the step and expected result.
- The focused pytest command passes.

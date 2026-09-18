"""FastAPI example using a path parameter and an optional query parameter."""

import fastapi

app = fastapi.FastAPI()

students = {
    1: {
        "student_id": 1,
        "name": "Aarav",
        "course": "Python",
        "email": "aarav@example.com",
    },
    2: {
        "student_id": 2,
        "name": "Diya",
        "course": "FastAPI",
        "email": "diya@example.com",
    },
}


@app.get("/student/{student_id}")
def get_student(student_id: int, details: bool = False):
    """Return a student using the ID in the URL and optional details query parameter."""
    student = students.get(student_id)

    if student is None:
        raise fastapi.HTTPException(status_code=404, detail="Student not found")

    if details:
        return student

    return {"student_id": student["student_id"], "name": student["name"]}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

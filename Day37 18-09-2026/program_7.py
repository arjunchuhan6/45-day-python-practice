# filter students
import fastapi
import uvicorn
students = [
    {"student_id": 1, "name": "Aarav", "course": "Python"},
    {"student_id": 2, "name": "Diya", "course": "FastAPI"},
    {"student_id": 3, "name": "Kabir", "course": "Python"},
    {"student_id": 4, "name": "Anaya", "course": "Django"}
]

app = fastapi.FastAPI()
@app.get("/filter")
def filter_students(name: str | None = None, course: str | None = None):
    """Filter students by name or course."""
    selected_students = students

    if name is not None:
        name = name.strip()
        selected_students = [
            student
            for student in selected_students
            if name.lower() in student["name"].lower()
        ]

    if course is not None:
        course = course.strip()
        selected_students = [
            student
            for student in selected_students
            if course.lower() in student["course"].lower()
        ]

    return {"count": len(selected_students), "students": selected_students}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
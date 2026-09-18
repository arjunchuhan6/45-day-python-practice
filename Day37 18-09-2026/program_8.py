#add student details to the list
import fastapi
import uvicorn

app = fastapi.FastAPI()

students = [
    {"student_id": 1, "name": "Aarav", "course": "Python"},
    {"student_id": 2, "name": "Diya", "course": "FastAPI"},
    {"student_id": 3, "name": "Kabir", "course": "Python"},
    {"student_id": 4, "name": "Anaya", "course": "Django"}
]

@app.post("/add")
def add_student(student: dict):
    """Add a new student to the list."""
    if not isinstance(student, dict) or "student_id" not in student or "name" not in student or "course" not in student:
        raise fastapi.HTTPException(status_code=400, detail="Invalid student data")

    # Check for duplicate student_id
    if any(s["student_id"] == student["student_id"] for s in students):
        raise fastapi.HTTPException(status_code=402, detail="Student ID already exists")

    students.append(student)
    return {"message": "Student added successfully", "student": student}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
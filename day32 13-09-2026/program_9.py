#create a database class for sqlite database using python only create data
import sqlite3
from typing import Any
class Database:
    def __init__(self, db_name: str) -> None:
        self.connection: sqlite3.Connection = sqlite3.connect(db_name)
        self.cursor: sqlite3.Cursor = self.connection.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            grade TEXT NOT NULL)''')
        self.connection.commit()
        print("Table created successfully.")

    def insert_data(self, name: str, age: int, grade: str) -> None:
        self.cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
        self.connection.commit()
        print("Data inserted successfully.")

    def search_data(self, name: str) -> None:
        self.cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        result: list[Any] = self.cursor.fetchall()
        print("Search results:", result)

    def close_connection(self) -> None:
        self.cursor.close()
        self.connection.close()


if __name__ == "__main__":
    database = Database("students.db")
    try:
        student_name: str = input("Enter student name: ")
        student_age = int(input("Enter student age: "))
        student_grade: str = input("Enter student grade: ")

        database.insert_data(student_name, student_age, student_grade)
        database.search_data(student_name)
    finally:
        database.close_connection()
        
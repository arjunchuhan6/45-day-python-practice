#delete data from sqlite database using python only delete data
import sqlite3
connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()
# Delete data from the students table where age is greater than 20
cursor.execute("DELETE FROM students WHERE id =  '1'")
connection.commit()
print("Data deleted successfully.")
connection.close()
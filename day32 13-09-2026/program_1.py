#create sqlite database using python only create data 
import sqlite3
connection: sqlite3.Connection = sqlite3.connect("students.db")
cursor: sqlite3.Cursor = connection.cursor()
connection.close()
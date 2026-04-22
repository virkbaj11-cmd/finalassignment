# Program to perform CRUD operations in SQLite

import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table (if not exists)
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")

# INSERT operation
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Alice", 20, "A"))
cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
               ("Bob", 22, "B"))
print("Data inserted successfully.")

# UPDATE operation
cursor.execute("UPDATE students SET age = ? WHERE name = ?", (21, "Alice"))
print("Data updated successfully.")

# DELETE operation
cursor.execute("DELETE FROM students WHERE name = ?", ("Bob",))
print("Data deleted successfully.")

# SELECT operation
print("\nStudent Records:")
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Commit and close
conn.commit()
conn.close()

# Program to connect to a database and create a table

import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect("student.db")

# Create a cursor object
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade TEXT
)
""")

print("Table created successfully.")

# Commit changes and close connection
conn.commit()
conn.close()

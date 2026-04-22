# Program to demonstrate commit and rollback

import sqlite3

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    balance INTEGER
)
""")

# Insert sample data
cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Alice", 1000))
cursor.execute("INSERT INTO accounts (name, balance) VALUES (?, ?)", ("Bob", 1000))
conn.commit()

print("Initial data inserted.\n")

try:
    # Start transaction: Transfer 200 from Alice to Bob
    cursor.execute("UPDATE accounts SET balance = balance - 200 WHERE name = ?", ("Alice",))
    
    # Simulate an error
    x = 1 / 0   # This will cause an error
    
    cursor.execute("UPDATE accounts SET balance = balance + 200 WHERE name = ?", ("Bob",))
    
    # Commit if everything is successful
    conn.commit()
    print("Transaction committed.")

except Exception as e:
    # Rollback in case of error
    conn.rollback()
    print("Transaction failed. Rolled back.")
    print("Error:", e)

# Display final data
print("\nFinal account balances:")
cursor.execute("SELECT * FROM accounts")
for row in cursor.fetchall():
    print(row)

# Close connection
conn.close()

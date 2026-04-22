# Program to demonstrate dictionary operations

# Creating a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}

print("Original dictionary:", student)

# Adding a new key-value pair
student["city"] = "Delhi"
print("\nAfter adding (city):", student)

# Updating an existing value
student["age"] = 21
print("After updating (age):", student)

# Deleting a key-value pair using del
del student["grade"]
print("After deleting (grade):", student)

# Deleting using pop()
removed = student.pop("city")
print("After pop (city):", student)
print("Removed value:", removed)

# Program to demonstrate built-in functions

# List operations
numbers = [5, 2, 9, 1, 7]
print("List:", numbers)
print("Length of list:", len(numbers))
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))
print("Sum of elements:", sum(numbers))
print("Sorted list:", sorted(numbers))

# String operations
text = "Python Programming"
print("\nString:", text)
print("Length of string:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Count of 'o':", text.count('o'))
print("Reversed string:", text[::-1])

# Dictionary operations
student = {"name": "Alice", "age": 20, "marks": 85}
print("\nDictionary:", student)
print("Length of dictionary:", len(student))
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

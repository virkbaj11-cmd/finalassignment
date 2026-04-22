# Program to demonstrate list slicing and manipulation

# Creating a list
numbers = [10, 20, 30, 40, 50, 60]

print("Original list:", numbers)

# List Slicing
print("\nSlicing Operations:")
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Middle elements:", numbers[1:5])
print("Reversed list:", numbers[::-1])

# List Manipulation
print("\nList Manipulation:")

# Append
numbers.append(70)
print("After append:", numbers)

# Insert
numbers.insert(2, 25)
print("After insert at index 2:", numbers)

# Remove
numbers.remove(40)
print("After removing 40:", numbers)

# Pop
numbers.pop()
print("After pop (last element removed):", numbers)

# Update value
numbers[1] = 15
print("After updating index 1:", numbers)

# Sort
numbers.sort()
print("After sorting:", numbers)

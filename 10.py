# Program to demonstrate string operations

# Taking input from user
text = input("Enter a string: ")

# Slicing
print("\nSlicing Operations:")
print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Middle part:", text[1:-1])

# Concatenation
str2 = input("\nEnter another string: ")
concatenated = text + " " + str2
print("Concatenated string:", concatenated)

# Reversing the string
reversed_text = text[::-1]
print("\nReversed string:", reversed_text)

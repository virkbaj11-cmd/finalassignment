# Demonstration of numeric data types and type conversion

# Integer data type
a = 10
print("Value of a:", a)
print("Type of a:", type(a))

# Float data type
b = 5.75
print("\nValue of b:", b)
print("Type of b:", type(b))

# Type conversion: int to float
c = float(a)
print("\nAfter converting a to float:")
print("Value of c:", c)
print("Type of c:", type(c))

# Type conversion: float to int
d = int(b)
print("\nAfter converting b to int:")
print("Value of d:", d)
print("Type of d:", type(d))

# Taking user input and converting types
x = int(input("\nEnter an integer: "))
y = float(input("Enter a float: "))

print("\nYou entered:")
print("Integer:", x, "Type:", type(x))
print("Float:", y, "Type:", type(y))

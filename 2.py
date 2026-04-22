# Program to perform arithmetic operations

# Taking input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division safely
if num2 != 0:
    division = num1 / num2
    floor_division = num1 // num2
    modulus = num1 % num2
else:
    division = "Undefined (division by zero)"
    floor_division = "Undefined"
    modulus = "Undefined"

# Output results
print("\nResults:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)

# Exponentiation
power = num1 ** num2
print("Exponentiation (num1 ** num2):", power)

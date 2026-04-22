# Demonstration of variable assignment and swapping

# Variable assignment
a = 5
b = 10

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping using temporary variable:")
print("a =", a)
print("b =", b)

# Swapping without using a temporary variable
a, b = b, a

print("\nAfter swapping without temporary variable:")
print("a =", a)
print("b =", b)

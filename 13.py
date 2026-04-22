# Program to demonstrate tuple operations and immutability

# Creating a tuple
t = (10, 20, 30, 40, 50)

print("Original tuple:", t)

# Accessing elements
print("\nFirst element:", t[0])
print("Last element:", t[-1])

# Slicing
print("\nSliced tuple (1 to 3):", t[1:4])

# Tuple operations
print("\nLength of tuple:", len(t))
print("Count of 20:", t.count(20))
print("Index of 30:", t.index(30))

# Concatenation
t2 = (60, 70)
t3 = t + t2
print("\nAfter concatenation:", t3)

# Demonstrating immutability
print("\nTrying to modify tuple...")
try:
    t[0] = 100   # This will cause an error
except TypeError as e:
    print("Error:", e)

print("\nTuple remains unchanged:", t)

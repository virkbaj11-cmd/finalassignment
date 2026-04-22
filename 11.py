# Program to count frequency of characters in a string

# Taking input from user
text = input("Enter a string: ")

# Dictionary to store frequency
freq = {}

# Counting frequency
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Display result
print("\nCharacter frequencies:")
for key, value in freq.items():
    print(key, ":", value)

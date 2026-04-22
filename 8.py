# Program to find sum of first N natural numbers

# Taking input from user
n = int(input("Enter a positive integer: "))

# Initialize variables
sum = 0
i = 1

# Using while loop
while i <= n:
    sum += i
    i += 1

# Display result
print("Sum of first", n, "natural numbers is:", sum)

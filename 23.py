# Program to read file contents in different ways

# Open the file
file = open("sample.txt", "r")

# Using read()
print("Using read():")
content = file.read()
print(content)

# Move file pointer to beginning
file.seek(0)

# Using readline()
print("\nUsing readline():")
line1 = file.readline()
line2 = file.readline()
print("First line:", line1, end="")
print("Second line:", line2, end="")

# Move file pointer to beginning again
file.seek(0)

# Using readlines()
print("\n\nUsing readlines():")
lines = file.readlines()
for line in lines:
    print(line, end="")

# Close the file
file.close()

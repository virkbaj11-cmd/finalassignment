# Program to write and append data to a file

# Writing to a file (overwrites if file already exists)
with open("sample.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This file is created using write mode.\n")

print("Data written to file.")

# Appending to the same file
with open("sample.txt", "a") as file:
    file.write("This line is added later using append mode.\n")

print("Data appended to file.")

# Reading the file to display contents
with open("sample.txt", "r") as file:
    print("\nFile contents:")
    print(file.read())

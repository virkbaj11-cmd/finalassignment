# Program to copy contents of one file to another

# Open source file in read mode
with open("source.txt", "r") as source:
    content = source.read()

# Open destination file in write mode
with open("destination.txt", "w") as destination:
    destination.write(content)

print("File copied successfully.")

# Optional: Display contents of destination file
with open("destination.txt", "r") as file:
    print("\nContents of destination file:")
    print(file.read())

# Program to demonstrate seek() function

# Create and write to a file
with open("sample.txt", "w") as file:
    file.write("Hello World!\nWelcome to Python file handling.")

# Open file in read mode
with open("sample.txt", "r") as file:
    
    # Read first 5 characters
    print("Reading first 5 characters:")
    print(file.read(5))
    
    # Move pointer to beginning
    file.seek(0)
    print("\nAfter seek(0):")
    print(file.read(5))
    
    # Move pointer to 6th position
    file.seek(6)
    print("\nAfter seek(6):")
    print(file.read(5))
    
    # Move pointer to end and try reading
    file.seek(0, 2)  # 2 means end of file
    print("\nAfter seek to end:")
    print(file.read())  # Nothing will be read

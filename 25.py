# Program to demonstrate multiple exception handling

try:
    # Taking input from user
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    # Perform division
    result = a / b

    # Accessing list element
    lst = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print("Element at index:", lst[index])

    print("Division result:", result)

# Handling multiple exceptions
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter integers only.")

except IndexError:
    print("Error: Index out of range.")

except Exception as e:
    print("Unexpected error:", e)

else:
    print("All operations completed successfully.")

finally:
    print("Program execution finished.")

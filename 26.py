# Program using finally and custom exception

# Define a custom exception
class NegativeNumberError(Exception):
    pass

try:
    # Taking input
    num = int(input("Enter a positive number: "))

    # Raise custom exception if number is negative
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    result = 100 / num
    print("Result:", result)

except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Enter an integer.")

finally:
    print("This block always executes.")

print("Program ended.")

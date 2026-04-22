# Program to demonstrate exception handling

try:
    # Taking input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Performing division
    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter numbers only.")

except Exception as e:
    print("An unexpected error occurred:", e)

else:
    print("Division successful.")

finally:
    print("Program execution completed.")

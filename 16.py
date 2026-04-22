# Functions for string operations
def string_operations(text):
    print("\nString Operations:")
    print("Original string:", text)
    print("Length:", len(text))
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Reversed:", text[::-1])


# Functions for list operations
def list_operations(lst):
    print("\nList Operations:")
    print("Original list:", lst)
    print("Length:", len(lst))
    print("Maximum value:", max(lst))
    print("Minimum value:", min(lst))
    print("Sorted list:", sorted(lst))


# Main program
# String input
text = input("Enter a string: ")
string_operations(text)

# List input
lst = list(map(int, input("\nEnter list elements separated by space: ").split()))
list_operations(lst)

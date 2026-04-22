# Demonstration of break, continue, and pass

print("Using break:")
for i in range(1, 11):
    if i == 6:
        break   # exits the loop when i is 6
    print(i)

print("\nUsing continue:")
for i in range(1, 11):
    if i == 6:
        continue   # skips the iteration when i is 6
    print(i)

print("\nUsing pass:")
for i in range(1, 6):
    if i == 3:
        pass   # does nothing, acts as a placeholder
    print(i)

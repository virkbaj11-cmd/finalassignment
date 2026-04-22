# Program to plot line and bar graphs using matplotlib

import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Line Graph
plt.figure()
plt.plot(x, y, marker='o')
plt.title("Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Graph
plt.figure()
plt.bar(x, y)
plt.title("Bar Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

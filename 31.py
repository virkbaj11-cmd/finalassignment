# Program combining NumPy, Pandas, and Matplotlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create data using NumPy
data = {
    "Days": np.arange(1, 8),
    "Sales": np.array([200, 250, 300, 280, 350, 400, 420])
}

# Step 2: Create DataFrame using Pandas
df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Step 3: Basic Analysis
print("\nSummary Statistics:")
print(df.describe())

print("\nTotal Sales:", np.sum(df["Sales"]))
print("Average Sales:", np.mean(df["Sales"]))

# Step 4: Plot using Matplotlib

# Line Graph
plt.figure()
plt.plot(df["Days"], df["Sales"], marker='o')
plt.title("Sales Trend")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

# Bar Graph
plt.figure()
plt.bar(df["Days"], df["Sales"])
plt.title("Sales per Day")
plt.xlabel("Days")
plt.ylabel("Sales")
plt.show()

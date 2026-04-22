# Program to filter and group data using pandas

import pandas as pd

# Sample data (you can also read from CSV)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "IT", "IT", "HR", "Finance"],
    "Salary": [40000, 50000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Filtering data (Salary > 45000)
filtered_data = df[df["Salary"] > 45000]
print("\nFiltered Data (Salary > 45000):")
print(filtered_data)

# Grouping data by Department and calculating average salary
grouped_data = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary by Department:")
print(grouped_data)

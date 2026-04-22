# Program to read CSV file and perform basic analysis

import pandas as pd

# Read CSV file
df = pd.read_csv("data.csv")

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Display basic information
print("\nDataset Info:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display number of rows and columns
print("\nShape of dataset (rows, columns):")
print(df.shape)

# Example: selecting a column (replace 'column_name' with actual column)
# print("\nColumn data:")
# print(df['column_name'])

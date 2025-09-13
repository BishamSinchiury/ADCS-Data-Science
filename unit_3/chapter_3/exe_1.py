# ------------------------------------------------------
# Data Formatting in Python - Full Exercise
# ------------------------------------------------------

# Import required library
import pandas as pd   # pandas is used for data manipulation and analysis
import numpy as np    # numpy is used for numerical operations

# ------------------------------------------------------
# 1. Create a Sample Dataset
# ------------------------------------------------------
# We use a dictionary to simulate raw, messy data
# Keys = column names, Values = lists of data for each column
data = {
    'ID': ['001', '002', '003', '004'],                 # Employee IDs as strings
    'Name': [' alice ', 'BOB', 'ChArLie ', 'david'],    # Names with inconsistent formatting
    'Birthdate': ['2001-05-21', '22-06-2000', 'July 5, 1999', '1998/08/30'],  # Mixed date formats
    'Salary': ['1000.50', '2000', '3,000.75', '4000.00'], # Salaries with commas & strings
    'Joining_Year': [2020, '2021', 2022, '2023']        # Mixed integers and strings
}

# Convert dictionary into a DataFrame
df = pd.DataFrame(data)  
# DataFrame is a tabular data structure with rows and columns
print("Original Data:\n", df)

# ------------------------------------------------------
# 2. Changing Data Types
# ------------------------------------------------------
# Converting 'ID' column to integer type
# .astype(int) converts the column values from string to integer
df['ID'] = df['ID'].astype(int)

# Converting 'Joining_Year' column to integer type
# Handles the mix of integers and strings
df['Joining_Year'] = df['Joining_Year'].astype(int)

# ------------------------------------------------------
# 3. Date & Time Formatting
# ------------------------------------------------------
# Converting 'Birthdate' column into datetime format
# pd.to_datetime() automatically detects multiple formats
# errors='coerce' → If a value cannot be converted, it is replaced with NaT (Not a Time)
df['Birthdate'] = pd.to_datetime(df['Birthdate'], errors='coerce')

# ------------------------------------------------------
# 4. String Formatting
# ------------------------------------------------------
# Standardizing 'Name' column
# .str.strip() → removes leading and trailing spaces
# .str.title() → converts each word to Title Case (e.g., "alice" → "Alice")
df['Name'] = df['Name'].str.strip().str.title()

# ------------------------------------------------------
# 5. Numeric Formatting
# ------------------------------------------------------
# Cleaning 'Salary' column
# .str.replace(',', '') → removes commas
# .astype(float) → converts the values to floating-point numbers
df['Salary'] = df['Salary'].str.replace(',', '').astype(float)

# Rounding salary values to 2 decimal places
# .round(2) → keeps only two digits after the decimal point
df['Salary'] = df['Salary'].round(2)

# ------------------------------------------------------
# 6. Renaming Columns
# ------------------------------------------------------
# df.rename() is used to rename column names
# columns={'OldName':'NewName'} specifies mapping of names
# inplace=True → modifies the DataFrame directly instead of returning a copy
df.rename(columns={'ID': 'Employee_ID', 'Name': 'Employee_Name'}, inplace=True)

# ------------------------------------------------------
# 7. Final Output
# ------------------------------------------------------
print("\nFormatted Data:\n", df)

# ------------------------------------------------------
# 8. Demonstrating Results
# ------------------------------------------------------
# Example: Extracting year from Birthdate
# .dt.year accesses the year component of datetime objects
df['Birth_Year'] = df['Birthdate'].dt.year

print("\nData with Birth Year Extracted:\n", df)

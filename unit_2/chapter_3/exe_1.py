# 1️⃣ Check Size and Shape
# Function: data.shape
#     Purpose: Returns the number of rows and columns in the DataFrame.
#     Code Example:

import pandas as pd

data = pd.read_csv("./data/sample.csv")
print("Shape of the dataset:", data.shape)
print("""
    Explanation:
        The dataset has 5 rows (records) and 5 columns (features). 
        This helps quickly understand dataset size.
    """)
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

# 2️⃣ Preview Data
# Functions: data.head() and data.tail()
#     Purpose: Show first or last few rows of the dataset for a quick check.
#     Code Example:

print("First 5 rows:\n", data.head())  # Default shows first 5 rows
print("Last 3 rows:\n", data.tail(3))  # Shows last 3 rows

print("""
    Explanation:
        Previewing lets you verify the data loaded correctly and check for obvious issues (e.g., missing values or typos).
    """)

# ----------------------------------------------------------------------
# ----------------------------------------------------------------------

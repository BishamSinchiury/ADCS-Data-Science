# ------------------------------------------
# Dealing with Missing Values in Python
# ------------------------------------------

import pandas as pd
import numpy as np

# 1. Create a sample dataset with missing values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, np.nan, 30, None, 40],         # Missing ages
    'Score': [85, 90, np.nan, 95, None],       # Missing scores
    'City': ['NY', None, 'LA', 'SF', None]     # Missing categorical values
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# ------------------------------------------------------
# 2. Removing Missing Values
# ------------------------------------------------------
# Drop any row with missing values
df_drop_rows = df.dropna()
print("\nAfter Removing Rows with Missing Values:\n", df_drop_rows)

# Drop any column with missing values
df_drop_cols = df.dropna(axis=1)
print("\nAfter Removing Columns with Missing Values:\n", df_drop_cols)

# ------------------------------------------------------
# 3. Filling Missing Values with a Constant
# ------------------------------------------------------
# Fill NaN in Age with 0, Score with -1, City with "Unknown"
df_fill_const = df.fillna({'Age': 0, 'Score': -1, 'City': 'Unknown'})
print("\nAfter Filling with Constant Values:\n", df_fill_const)

# ------------------------------------------------------
# 4. Filling with Summary Statistics
# ------------------------------------------------------
df_stat = df.copy()

# Fill Age with mean
df_stat['Age'] = df_stat['Age'].fillna(df_stat['Age'].mean())

# Fill Score with median
df_stat['Score'] = df_stat['Score'].fillna(df_stat['Score'].median())

# Fill City with mode (most frequent value)
df_stat['City'] = df_stat['City'].fillna(df_stat['City'].mode()[0])

print("\nAfter Filling with Summary Statistics:\n", df_stat)

# ------------------------------------------------------
# 5. Forward Fill & Backward Fill
# ------------------------------------------------------
# Forward Fill (use previous value to fill missing)
df_ffill = df.fillna(method='ffill')
print("\nAfter Forward Fill:\n", df_ffill)

# Backward Fill (use next value to fill missing)
df_bfill = df.fillna(method='bfill')
print("\nAfter Backward Fill:\n", df_bfill)

# ------------------------------------------------------
# 6. Interpolation
# ------------------------------------------------------
# Interpolation estimates missing numeric values mathematically
df_interp = df.copy()
df_interp['Age'] = df_interp['Age'].interpolate()
df_interp['Score'] = df_interp['Score'].interpolate()

print("\nAfter Interpolation:\n", df_interp)

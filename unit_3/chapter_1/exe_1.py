# Simple Data Pre-processing Exercise

# Import libraries
import pandas as pd  
# For data manipulation and creating DataFrames
import numpy as np   
# For numerical operations, handling NaN, and arrays
from sklearn.preprocessing import LabelEncoder, StandardScaler  
# For encoding categorical variables and feature scaling
from sklearn.model_selection import train_test_split  
# For splitting dataset into training and testing sets

# 1. Create a sample dataset
# Dictionary with sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Alice'],  # Names of individuals (categorical)
    'Age': [14, 15, np.nan, 16, 14],                        # Age with one missing value (np.nan represents missing)
    'Grade': ['8th', '9th', '10th', np.nan, '8th'],        # Grade with one missing value
    'Score': [85, 90, 95, 1000, 85]                        # Score with an outlier (1000)
}

# Convert dictionary to pandas DataFrame
df = pd.DataFrame(data)  # pd.DataFrame(data) creates a tabular structure with rows and columns
print("Original Data:\n", df)

# 2. Handle missing data
# Fill missing Age values with the mean of Age column
# Arguments:
#   value: What to fill NaN with (here we use df['Age'].mean())
# Instead of inplace=True on a slice (which causes warnings), we reassign directly
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Grade values with a default value 'Unknown'
df['Grade'] = df['Grade'].fillna('Unknown')

# 3. Remove duplicates
# drop_duplicates removes repeated rows from the DataFrame
# Arguments:
#   inplace=True modifies the original DataFrame
df.drop_duplicates(inplace=True)

# 4. Encode categorical variables
# LabelEncoder converts categorical labels into numeric form
# Useful because ML algorithms require numeric input
encoder = LabelEncoder()            # Initialize LabelEncoder object
df['Grade'] = encoder.fit_transform(df['Grade'])  
# fit_transform() both learns the mapping and applies it:
#   '8th' -> 0, '9th' -> 1, '10th' -> 2, 'Unknown' -> 3 (example mapping)

# 5. Handle outliers (capping Score at 100)
# np.where(condition, value_if_true, value_if_false)
# Replaces values in Score column greater than 100 with 100
df['Score'] = np.where(df['Score'] > 100, 100, df['Score'])

# 6. Feature scaling (Age and Score)
# StandardScaler standardizes features by removing mean and scaling to unit variance
# fit_transform() computes mean & std from the data and applies scaling
scaler = StandardScaler()
df[['Age', 'Score']] = scaler.fit_transform(df[['Age', 'Score']])
# After scaling:
#   - Mean of each column ≈ 0
#   - Standard deviation ≈ 1

# 7. Split dataset into training and testing
# Select features (X) and target (y)
X = df[['Age', 'Grade', 'Score']]  # Feature columns

# Create a target variable (y) of the same length as df
# Here we just create example labels for demonstration
y = [0, 1, 0, 1]  # Length = 4 to match the DataFrame after drop_duplicates

# train_test_split splits arrays or DataFrames into random train and test subsets
# Arguments:
#   test_size=0.33 -> 33% data for testing
#   random_state=42 -> ensures reproducible split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Display processed data
print("\nProcessed Data:\n", df)
print("\nTraining Set:\n", X_train)
print("\nTest Set:\n", X_test)

# -------------------------------
# Practical Example: Importing & Exporting Data
# -------------------------------

# 1️⃣ CSV Files using pandas
import pandas as pd  
# Import pandas library for data manipulation and analysis

# Import CSV
csv_data = pd.read_csv("data/employee.csv")  
# Read CSV file located at "data/employee.csv" into a DataFrame
print("CSV Imported:\n", csv_data.head())  
# Display the first 5 rows of the imported CSV for verification

# Export CSV
csv_data.to_csv("output/employee_export.csv", index=False)  
# Save the DataFrame to CSV without including the row index
print("CSV Exported!")  
# Confirmation message

# -------------------------------

# 2️⃣ Excel Files using pandas
# Import Excel
excel_data = pd.read_excel("data/employee.xlsx", sheet_name="Sheet1")  
# Read Excel file and specify the sheet name
print("Excel Imported:\n", excel_data.head())  
# Display the first 5 rows to verify data

# Export Excel
excel_data.to_excel("output/employee_export.xlsx", sheet_name="Sheet1", index=False)  
# Save DataFrame to Excel sheet without row index
print("Excel Exported!")  
# Confirmation message

# -------------------------------

# 3️⃣ JSON Files using pandas
# Import JSON
json_data = pd.read_json("data/employee.json")  
# Read JSON file into a DataFrame
print("JSON Imported:\n", json_data.head())  
# Display the first 5 rows

# Export JSON
json_data.to_json("output/employee_export.json", orient="records")  
# Export DataFrame to JSON in "records" format (list of dictionaries)
print("JSON Exported!")  
# Confirmation message

# -------------------------------

# 4️⃣ JSON Files using json module (built-in)
import json  
# Import built-in JSON module for working with JSON files

# Import JSON
with open("data/employee.json", "r") as f:  
    # Open JSON file in read mode
    settings = json.load(f)  # Parse JSON data from file into a Python dictionary
print("JSON (built-in) Imported:\n", settings)  # Print imported JSON dictionary

# Export JSON
with open("output/employee_export.json", "w") as f:  
    # Open JSON file in write mode
    json.dump(settings, f, indent=4)  # Write Python dictionary to JSON file with indentation
print("JSON (built-in) Exported!")  # Confirmation message

# -------------------------------

# 5️⃣ Database (SQLite) using sqlite3
import sqlite3  # Import sqlite3 module for database operations

# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("data/employee.db")
cursor = conn.cursor()

# 1️⃣ Create the 'employees' table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Department TEXT,
    Position TEXT,
    DateOfJoining TEXT,
    Salary REAL,
    Email TEXT,
    Phone TEXT
)
""")

# 2️⃣ Optional: Insert sample data if table is empty
cursor.execute("SELECT COUNT(*) FROM employees")
if cursor.fetchone()[0] == 0:
    sample_employees = [
        (1001, "John", "Doe", "Engineering", "Software Engineer", "2021-06-15", 75000, "john.doe@example.com", "555-1234"),
        (1002, "Jane", "Smith", "Marketing", "Marketing Manager", "2020-03-22", 68000, "jane.smith@example.com", "555-5678"),
        (1003, "Michael", "Brown", "HR", "HR Specialist", "2019-11-05", 62000, "michael.brown@example.com", "555-8765"),
        (1004, "Emily", "Davis", "Finance", "Accountant", "2022-01-10", 70000, "emily.davis@example.com", "555-4321"),
        (1005, "William", "Wilson", "Engineering", "DevOps Engineer", "2021-09-18", 78000, "william.wilson@example.com", "555-2468")
    ]
    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", sample_employees)
    conn.commit()

# 3️⃣ Import data from database
cursor.execute("SELECT * FROM employees")
db_data = cursor.fetchall()  
# Fetch all results as a list of tuples
print("Database Imported:\n", db_data[:5])  # Display first 5 rows for verification

# 4️⃣ Export data to another table
cursor.execute("""
CREATE TABLE IF NOT EXISTS export_table (
    EmployeeID INTEGER,
    FirstName TEXT,
    LastName TEXT,
    Department TEXT,
    Position TEXT,
    DateOfJoining TEXT,
    Salary REAL,
    Email TEXT,
    Phone TEXT
)
""")  

# Insert all data into the new table with correct number of placeholders
cursor.executemany("""
INSERT INTO export_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", db_data)  

conn.commit()  # Commit changes to the database
print("Database Exported!")  # Confirmation message
conn.close()  # Close the database connection

# -------------------------------

# 6️⃣ Pickle (Python Object Serialization)
import pickle  # Import pickle module to serialize/deserialize Python objects

# Export Python object (dictionary) to pickle
sample_data = {"name": "Alice", "age": 30, "department": "HR"}  
# Sample Python dictionary to save
with open("output/sample_data.pkl", "wb") as f:  
    # Open a file in binary write mode
    pickle.dump(sample_data, f)  
    # Serialize Python object and write it to file
print("Pickle Exported!")  # Confirmation message

# Import Python object from pickle
with open("output/sample_data.pkl", "rb") as f:  
    # Open pickle file in binary read mode
    loaded_data = pickle.load(f)  # Deserialize Python object from file
print("Pickle Imported:\n", loaded_data)  # Display the loaded object

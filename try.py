import sqlite3

conn = sqlite3.connect('./unit_2/chapter_2/data/employee.db')
cursor = conn.cursor()

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
employees = [
    (1001, "John", "Doe", "Engineering", "Software Engineer", "2021-06-15", 75000, "john.doe@example.com", "555-1234"),
    (1002, "Jane", "Smith", "Marketing", "Marketing Manager", "2020-03-22", 68000, "jane.smith@example.com", "555-5678"),
    (1003, "Michael", "Brown", "HR", "HR Specialist", "2019-11-05", 62000, "michael.brown@example.com", "555-8765"),
    (1004, "Emily", "Davis", "Finance", "Accountant", "2022-01-10", 70000, "emily.davis@example.com", "555-4321"),
    (1005, "William", "Wilson", "Engineering", "DevOps Engineer", "2021-09-18", 78000, "william.wilson@example.com", "555-2468")
]
cursor.executemany("""
INSERT OR REPLACE INTO employees
(EmployeeID, FirstName, LastName, Department, Position, DateOfJoining, Salary, Email, Phone)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""", employees)
conn.commit()
conn.close()
print("SQLite Database 'employee.db' created with employees table!")
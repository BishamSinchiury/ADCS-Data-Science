import pandas as pd
# Importing pandas library to use its functions
# As pd for easier reference and calling 
 

csv_data = pd.read_csv("./data/employee.csv")
#Import csv file with read_csv() function
# syntax: pd.read_csv(filepath)

print("CSV Imported: \n", csv_data.head())
#print data head and first five data rowof the csv file


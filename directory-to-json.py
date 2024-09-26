import pandas as pd
import json

# Load the CSV file
df = pd.read_csv('Employee-Directory-Working.csv')

# Create a list to store employee data in JSON format
employee_data = []

# Iterate through the DataFrame and append each row as a JSON object
for index, row in df.iterrows():
    employee = {
        "Employee Name": row['Employee Name'],
        "Department": row['Department'],
        "Title": row['Title'],
        "Employee ID Number": row['Employee ID Number'],
        "Directory URL": row['Directory URL']
    }
    employee_data.append(employee)

# Save the data to a JSON-formatted .txt file
with open('employee_directory_json.txt', 'w') as f:
    json.dump(employee_data, f, indent=4)

print("Conversion complete!")

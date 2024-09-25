import pandas as pd

# Load the CSV file
df = pd.read_csv('Employee-Directory-Working.csv')

# Open a text file for writing
with open('employee_directory_calendar_format.txt', 'w') as f:
    # Iterate through the rows of the DataFrame and write each employee's information
    for index, row in df.iterrows():
        f.write(f"Employee Name: {row['Employee Name']}\n")
        f.write(f"Department: {row['Department']}\n")
        f.write(f"Title: {row['Title']}\n")
        f.write(f"Employee ID Number: {row['Employee ID Number']}\n")
        f.write(f"Directory URL: {row['Directory URL']}\n")
        f.write("\n========================================\n\n")
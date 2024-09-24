# Open the original CSV file
with open('processed_employee_directory.csv', 'r') as infile, open('employee_directory_with_spaces.csv', 'w') as outfile:
    # Read all the rows from the original file
    lines = infile.readlines()

    # Write rows to the new file, inserting a blank line between each
    for line in lines:
        outfile.write(line)
        outfile.write('\n')  # Add an extra new line for space between rows

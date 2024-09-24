import csv
import re

# Function to process BioText and extract department and title
def process_biotext(biotext):
    # Initialize fields
    department = None
    title = None

    # Stop capturing at "Phone" if it exists
    biotext = re.split(r'Phone:', biotext)[0]

    # Extract title using regex
    title_match = re.search(r'Title:\s*(.*)', biotext)
    if title_match:
        title = title_match.group(1).strip()

    # Extract department (everything before "Title:")
    if title:
        department = biotext.split('Title:')[0].strip()

    return department, title

# Function to read from the existing CSV, process the BioText, and write to a new CSV
def process_employee_directory(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r', encoding='utf-8') as infile, open(output_csv_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write the header row for the new CSV
        writer.writerow(['EID URL', 'Employee Name', 'Department', 'Title'])

        # Skip the header of the input CSV
        next(reader)

        # Process each row of the input CSV
        for row in reader:
            eid_url = row[0]
            name = row[1]
            biotext = row[2]
            
            # Process the BioText to extract department and title
            department, title = process_biotext(biotext)

            # Write the processed information to the new CSV
            writer.writerow([eid_url, name, department, title])

    print(f"Processed employee directory saved to {output_csv_file}")

# Input and output CSV file paths
input_csv_file = 'employee_directory.csv'  # Replace with your actual input file path
output_csv_file = 'processed_employee_directory.csv'  # Output CSV file for processed data

# Run the processing function
process_employee_directory(input_csv_file, output_csv_file)
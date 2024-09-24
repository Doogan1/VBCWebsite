import requests
from bs4 import BeautifulSoup
import csv

# Function to get the name and the full BioText from the employee's page
def get_employee_info(eid_url):
    try:
        # Send a GET request to the employee's page
        response = requests.get(eid_url)
        response.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the name in the h1 element with class "BioName"
        name_tag = soup.find('h1', class_='BioName')
        name = name_tag.get_text(strip=True) if name_tag else None

        # Grab the entire BioText div content
        bio_text_div = soup.find('div', class_='BioText')
        bio_text = bio_text_div.get_text(strip=True) if bio_text_div else None

        return name, bio_text

    except requests.exceptions.RequestException:
        return None, None

# Function to generate a CSV with eid URLs, names, and full BioText content
def generate_employee_csv(max_eid, output_csv_file):
    consecutive_failures = 0  # To track consecutive failures
    max_consecutive_failures = 50  # Halt after 20 consecutive failures

    with open(output_csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Write the header row
        writer.writerow(['EID URL', 'Employee Name', 'BioText'])

        # Iterate over each EID starting from 1 up to max_eid
        for eid in range(1, max_eid + 1):
            eid_url = f"https://www.vanburencountymi.gov/Directory.aspx?eid={eid}"
            print(f"Processing {eid_url}...")

            employee_name, bio_text = get_employee_info(eid_url)

            if employee_name:
                # Reset consecutive failures if valid name found
                consecutive_failures = 0
                # Write the URL, name, and BioText to the CSV
                writer.writerow([eid_url, employee_name, bio_text])
                print(f"Found: {employee_name}")
            else:
                # Increment consecutive failures if no valid data
                consecutive_failures += 1
                print(f"No info found for {eid_url}")

            # Check if we should halt due to too many consecutive failures
            if consecutive_failures >= max_consecutive_failures:
                print(f"Halted after {max_consecutive_failures} consecutive failures.")
                break

    print(f"Employee CSV saved to {output_csv_file}")

# Maximum EID to query and output file path
max_eid = 500  # Set the upper limit for EID (adjust as needed)
output_csv_file = 'employee_directory.csv'

# Run the function to generate the CSV
generate_employee_csv(max_eid, output_csv_file)
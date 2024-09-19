import json
from parsing_utils import parse_icalendar  # Import the utility function

# Function to extract and parse iCalendar URLs from JSON, then save events to a new JSON file
def process_icalendar_urls(input_json_file, output_json_file):
    # Load the JSON file with URLs
    with open(input_json_file, 'r', encoding='utf-8') as infile:
        urls = json.load(infile)

    # Filter out only iCalendar URLs (usually ending in .ics or having iCalendar download links)
    ical_urls = [url for url in urls if '.ics' in url or 'iCalendar' in url]

    all_events = []  # List to store all events

    # Process each iCalendar URL
    for ical_url in ical_urls:
        print(f"Processing iCalendar URL: {ical_url}")
        events = parse_icalendar(ical_url)

        # Add the events to the overall list
        all_events.extend(events)

    # Save all events to the output JSON file
    with open(output_json_file, 'w', encoding='utf-8') as outfile:
        json.dump(all_events, outfile, indent=4)

    print(f"Events successfully saved to {output_json_file}")

# Input and output file paths
input_json_file = 'calendar_urls.json'  # Replace with the actual path to your file
output_json_file = 'parsed_calendar_events.json'  # Output file where events will be saved

# Run the function
process_icalendar_urls(input_json_file, output_json_file)
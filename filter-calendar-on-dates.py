import json
from datetime import datetime, timezone

# Function to filter events before 2030
def filter_events_before_2030(input_json_file, output_json_file):
    # Load the JSON file with events
    with open(input_json_file, 'r', encoding='utf-8') as infile:
        events = json.load(infile)

    # Define the cutoff date (Jan 1, 2030) as an offset-aware datetime (UTC)
    cutoff_date = datetime(2030, 1, 1, tzinfo=timezone.utc)

    # Filter events that occur before 2030
    filtered_events = []
    for event in events:
        try:
            event_start = datetime.fromisoformat(event['start'])
            # Only keep events that occur before the cutoff date
            if event_start < cutoff_date:
                filtered_events.append(event)
        except ValueError:
            print(f"Skipping invalid date format for event: {event['name']}")

    # Save the filtered events to a new JSON file
    with open(output_json_file, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_events, outfile, indent=4)

    print(f"Filtered events saved to {output_json_file}")

# Input and output file paths
input_json_file = 'parsed_calendar_events.json'  # Replace with the actual input file path
output_json_file = 'filtered_calendar_events.json'  # Output file for filtered events

# Run the filtering function
filter_events_before_2030(input_json_file, output_json_file)
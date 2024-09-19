import json

# Function to convert events from JSON to a readable TXT format
def convert_json_to_txt(input_json_file, output_txt_file):
    # Load the JSON file with events
    with open(input_json_file, 'r', encoding='utf-8') as infile:
        events = json.load(infile)

    # Open the TXT file for writing
    with open(output_txt_file, 'w', encoding='utf-8') as outfile:
        for event in events:
            # Write each event in a readable format
            outfile.write(f"Event Name: {event['name']}\n")
            outfile.write(f"Start Date: {event['start']}\n")
            outfile.write(f"End Date: {event['end']}\n")
            outfile.write(f"Description: {event.get('description', 'No description available')}\n")
            outfile.write("\n" + "="*40 + "\n\n")  # Separator between events

    print(f"Events successfully saved to {output_txt_file}")

# Input and output file paths
input_json_file = 'filtered_calendar_events.json'  # Replace with your JSON file path
output_txt_file = 'calendar_events.txt'  # Output file for chatbot

# Run the conversion function
convert_json_to_txt(input_json_file, output_txt_file)

import json

# Function to filter URLs that contain "Calendar.aspx"
def filter_calendar_urls(input_file, output_file):
    # Load the JSON file with URLs
    with open(input_json_file, 'r', encoding='utf-8') as infile:
        urls = json.load(infile)
    
    # Filter URLs that contain "Calendar.aspx"
    filtered_urls = [url for url in urls if 'Calendar.aspx' in url]
    
    # Save the filtered URLs to a new JSON file
    with open(output_json_file, 'w', encoding='utf-8') as outfile:
        json.dump(filtered_urls, outfile, indent=4)
    
    print(f"Filtered URLs saved to {output_file}")

# Input and output file paths
input_json_file = 'sitemap_urls.json'
output_json_file = 'calendar_urls.json'

# Run the filtering function
filter_calendar_urls(input_json_file, output_json_file)
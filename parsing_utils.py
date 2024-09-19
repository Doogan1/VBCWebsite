import requests
from ics import Calendar

# Function to parse iCalendar data from a URL and handle Arrow serialization
def parse_icalendar(ical_url):
    try:
        # Download the iCalendar file
        response = requests.get(ical_url)
        response.raise_for_status()

        # Check if the response is a valid iCalendar
        if 'text/calendar' not in response.headers.get('Content-Type', ''):
            print(f"Skipping non-iCalendar content from {ical_url}")
            return []

        # Parse the iCalendar content
        c = Calendar(response.text)

        # Extract and return events
        events = []
        for event in c.events:
            events.append({
                'name': event.name,
                'start': event.begin.isoformat(),  # Convert Arrow to ISO 8601 string
                'end': event.end.isoformat(),      # Convert Arrow to ISO 8601 string
                'description': event.description
            })
        return events

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the iCalendar: {e}")
        return []
    except Exception as e:
        print(f"An error occurred while parsing the iCalendar: {e}")
        return []
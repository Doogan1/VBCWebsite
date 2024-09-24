import requests
from bs4 import BeautifulSoup

# URLs to scrape
urls = {
    'cdirectory_test':'https://www.vanburencountymi.gov/Directory.aspx'
}

# Function to extract and save text content
def extract_and_save_text(url, filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text_content = soup.get_text(separator='\n', strip=True)
    
    # Save to a text file
    with open(f'{filename}.txt', 'w',encoding='utf-8') as file:
        file.write(text_content)

# Extracting and saving text for both URLs
for filename, url in urls.items():
    extract_and_save_text(url, filename)

# Return file paths
file_paths = [f'/mnt/data/{filename}.txt' for filename in urls.keys()]
file_paths
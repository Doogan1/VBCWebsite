import xml.etree.ElementTree as ET
import json

# Load the sitemap.xml file
tree = ET.parse('sitemap.xml')
root = tree.getroot()

# Extract all URLs from the sitemap
sitemap_urls = set()

# Sitemap URLs are typically in <url><loc> tags
for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
    loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
    sitemap_urls.add(loc)

# Save the URLs to a JSON file
with open('sitemap_urls.json', 'w') as f:
    json.dump(list(sitemap_urls), f, indent=4)

print(f"Sitemap URLs successfully saved to sitemap_urls.json with {len(sitemap_urls)} URLs.")
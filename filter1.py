import json
import re
import xml.etree.ElementTree as ET

# Load the URLs from the JSON file
with open('sitemap_urls.json', 'r') as f:
    sitemap_urls = set(json.load(f))

# Define the regex pattern to filter URLs of the form https://www.vanburencountymi.gov/*some number*/*something*
url_pattern = re.compile(r"https://www\.vanburencountymi\.gov/\d+/[a-zA-Z0-9_\-]+")

# Filter URLs that match the specified pattern
filtered_urls = {url for url in sitemap_urls if url_pattern.match(url)}

# Create the XML sitemap for the filtered URLs
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for url in filtered_urls:
    url_tag = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url_tag, "loc")
    loc.text = url

# Save the filtered XML sitemap to a file
with open('filtered_sitemap.xml', 'wb') as f:
    sitemap = ET.ElementTree(urlset)
    sitemap.write(f, encoding="utf-8", xml_declaration=True)

print(f"Filtered sitemap generated with {len(filtered_urls)} URLs.")
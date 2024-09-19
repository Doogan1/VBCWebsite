import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import xml.etree.ElementTree as ET

# The base URL of the site to crawl
base_url = "https://www.vanburencountymi.gov"
visited_urls = set()
sitemap_urls = set()

def crawl(url):
    if url in visited_urls:
        return

    print(f"Crawling: {url}")
    visited_urls.add(url)
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Find all <a> tags to extract links
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(base_url, href)  # Resolve relative URLs
            
            # Filter only links that belong to the same domain
            parsed_url = urlparse(full_url)
            if parsed_url.netloc == urlparse(base_url).netloc:
                sitemap_urls.add(full_url)
                if full_url not in visited_urls:
                    crawl(full_url)  # Recursively crawl
    except Exception as e:
        print(f"Error crawling {url}: {e}")

# Start crawling from the base URL
crawl(base_url)

# Create XML sitemap
urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for url in sitemap_urls:
    url_tag = ET.SubElement(urlset, "url")
    loc = ET.SubElement(url_tag, "loc")
    loc.text = url

# Save the XML to a file
sitemap = ET.ElementTree(urlset)
with open("sitemap.xml", "wb") as f:
    sitemap.write(f, encoding="utf-8", xml_declaration=True)

print(f"Sitemap generated with {len(sitemap_urls)} URLs.")
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

# Load the HTML file
with open('htmlSitemap.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# Find all links in the HTML sitemap
urls = []
for li in soup.find_all('li'):
    a_tag = li.find('a')
    if a_tag and a_tag.get('href'):
        url = a_tag['href']
        # If the link is relative, convert it to an absolute URL
        if not url.startswith('http'):
            url = 'https://www.vanburencounty.org' + url
        urls.append(url)

# Create an XML tree for the sitemap
urlset = ET.Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for url in urls:
    url_tag = ET.SubElement(urlset, 'url')
    loc = ET.SubElement(url_tag, 'loc')
    loc.text = url

# Convert the XML tree to a string
sitemap = ET.ElementTree(urlset)
sitemap.write('sitemap.xml', encoding='utf-8', xml_declaration=True)

print("Sitemap generated successfully as sitemap.xml")
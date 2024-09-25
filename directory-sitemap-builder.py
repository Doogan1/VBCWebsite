import pandas as pd

# Load the CSV file
df = pd.read_csv('processed_employee_directory.csv')

# Open an XML file for writing
with open('directory_sitemap.xml', 'w') as f:
    # Write the XML header
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
    
    # Iterate through the first column of URLs and write each as a <url> entry
    for url in df['EID URL']:  # Assuming 'EID URL' is the column with URLs
        f.write(f'   <url>\n')
        f.write(f'      <loc>{url}</loc>\n')
        f.write(f'   </url>\n')
    
    # Close the <urlset> tag
    f.write('</urlset>')

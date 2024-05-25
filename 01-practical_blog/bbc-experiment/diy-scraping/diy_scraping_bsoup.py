from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
url = 'https://www.bbc.com/news/world-europe-67895152'

# Make a request to get the page content
response = requests.get(url)
html_content = response.content


# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the title
title = soup.find('h1', class_='sc-518485e5-0 bWszMR').text

print(soup.find('time'))
# Extract publication date
pub_date = soup.find('time')['datetime']

# Extract main article content
# Assuming main content is in paragraphs <p>
article_content = soup.find_all('p')
content = ' '.join([para.get_text() for para in article_content])

# Extract image information (if present)
image_data = []
images = soup.find_all('img')
for image in images:
    img_dict = {
        'src': image.get('src'),
        'alt': image.get('alt')
    }
    image_data.append(img_dict)

# Extract other metadata if needed

# Print or process the scraped data
print(f"Title: {title}")
print(f"Publication Date: {pub_date}")
print("Article Content:", content)
print("Images:", image_data)

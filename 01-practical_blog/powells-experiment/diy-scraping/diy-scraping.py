from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
url = 'https://www.powells.com/featured/picks-of-the-season-2023'

# Make a request to get the page content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the specific section in the HTML (modify this according to your HTML structure)
books_section = soup.find_all('div', class_='thumbnail')

# Initialize a list to store extracted book data
book_data = []

# Iterate through each book in the section and extract details
for book in books_section:
    title = book.h3.get_text(strip=True) if book.h3 else 'No Title'
    author = book.find('p', class_='picksauthor').get_text(strip=True) if book.find('p', class_='picksauthor') else 'No Author'
    link = book.a['href'] if book.a else 'No Link'
    book_data.append({'Title': title, 'Author': author, 'Link': link})

# Print or process the extracted data
for book in book_data:
    print(book)

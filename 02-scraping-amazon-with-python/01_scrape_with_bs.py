from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
url = 'https://www.amazon.com/MSI-Desktop-i5-12400F-GeForce-VR-Ready/dp/B0CJB41ZT5'

# Make a request to get the page content
response = requests.get(url)
html_content = response.content


# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting data
data = {}

# Product Title
product_title = soup.find("span", {"id": "productTitle"}).get_text(strip=True)
data["Product Title"] = product_title

# Main Image URL
main_image_url = soup.find("img", {"id": "landingImage"})["src"]
data["Main Image URL"] = main_image_url

thumbnail_urls=[]
# Thumbnail Image URLs
for li in soup.find_all("li", class_="item"):
    img_tags = li.find_all('img')

    for img in img_tags:
        thumbnail_urls.append(img.get('src'))
data["Thumbnail Image URLs"] = thumbnail_urls

# Price
price = soup.find("span", class_="a-price").get_text(strip=True).split('$')
data["Price"] = f'${price[1]}'

#About Product
bullet_points=[]

for feature in soup.find_all("div", {"id": "feature-bullets"}):
  for product_desc in feature.find_all('li'):
    bullet_points.append(product_desc.get_text(strip=True))

data["Product Description"] = bullet_points

"""
# Specific Product Details
product_details = {}
details_table = soup.find("table", class_="a-normal").find_all("tr")
for row in details_table:
    columns = row.find_all("td")
    key = columns[0].get_text(strip=True)
    value = columns[1].get_text(strip=True)
    product_details[key] = value
data["Product Details"] = product_details

# Product Description
product_description = soup.find("div", id="productDescription").get_text(strip=True)
data["Product Description"] = product_description

print(data)
# Technical Details
technical_details = {}
tech_table = soup.find("table", id="productDetails_techSpec_section_1").find_all("tr")
for row in tech_table:
    columns = row.find_all("td")
    key = columns[0].get_text(strip=True)
    value = columns[1].get_text(strip=True)
    technical_details[key] = value
data["Technical Details"] = technical_details

# Additional Information
additional_info = {}
additional_info_table = soup.find("table", id="productDetails_detailBullets_sections1").find_all("tr")
for row in additional_info_table:
    columns = row.find_all("td")
    key = columns[0].get_text(strip=True)
    value = columns[1].get_text(strip=True)
    additional_info[key] = value
data["Additional Information"] = additional_info

# Product Availability and Warranty Information
availability_warranty_info = {}

# Assuming the information is in a div with a specific id (adjust as per actual HTML)
availability_warranty_div = soup.find("div", id="availability_warranty_div")

if availability_warranty_div:
    # Extracting all rows in the div
    rows = availability_warranty_div.find_all("tr")
    for row in rows:
        columns = row.find_all("td")
        if len(columns) == 2:
            # Assuming the first column is the title and the second is the value
            key = columns[0].get_text(strip=True)
            value = columns[1].get_text(strip=True)
            availability_warranty_info[key] = value

data["Availability and Warranty Information"] = availability_warranty_info
"""

# Print extracted data
for key, value in data.items():
    print(f"{key}: {value}")
import requests
from bs4 import BeautifulSoup

def scrape_expedia_hotel_data(url):
    # Send an HTTP GET request to the URL
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all hotel information containers
    hotel_containers = soup.find_all("div", class_="uitk-card-content-section")

    # List to store hotel data
    hotels_data = []

    # Loop through each container and extract details
    for hotel in hotel_containers:
        # Create a dictionary to store hotel details
        hotel_dict = {}

        # Extract hotel name
        name_section = hotel.find("h3", class_="uitk-heading")
        hotel_dict["name"] = name_section.get_text(strip=True) if name_section else 'N/A'

        # Extract location
        location_section = hotel.find("div", class_="uitk-text")
        hotel_dict["location"] = location_section.get_text(strip=True) if location_section else 'N/A'

        # Extract price
        price_section = hotel.find("div", attrs={"data-test-id": "price-summary"})
        hotel_dict["price"] = price_section.get_text(strip=True) if price_section else 'N/A'

        # Extract review summary
        review_section = hotel.find("div", class_="uitk-layout-flex-item")
        hotel_dict["review_summary"] = review_section.get_text(strip=True) if review_section else 'N/A'

        # Extract number of reviews
        review_count_section = hotel.find("div", class_="uitk-text", attrs={"aria-hidden": "true"})
        hotel_dict["num_reviews"] = review_count_section.get_text(strip=True) if review_count_section else 'N/A'

        # Append the dictionary to the list
        hotels_data.append(hotel_dict)

    return hotels_data

# URL to scrape
url = "https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent="

# Scrape the data and store it in a variable
hotel_data = scrape_expedia_hotel_data(url)

# Print all hotels data
print(hotel_data)

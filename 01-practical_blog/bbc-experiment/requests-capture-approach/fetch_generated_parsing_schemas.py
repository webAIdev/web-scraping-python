import requests
import json

# Open the config.json file containing secret keys
with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

result_download_url = "https://api.webit.live/api/v1/tasks/bd95e877-f53a-447f-b9c9-659872708f1d/results"

payload = {}

# Headers for the API request, including the content type and authorization key
headers = {
  'Authorization': secret_keys['key'],
  'Content-Type': 'application/json'
}

# Making a request to the API with the specified URL, headers, and data (payload)
response = requests.request("GET", result_download_url, headers=headers, data=payload)

# Printing the response text from the API call
print(response.text)

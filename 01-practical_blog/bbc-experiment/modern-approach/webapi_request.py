import requests
import json

# Open the config.json file containing secret keys
with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

url = "https://api.webit.live/api/v1/realtime/web"

payload = json.dumps({
  "parse": True,
  "url": "https://www.bbc.com/news/world-europe-67895152",
  "format": "json",
  "render": True,
  "country": "US",
  "locale": "en",
  "parse_options": {
    "source": "parsit-ai",
    "params": {
      "parser_id": "65a6f946c530c7b6e40464ac"
    }
  }
})

# Headers for the API request, including the content type and authorization key
headers = {
  'Authorization': secret_keys['key'],
  'Content-Type': 'application/json'
}

# Making a request to the API with the specified URL, headers, and data (payload)
response = requests.request("POST", url, headers=headers, data=payload)

# Printing the response text from the API call
print(response.text)

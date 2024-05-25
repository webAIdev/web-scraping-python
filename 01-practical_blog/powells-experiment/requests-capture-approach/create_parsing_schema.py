import requests
import json

# Open the config.json file containing secret keys
with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

url = "https://api.webit.live/api/v1/async/web"

payload = json.dumps({
  "url": "https://www.powells.com/featured/picks-of-the-season-2023",
  "method": "GET",
  "parse": True,
  "render": True,
  "parse_options": {
    "source": "parsit-ai",
    "params": {
      "schema": {
        "fields": {
          "title": {
            "type": "str"
          },
          "author": {
            "type": "str"
          },
          "book_link": {
            "type": "str"
          },
          "book_review": {
            "type": "str"
          },
          "book_cover_url": {
            "type": "str"
          }
        }
      }
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

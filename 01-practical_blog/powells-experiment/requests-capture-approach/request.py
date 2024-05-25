import requests
import json

# Open the config.json file containing secret keys
with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)
    
url = "https://api.webit.live/api/v1/realtime/web"

payload = json.dumps({
  "url": "https://www.powells.com/featured/picks-of-the-season-2023",
  "parse": True,
  "format": "json",
  "render": True,
  "country": "US",
  "locale": "en",
  "network_capture": [
        {
            "method": "GET",
            "url": {
                "type": "contains",
                "value": "print"
            }
        }
    ]
})


# Headers for the API request, including the content type and authorization key
headers = {
  'Content-Type': 'application/json',
  'Authorization': secret_keys['key']
}

# Making a request to the API with the specified URL, headers, and data (payload)
response = requests.request("GET", url, headers=headers, data=payload)

# Printing the response text from the API call
print(response.text)

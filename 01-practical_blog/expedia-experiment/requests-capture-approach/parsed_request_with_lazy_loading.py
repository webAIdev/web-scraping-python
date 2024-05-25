import requests
import json

# Open the config.json file containing secret keys
with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)
    
url = "https://api.webit.live/api/v1/realtime/web"

payload = json.dumps({
  "url": "https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent=",
  "parse": True,
  "parse_options": {
    "source": "parsit-ai",
    "params": {
      "parser_id": "65a1267c48d771f6806583b7"
    }
  },
  "format": "json",
  "render": True,
  "country": "US",
  "locale": "en",
  "render_flow": [
    {
      "wait": {
        "delay": 8000
      },
      "infinite_scroll": {
        "loading_selector": ".is-visible",
        "delay_after_scroll": 2000,
        "duration": 15000
      }
    }
  ],
  "network_capture": [
    {
      "url": {
        "type": "contains",
        "value": "www.expedia.com/graphql"
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

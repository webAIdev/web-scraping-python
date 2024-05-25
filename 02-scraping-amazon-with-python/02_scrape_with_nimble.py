import requests
import json

# Open the config.json file containing secret keys
with open('../secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)


url = 'https://api.webit.live/api/v1/realtime/ecommerce'
headers = {
    'Authorization': secret_keys['key'],
    'Content-Type': 'application/json'
}
data = {
    "vendor": "amazon",
    "url": "https://www.amazon.com/MSI-Desktop-i5-12400F-GeForce-VR-Ready/dp/B0CJB41ZT5",
    "country": "US",
    "zip": "90210",
    "locale": "en"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

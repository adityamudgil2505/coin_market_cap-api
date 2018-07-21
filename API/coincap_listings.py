import requests
import json

listing_url = 'https://api.coinmarketcap.com/v2/listings/'
request = requests.get(listing_url)
result = request.json()

#print(json.dumps(result,sort_keys=True,indent=4))
data = result['data']

for currency in data:
    rank = currency['id']
    name = currency['name']
    symbol = currency['symbol']
    web_slug = currency['website_slug']
    print('{}: {} ({}) {}'.format(rank,name,symbol,web_slug))

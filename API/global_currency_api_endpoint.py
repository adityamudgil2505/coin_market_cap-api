import requests
import json
from datetime import datetime as dt

global_url = 'https://api.coinmarketcap.com/v2/global/'
request = requests.get(global_url)
result = request.json()

#print(json.dumps(result,sort_keys=True,indent=4))
active_currency = result['data']['active_cryptocurrencies']
active_market = result['data']['active_markets']
bitcoin_percentage = result['data']['bitcoin_percentage_of_market_cap']
last_updated = result['data']['last_updated']
global_cap = int(result['data']['quotes']['USD']['total_market_cap'])
global_volume = int(result['data']['quotes']['USD']['total_volume_24h'])

active_currency_string = '{:,}'.format(active_currency)
active_market_string = '{:,}'.format(active_market)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)
last_updated_string = dt.fromtimestamp(last_updated).strftime('%b'+' %d'+', %Y'+' at %I:%M%p')

print('\n'+'There are currently {} active cryptocurrencies and {} active markets.'.format(active_currency_string,active_market_string))
print('The global cap of all cryptos is {} and the 24 hours global volume is {}.'.format(global_cap_string,global_volume_string))
print('Bitcoin\'s total percentage of the global cap is {}%.\n'.format(bitcoin_percentage) )
print('This information was last updated on {}.'.format(last_updated_string))
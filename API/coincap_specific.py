import requests
import json
from datetime import datetime as dt
convert = input('Which currency do you want your result?: ').upper()
listing_url = 'https://api.coinmarketcap.com/v2/listings/'
end_url = '?structure=array&convert='+convert

request = requests.get(listing_url)
results = request.json()
data = results['data']
ticker_url_pair = {}
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pair[symbol]=url

while True:
    print()
    choice = input('Enter the symbol of the currency: ')
    choice = choice.upper()
    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/'+ str(ticker_url_pair[choice]) + '/' + end_url
    #print(ticker_url)
    request = requests.get(ticker_url)
    results = request.json()
    #print(json.dumps(results,sort_keys=True,indent=4))
    currency = results['data'][0]
    circulation_supply = int(currency['circulating_supply'])
    circulation_supply_string = '{:,}'.format(circulation_supply)
    last_updated = int(currency['last_updated'])
    rank = str(currency['rank'])
    name = currency['name']
    symbol = currency['symbol']
    total_supply = int(currency['total_supply'])
    total_supply_string = '{:,}'.format(total_supply)
    quotes = currency['quotes'][convert]
    market_cap = quotes['market_cap']
    market_cap = '{:,}'.format(market_cap)
    percent_change_1h = quotes['percent_change_1h']
    percent_change_24h = quotes['percent_change_24h']
    percent_change_7d = quotes['percent_change_7d']
    price = quotes['price']
    price = '{:,}'.format(price)
    volume_24h = quotes['volume_24h']
    volume_24h = '{:,}'.format(volume_24h)

    print('\n{}: {} ({})'.format(rank, name, symbol))
    print('\tMarket cap: \t\t\t\t\t\t\t{}'.format(market_cap))
    print('\tPrice: \t\t\t\t\t\t\t\t\t{}'.format(price))
    print('\t24h Volume: \t\t\t\t\t\t\t{}'.format(volume_24h))
    print('\tHour change: \t\t\t\t\t\t\t{}%'.format(percent_change_1h))
    print('\tDay change: \t\t\t\t\t\t\t{}%'.format(percent_change_24h))
    print('\tWeek change: \t\t\t\t\t\t\t{}%'.format(percent_change_7d))
    print('\tTotal supply: \t\t\t\t\t\t\t{}'.format(total_supply_string))
    print('\tCirculation supply: \t\t\t\t\t{}'.format(circulation_supply_string))
    print('\tPercentage of coins in circulation: \t{}%'.format(round(circulation_supply / total_supply * 100, 2)))

    try_again = input('Do you want to try again? (y/n): ')
    if try_again == 'n':
        break
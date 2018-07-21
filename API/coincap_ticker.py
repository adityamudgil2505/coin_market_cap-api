import requests
import json
from datetime import datetime as dt
while True:
    listing_url = 'https://api.coinmarketcap.com/v2/ticker/'
    limit = 100
    start = 1
    sort = 'rank'
    convert = 'USD'

    choice = input('Do you want to customize parameters? (y/n) : ')
    if choice == 'y':
        limit = input('What is the custom limit? (1-100):\n')
        start = input('What is the custom start? (1-2200):\n')
        sort = input('What do you want to sort by? (id,rank,name,max_supply,symbol):\n')
        convert = input('What is your local currency? ("AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR", "GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", "PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR"):\n')

    listing_url += '?start='+str(start)+'&limit='+str(limit)+'&sort='+sort+'&convert='+convert+'&structure=array'
    request = requests.get(listing_url)
    result = request.json()
    #print(json.dumps(result,sort_keys=True,indent=4))
    data = result['data']
    last_updated =0
    for currency in data:
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

        print('\n{}: {} ({})'.format(rank,name,symbol))
        print('\tMarket cap: \t\t\t\t\t\t\t{}'.format(market_cap))
        print('\tPrice: \t\t\t\t\t\t\t\t\t{}'.format(price))
        print('\t24h Volume: \t\t\t\t\t\t\t{}'.format(volume_24h))
        print('\tHour change: \t\t\t\t\t\t\t{}%'.format(percent_change_1h))
        print('\tDay change: \t\t\t\t\t\t\t{}%'.format(percent_change_24h))
        print('\tWeek change: \t\t\t\t\t\t\t{}%'.format(percent_change_7d))
        print('\tTotal supply: \t\t\t\t\t\t\t{}'.format(total_supply_string))
        print('\tCirculation supply: \t\t\t\t\t{}'.format(circulation_supply_string))
        print('\tPercentage of coins in circulation: \t{}%'.format(round(circulation_supply/total_supply*100,2)))

    last_updated_string = dt.fromtimestamp(last_updated).strftime('%b'+' %d'+', %Y'+' at %I:%M%p')
    print('\nLast updated '+last_updated_string)
    try_again = input('Do you want to try again? (y/n): ')
    if try_again == 'n':
        break


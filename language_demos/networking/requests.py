import urllib.request
import json


url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'

with urllib.request.urlopen(url) as response:
    coin_price = json.loads(response.read())
    print(coin_price)

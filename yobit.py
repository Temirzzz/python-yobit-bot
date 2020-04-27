import requests

def get_btc():
    url = 'https://yobit.net/api/2/btc_usd/ticker'
    resp = requests.get(url).json()
    price = resp['ticker']['last'] 
    return str(price) + ' доляров, епта!'


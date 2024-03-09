from prometheus_client import start_http_server, Gauge
import time
import requests

# Create a metric to track BTCUSD price.
BITCOIN_PRICE = Gauge('bitcoin_price', 'Current Bitcoin price in USD')

def get_bitcoin_price():
    # do a GET on CoinDesk API. for latest BTCUSD price
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return float(data['bpi']['USD']['rate'].replace(',', ''))

if __name__ == '__main__':
    # start server at port 8000
    start_http_server(8000)

    while True:
        # get the latest BTC price & update metric
        bitcoin_price = get_bitcoin_price()
        BITCOIN_PRICE.set(bitcoin_price)

        # Wait for 1 min before querying again
        time.sleep(60)  

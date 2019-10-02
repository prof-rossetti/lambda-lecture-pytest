
import os
import json

from dotenv import load_dotenv
import requests

load_dotenv() #> loads contents of the .env file into the script's environment

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="abc123") # use "abc123" as a default value, and surprisingly this should work, based on the API we are using. Otherwise

def get_stock_data(symbol):
    """
    Issues an HTTP request to the Alphavantage API.
    Example: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=abc123
    """
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    return parsed_response

def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

def latest_closing_price(parsed_response):
    """
    Param parsed_response: a dictionary representing the JSON API response.
    """

    latest_close = 100.00 # TODO: parse the parsed_response

    return latest_close

if __name__ == "__main__":

    symbol = input("Hello, please input a stock symbol (e.g. 'AMZN'): ")
    print(f"Requesting stock data for {symbol}...")

    parsed_response = get_stock_data(symbol)
    print("----------")
    print(parsed_response)
    print("----------")

    latest_close = latest_closing_price(parsed_response)
    print("Latest closing price is:", to_usd(latest_close))

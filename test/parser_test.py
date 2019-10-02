


from app.parser import to_usd, latest_closing_price

def test_to_usd():
    assert to_usd(123456.8) == "$123,456.80"

# Using simplified mock data in this test allows us to learn what kind of response structure to expect from the API.
# We could use a hard-coded structure, like the one you see below,
# ... or we could try reading in the mock data from a file like "test/data/msft_response.json".
# Either way, using mock data helps us prevent issuing unnecessary HTTP requests,
# ... which saves time and resources on both the client and server side,
# ... and allows us to run tests without a network connection.
def test_latest_closing_price():
    mock_parsed_response = {
        "Meta Data": {
            "1. Information": "Daily Prices (open, high, low, close) and Volumes",
            "2. Symbol": "MSFT",
            "3. Last Refreshed": "2018-06-08",
            "4. Output Size": "Full size",
            "5. Time Zone": "US/Eastern"
        },
        "Time Series (Daily)": {
            "2019-06-08": {
                "1. open": "101.0924",
                "2. high": "101.9500",
                "3. low": "100.5400",
                "4. close": "101.6300",
                "5. volume": "22165128"
            },
            "2019-06-07": {
                "1. open": "102.6500",
                "2. high": "102.6900",
                "3. low": "100.3800",
                "4. close": "100.8800",
                "5. volume": "28232197"
            },
            "2019-06-06": {
                "1. open": "102.4800",
                "2. high": "102.6000",
                "3. low": "101.9000",
                "4. close": "102.4900",
                "5. volume": "21122917"
            }
        }
    }

    assert latest_closing_price(mock_parsed_response) == 101.63

import yfinance as yf

def testScript():
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period="1d")  # Fetches the last day's data
    data.reset_index(inplace=True)  # This line is added to convert the date index to a column
    return data.to_dict('records')  
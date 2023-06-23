#For third party API Calls! 
import requests
from .ApiConfig import ALPACA_API_KEY,ALPACA_API_SECRET
import yfinance as yf

ALPACA_BASE_URL = "https://api.alpaca.markets"
PAPER_BASE_URL = "https://paper-api.alpaca.markets"
class AlpacaApi():
    
    #set base URL and headers:
    
    def __init__(self):
        self.BASE_URL = ALPACA_BASE_URL
        self.headers = {
            "APCA-API-KEY-ID":ALPACA_API_KEY,
            "APCA-API-SECRET-KEY":ALPACA_API_SECRET
        }
    
    def get_account_info(self):
        #should  be returning data about Alpaca account
        response = requests.get(self.BASE_URL + "/v2/account", headers=self.headers)
        return response.json()
    
class YFinanceApi():
    def __init__(self):
        None
    
    def get_BTC_Trading_Data(self):
        stock_symbol = "BTC-USD"
        start_date = "2022-12-26"
        end_date = "2022-12-31"

        data = yf.download(stock_symbol, start=start_date, end=end_date)
        data.index = data.index.strftime('%Y-%m-%d')
        return data.to_dict()
    
    def make_trade(self, symbol, shares, side):
        data = {
            "symbol": symbol,
            "qty": shares,
            "side": side,
            "type": "market",
            "time_in_force": "gtc"
        }
        response = requests.post(self.BASE_URL + "/v2/orders", json=data, headers=self.headers)
        return response.json()
            

import yfinance as yf
#import talib
import pandas as pd
import alpaca_trade_api as tradeapi

def testScript():
    ticker = yf.Ticker("AAPL")
    data = ticker.history(period="1d")  # Fetches the last day's data
    data.reset_index(inplace=True)  # This line is added to convert the date index to a column
    return data.to_dict('records')  


'''


# Set up Alpaca API credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET_KEY'
base_url = 'https://paper-api.alpaca.markets'


# Initialize Alpaca API
api = tradeapi.REST(api_key, api_secret, base_url, api_version='v2')


# Define the trading symbol and time frame
symbol = 'AAPL'
timeframe = '1D'


# Set up the technical indicators' parameters
rsi_period = 14
macd_fast_period = 12
macd_slow_period = 26
macd_signal_period = 9
momentum_period = 10


# Define the number of shares to buy/sell
shares_to_trade = 10


# Fetch historical data using yfinance
data = yf.download(symbol, period='60d', interval=timeframe)


# Calculate the RSI using TA-Lib
rsi = talib.RSI(data['Close'], timeperiod=rsi_period)


# Calculate the MACD using TA-Lib
macd, macd_signal, _ = talib.MACD(data['Close'], fastperiod=macd_fast_period, slowperiod=macd_slow_period, signalperiod=macd_signal_period)


# Calculate the Momentum using TA-Lib
momentum = talib.MOM(data['Close'], timeperiod=momentum_period)


# Create a DataFrame to store the signals
signals = pd.DataFrame(index=data.index)
signals['RSI'] = rsi
signals['MACD'] = macd
signals['MACD_Signal'] = macd_signal
signals['Momentum'] = momentum


# Define the trading strategy
def generate_signals(signals):
   signals['Signal'] = 0  # Initialize a column for the trading signals


   # Generate buy signals
   signals.loc[(signals['RSI'] < 30) & (signals['MACD'] > signals['MACD_Signal']) & (signals['Momentum'] > 0), 'Signal'] = 1


   # Generate sell signals
   signals.loc[(signals['RSI'] > 70) & (signals['MACD'] < signals['MACD_Signal']) & (signals['Momentum'] < 0), 'Signal'] = -1


   return signals


# Generate trading signals
signals = generate_signals(signals)


# Print the signals DataFrame (for demonstration purposes)
print(signals)


# Execute trades based on the signals
for i in range(len(signals)):
   if signals['Signal'][i] == 1:
       # Buy the specified number of shares
       api.submit_order(
           symbol=symbol,
           qty=shares_to_trade,
           side='buy',
           type='market',
           time_in_force='gtc'
       )
       print('Buy signal generated. Buying', shares_to_trade, 'shares of', symbol)
   elif signals['Signal'][i] == -1:
       # Sell the specified number of shares
       api.submit_order(
           symbol=symbol,
           qty=shares_to_trade,
           side='sell',
           type='market',
           time_in_force='gtc'
       )
       print('Sell signal generated. Selling', shares_to_trade, 'shares of', symbol)

'''


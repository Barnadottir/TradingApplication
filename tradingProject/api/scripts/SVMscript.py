

import yfinance as yf
import talib
from sklearn.svm import SVR
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


# Step 1: Gather Historical Data
symbol = "BTC-USD"
start_date = "2021-01-01"
end_date = "2023-06-20"


data = yf.download(symbol, start=start_date, end=end_date)


# Step 2: Feature Engineering and Labeling
data['MACD'], _, _ = talib.MACD(data['Close'], fastperiod=3, slowperiod=9, signalperiod=2)
data['RSI'] = talib.RSI(data['Close'], timeperiod=5)
data['MOM'] = talib.MOM(data['Close'], timeperiod=5)
data['VolumeIndicator'] = talib.MA(data['Volume'], timeperiod=5) / talib.MA(data['Volume'], timeperiod=20)
data['BBUpper'], data['BBMiddle'], data['BBLower'] = talib.BBANDS(data['Close'], timeperiod=10, nbdevup=2, nbdevdn=2)
data['StochasticK'], data['StochasticD'] = talib.STOCH(data['High'], data['Low'], data['Close'], fastk_period=12, slowk_period=3, slowd_period=3)


data['Target'] = data['Close'].shift(-1) # Use the next day's closing price as the target variable


# Step 3: Prepare data
features = ['MACD', 'RSI', 'MOM', 'VolumeIndicator', 'BBUpper', 'BBMiddle', 'BBLower', 'StochasticK', 'StochasticD']
# Note: It's important to drop the last row here because its 'Target' is NaN
data = data.dropna()


X = data[features].values
y = data['Target'].values


# Step 4: Split Data into Training and Testing Sets
split_date = "2023-02-01"
train_data = data[data.index < split_date]
test_data = data[data.index >= split_date]


X_train = train_data[features].values
y_train = train_data['Target'].values


X_test = test_data[features].values
y_test = test_data['Target'].values


# Step 5: Train the SVR Model
svm_model = SVR(kernel='linear')
svm_model.fit(X_train, y_train)


# Step 6: Make Predictions for the Next Day
next_day_features = X_test[-1].reshape(1, -1)
next_day_prediction = svm_model.predict(next_day_features)


# Step 7: Define threshold and calculate holding period
threshold = 200  # Example threshold value
current_price = test_data['Close'].iloc[-1]
target_price_long = current_price + threshold
target_price_short = current_price - threshold


if next_day_prediction > target_price_long:
   position = 'Long'
   holding_period = 1  # Hold the position for 1 day
elif next_day_prediction < target_price_short:
   position = 'Short'
   holding_period = 1  # Hold the position for 1 day
else:
   position = 'No position'
   holding_period = 0  # No position, no holding period









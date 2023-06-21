


import yfinance as yf
import pandas as pd
import talib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt


# Download the historical data
ticker = yf.Ticker("^GSPC")
data = ticker.history(period="max")

# Clean up the data and add target variable
data = data.loc["1990/01/01":].copy()
data["Tomorrow"] = data["Close"].shift(-1)
data["Target"] = (data["Tomorrow"] > data["Close"]).astype(int)

# Calculate technical indicators
data['MACD'], _, _ = talib.MACD(data['Close'], fastperiod=9, slowperiod=18, signalperiod=3)
data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
data['MOM'] = talib.MOM(data['Close'], timeperiod=10)
data['VolumeIndicator'] = talib.MA(data['Volume'], timeperiod=5) / talib.MA(data['Volume'], timeperiod=20)
data['BBUpper'], data['BBMiddle'], data['BBLower'] = talib.BBANDS(data['Close'], timeperiod=20, nbdevup=2, nbdevdn=2)
data['StochasticK'], data['StochasticD'] = talib.STOCH(data['High'], data['Low'], data['Close'], fastk_period=14, slowk_period=3, slowd_period=3)

# Define predictors and train/test split
predictors = ["Close", "Volume", "Open", "High", "Low", 'MACD', 'RSI', 'MOM', 'VolumeIndicator', 'BBUpper', 'BBMiddle', 'BBLower', 'StochasticK', 'StochasticD']
data = data.dropna()
train = data.iloc[:-100]
test = data.iloc[-100:]

# Train the random forest model
imputer = SimpleImputer()
model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)
pipeline = make_pipeline(imputer, model)
pipeline.fit(train[predictors], train["Target"])

# Make predictions on the test set
preds = pipeline.predict(test[predictors])
preds = pd.Series(preds, index=test.index)

# Evaluate precision score
precision = precision_score(test["Target"], preds)
print("Precision Score:", precision)

# Combine predictions with the target variable
combined = pd.concat([test["Target"], preds], axis=1)

# Define prediction function
def predict(train, test, predictors, model):
   pipeline.fit(train[predictors], train["Target"])
   preds = pipeline.predict_proba(test[predictors])[:, 1]
   preds[preds >= .6] = 1
   preds[preds < .6] = 0
   preds = pd.Series(preds, index=test.index, name="Predictions")
   combined = pd.concat([test["Target"], preds], axis=1)
   return combined

# Define backtesting function
# Define backtesting function
def backtest(data, model, predictors, horizons, start=2500, step=250):
   all_predictions = []
  
   for i in range(start, data.shape[0], step):
       train = data.iloc[0:i].copy()
       test = data.iloc[i:(i+step)].copy()

       for horizon in horizons:
           rolling_averages_train = train["Close"].rolling(horizon).mean()
           rolling_averages_test = test["Close"].rolling(horizon).mean()

           ratio_column = f"Close_Ratio_{horizon}"
           train[ratio_column] = train["Close"] / rolling_averages_train
           test[ratio_column] = test["Close"] / rolling_averages_test

           trend_column = f"Trend_{horizon}"
           train[trend_column] = train.shift(1).rolling(horizon).sum()["Target"]
           test[trend_column] = test.shift(1).rolling(horizon).sum()["Target"]

       predictions = predict(train, test, predictors, model)
       all_predictions.append(predictions)
  
   return pd.concat(all_predictions)


# Define horizons for backtesting
horizons = [2, 5, 60, 250, 1000]

# Perform backtesting
new_predictors = predictors + [f"Close_Ratio_{horizon}" for horizon in horizons] + [f"Trend_{horizon}" for horizon in horizons]
predictions = backtest(data, pipeline, new_predictors, horizons)

# Evaluate precision score of backtesting results
backtest_precision = precision_score(predictions["Target"], predictions["Predictions"])
print("Backtest Precision Score:", backtest_precision)

"""

# Plot the actual values and predicted values
plt.figure(figsize=(12, 6))
plt.plot(combined.index, combined["Target"], label='Actual')
plt.plot(combined.index, combined[0], label='Predicted')
plt.xlabel('Date')
plt.ylabel('Target')
plt.title('Actual vs. Predicted Values')
plt.legend()
plt.show()

"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('AAPL-last-5-years.csv')

data = data[['Date', 'Close']]
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

X = pd.to_numeric(data.index).values.reshape(-1, 1)
y = data['Close'].values
lr_model = LinearRegression()
lr_model.fit(X, y)

plt.plot(data.index, data['Close'], label='Original Data')

plt.plot(data.index, lr_model.predict(X), label='Linear Trend')

plt.xlabel('Date')
plt.ylabel('Close Price')

plt.legend()
plt.grid()
plt.show()

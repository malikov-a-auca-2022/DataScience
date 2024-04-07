import pandas as pd
from autots import AutoTS
import joblib

data = pd.read_csv("AAPL-last-year-except-20.csv")
data = data[["Date", "Close"]]
data["Date"] = pd.to_datetime(data.Date)

model = AutoTS(forecast_length=20, frequency='infer',
               ensemble='simple')
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)

model_filepath = "model_author.pkl"
joblib.dump(model, model_filepath)
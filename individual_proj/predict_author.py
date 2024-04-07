import joblib

model = joblib.load('model_author.pkl')
prediction = model.predict()
forecast = prediction.forecast
print(forecast)
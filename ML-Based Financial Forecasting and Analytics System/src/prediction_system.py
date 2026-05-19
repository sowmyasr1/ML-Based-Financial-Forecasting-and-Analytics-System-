# src/prediction_system.py

from datetime import datetime, timedelta
import yfinance as yf
import pandas as pd
import joblib
import os

# ------------------------------
# 1. Load trained model
# ------------------------------
model_path = 'models/rf_model.pkl'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Trained model not found at {model_path}. "
                            f"Please run model training first.")

model = joblib.load(model_path)

# ------------------------------
# 2. Define features and ticker
# ------------------------------
features = ['Open', 'High', 'Low', 'Volume', 'Dividends', 
            'Stock Splits', 'MA_20', 'MA_50', 'Daily_Return', 'Volatility']
ticker = 'KO'  # Coca-Cola
start_date = (datetime.today() - timedelta(days=180)).strftime('%Y-%m-%d')  # last 6 months
end_date = datetime.today().strftime('%Y-%m-%d')
# ------------------------------
# 3. Fetch latest stock data (1-minute intervals)
# ------------------------------

live_data = yf.download(ticker, start=start_date, end=end_date, interval='1d')
# ------------------------------
# 4. Feature engineering
# ------------------------------
live_data['MA_20'] = live_data['Close'].rolling(window=20).mean()
live_data['MA_50'] = live_data['Close'].rolling(window=50).mean()
live_data['Daily_Return'] = live_data['Close'].pct_change()
live_data['Volatility'] = live_data['Daily_Return'].rolling(window=20).std()

# Add missing columns if not present (Dividends & Stock Splits)
for col in ['Dividends', 'Stock Splits']:
    if col not in live_data.columns:
        live_data[col] = 0

# Fill missing values
live_data.fillna(0, inplace=True)

# ------------------------------
# 5. Prepare latest data point for prediction
# ------------------------------
latest_features = live_data[features].iloc[-1:].dropna()

# ------------------------------
# 6. Predict closing price
# ------------------------------
if latest_features.empty:
    print("No valid data available for live prediction.")
else:
    live_prediction = model.predict(latest_features)
    print(f"Predicted Closing Price: {live_prediction[0]:.2f}")

# src/model_training.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

# 1 Load cleaned and feature-engineered dataset
data = pd.read_csv("data/processed/KO_stock_features.csv")
data['Date'] = pd.to_datetime(data['Date'])

# 2 Define features and target
features = ['Open', 'High', 'Low', 'Volume', 'Dividends',
            'Stock Splits', 'MA_20', 'MA_50', 'Daily_Return', 'Volatility']
target = 'Close'

X = data[features]
y = data[target]

# 3 Train-test split (time-series-aware)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=False
)

# 4 Initialize and train Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5 Predict on test set
y_pred = model.predict(X_test)

# 6 Evaluate
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")

#  Model is ready for further tuning or saving


# Save the trained model
import os
import joblib
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/rf_model.pkl")
print("Trained model saved as models/rf_model.pkl")
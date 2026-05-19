# src/data_splitting.py

import pandas as pd
from sklearn.model_selection import train_test_split

# 1 Load cleaned and feature-engineered dataset
data = pd.read_csv("data/processed/KO_stock_features.csv")

# Ensure Date is datetime type (optional, useful for plotting later)
data['Date'] = pd.to_datetime(data['Date'])

# 2 Define features and target
features = ['Open', 'High', 'Low', 'Volume', 'Dividends',
            'Stock Splits', 'MA_20', 'MA_50', 'Daily_Return', 'Volatility']
target = 'Close'

X = data[features]
y = data[target]

# 3 Train-test split (80% train, 20% test, no shuffle for time series)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=False
)

# 4 Print shapes to confirm
print("Shapes after train-test split:")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

#  Now the data is ready for model training

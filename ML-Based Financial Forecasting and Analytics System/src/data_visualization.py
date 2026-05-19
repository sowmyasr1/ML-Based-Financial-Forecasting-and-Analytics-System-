import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned & feature-engineered data
data = pd.read_csv("data/processed/KO_stock_features.csv")

# Convert Date to datetime type for proper plotting
data['Date'] = pd.to_datetime(data['Date'])

# 1 Line plot for stock prices with moving averages
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Close'], label='Close Price')
plt.plot(data['Date'], data['MA_20'], label='MA 20', linestyle='--')
plt.plot(data['Date'], data['MA_50'], label='MA 50', linestyle='--')
plt.title('Coca-Cola Stock Prices with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# 2 Correlation heatmap (only numeric columns)
numeric_data = data.select_dtypes(include='number')  # exclude Date
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

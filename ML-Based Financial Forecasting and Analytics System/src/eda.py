import pandas as pd

# Load feature-engineered data
data = pd.read_csv("data/processed/KO_stock_features.csv")

# 1 Number of records and date range
num_records = len(data)
print(f"Number of records: {num_records}")
print(f"Start date: {data['Date'].iloc[0]}")
print(f"End date: {data['Date'].iloc[-1]}")


# 2 Summary statistics
print("=== Summary Statistics ===")
print(data.describe())

# Select only numeric columns for correlation
numeric_data = data.select_dtypes(include='number')

# 3 Correlation matrix
print("\n=== Correlation Matrix ===")
print(numeric_data.corr())

# 4 Head of the dataset
print("\n=== First 5 Rows ===")
print(data.head())

# 5 Tail of the dataset
print("\n=== Last 5 Rows ===")
print(data.tail())


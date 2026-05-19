import pandas as pd
import os

def feature_engineering():
    input_file = "data/processed/KO_stock_history_clean.csv"
    output_file = "data/processed/KO_stock_features.csv"

    if not os.path.exists(input_file):
        print(f"File {input_file} not found.")
        return

    data = pd.read_csv(input_file)

    # Moving Averages
    data['MA_20'] = data['Close'].rolling(window=20).mean()
    data['MA_50'] = data['Close'].rolling(window=50).mean()

    # Daily Returns
    data['Daily_Return'] = data['Close'].pct_change()

    # Volatility (20-day rolling std dev of returns)
    data['Volatility'] = data['Daily_Return'].rolling(window=20).std()

    # Drop NA caused by rolling
    data.dropna(inplace=True)

    data.to_csv(output_file, index=False)
    print(f"Feature engineered data saved: {output_file}")
    print(data.head())

if __name__ == "__main__":
    feature_engineering()

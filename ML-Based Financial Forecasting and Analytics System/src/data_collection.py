import yfinance as yf
import pandas as pd
import os

def collect_data():
    ticker = "KO"
    stock = yf.Ticker(ticker)

    os.makedirs("data/raw", exist_ok=True)

    # Historical price data
    stock.history(period="10y").to_csv("data/raw/KO_stock_history.csv")

    # Dividends
    stock.dividends.to_csv("data/raw/KO_dividends.csv")

    # Splits
    stock.splits.to_csv("data/raw/KO_splits.csv")

    # Info (metadata)
    pd.DataFrame([stock.info]).to_csv("data/raw/KO_info.csv", index=False)

    print("KO data collected and saved in data/raw/")

if __name__ == "__main__":
    collect_data()

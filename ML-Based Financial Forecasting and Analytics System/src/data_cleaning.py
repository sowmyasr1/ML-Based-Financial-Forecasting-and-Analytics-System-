import pandas as pd
import os

def clean_file(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Skipping {input_file}, file not found.")
        return
    
    data = pd.read_csv(input_file)
    print(f"\nCleaning {input_file} ...")
    print("Missing values BEFORE:\n", data.isna().sum())

    # Forward-fill missing values
    data.ffill(inplace=True)

    print("Missing values AFTER:\n", data.isna().sum())

    os.makedirs("data/processed", exist_ok=True)
    data.to_csv(output_file, index=False)
    print(f"Saved cleaned file: {output_file}")

def clean_data():
    clean_file("data/raw/KO_stock_history.csv", "data/processed/KO_stock_history_clean.csv")
    clean_file("data/raw/KO_dividends.csv", "data/processed/KO_dividends_clean.csv")
    clean_file("data/raw/KO_splits.csv", "data/processed/KO_splits_clean.csv")
    clean_file("data/raw/KO_info.csv", "data/processed/KO_info_clean.csv")

if __name__ == "__main__":
    clean_data()

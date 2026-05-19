# # Coca-Cola Stock Price Prediction

A machine learning project that predicts **Coca-Cola stock prices** using historical data, feature engineering, and a trained Random Forest model.  
The project includes a **Streamlit web app** for making predictions interactively.  


##  Project Structure

├── .venv/ # Virtual environment

├── data/

│ ├── raw/ # Raw stock price data (CSV files)

│ ├── processed/ # Processed/cleaned data

├── images/ # Plots (stock price trends, correlation heatmaps, etc.)

├── models/

│ └── rf_model.pkl # Trained Random Forest model

├── src/ # Source code

│ ├── data_collection.py

│ ├── data_cleaning.py

│ ├── eda.py

│ ├── feature_engineering.py

│ ├── model_training.py

│ ├── prediction_system.py

│ ├── train_test_split.py

│ └── data_visualization.py

├── app.py # Streamlit web app

├── requirements.txt # Project dependencies

├── README.md # Project documentation

└── .gitignore # Files/folders ignored by Git


---

##  Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd coca-cola-stock-prediction
   ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    .venv/Scripts/activate     # On Windows
    source .venv/bin/activate  # On Mac/Linux
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**
    ```bash
    streamlit run app.py
    ```

## Features
 - Data collection and preprocessing of Coca-Cola stock data
 - Exploratory Data Analysis (EDA) with visualizations
 - Feature engineering and model training
 - Random Forest model for stock price prediction
 - Interactive Streamlit app for predictions

## Demo
 - Enter stock-related features (like Open, High, Low, Volume, etc.)
 - Get an instant prediction of Coca-Cola stock price

## Tech Stack
 - Python
 - Pandas, NumPy, Scikit-learn
 - Matplotlib, Seaborn
 - Streamlit

## Future Improvements
 - Experiment with LSTM/Deep Learning models
 - Deploy the app to Streamlit Cloud / Render / Heroku
 - Improve feature set with external factors (market indicators, news sentiment)

## Author
 - Varsha Reddy

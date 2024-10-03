import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

def train_regression_model(ticker):
    data = pd.read_csv("data/stock_data.csv")

    # Filter by ticker 
    ticker_data = data[data["ticker"] == ticker]
    if ticker_data.empty:
        print(f"There is no data for ticker: {ticker}")
        return
    
    X = ticker_data[["open", "high", "low", "volume"]]  # Features
    y = ticker_data["close"]  # Target variable
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X, y)
    
    # Save the model
    with open(f"models/{ticker}_regression_model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    train_regression_model("AHH")

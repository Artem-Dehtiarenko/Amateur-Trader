from src.download_data import download_data
from src.preprocess_data import preprocess_data
from src.train_model import train_model
from src.evaluate_model import evaluate_model

if __name__ == "__main__":
    tickers = ["AHH", "APO"]

    # Download data for each ticker
    for ticker in tickers:
        download_data(ticker)

        # Preprocess data for each ticker
        preprocess_data()

        # Train regression model for each ticker
        train_model(ticker)

        # Evaluate model for each ticker
      
        #print(f"Evaluating model for ticker: {ticker}")
        evaluate_model(ticker)
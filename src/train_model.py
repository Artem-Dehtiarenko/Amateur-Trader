import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

def train_model(ticker):
    # Define paths
    data_path = f"data/{ticker}/processed/{ticker}_processed.csv"
    model_dir = f"models/{ticker}"

    # Create the model directory if it does not exist
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)

    # Load processed data
    data = pd.read_csv(data_path)

    # Assuming 'Close' is your target variable
    target_column = 'Close'
    
    # Drop the target column and any non-numeric columns from the features
    X = data.drop(columns=[target_column])  # Drop target column
    X = X.select_dtypes(exclude=['object'])  # Exclude non-numeric columns
    y = data[target_column]

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Save the model
    model_path = f"{model_dir}/{ticker}_model.pkl"
    joblib.dump(model, model_path)

    print(f"Model trained for {ticker} and saved to {model_path}")

if __name__ == "__main__":
    tickers = ["AHH", "APO"]  # Add more tickers if needed
    for ticker in tickers:
        train_model(ticker)

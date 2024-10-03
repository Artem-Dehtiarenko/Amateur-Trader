import pandas as pd
from sklearn.linear_model import LinearRegression
from src.evaluation_metrics import calculate_regression_metrics

def evaluate_model(ticker):
    # Define the file path for the stock data based on the ticker symbol
    file_path = f'data/{ticker}/{ticker}_stock_data.csv'
    
    # Load the stock data into a DataFrame
    data = pd.read_csv(file_path)

    # Prepare data for regression by creating an adjusted close price column
    data['adj_close'] = data['Close'].shift(-1)  # Use the correct column name
    data.dropna(inplace=True)  # Remove rows with NaN values

    # Define features (X) and target variable (y) for the regression model
    X = data[['Close']]  # Use the correct column name
    y = data['adj_close']

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Make predictions using the trained model
    y_pred = model.predict(X)

    # Calculate evaluation metrics using the actual and predicted values
    metrics = calculate_regression_metrics(y, y_pred)
    print(f"Evaluation Metrics for {ticker}:", metrics)

if __name__ == "__main__":
    # List of ticker symbols to evaluate
    tickers = ['AHH', 'APO']
    for ticker in tickers:
        evaluate_model(ticker)  # Evaluate the model for each ticker

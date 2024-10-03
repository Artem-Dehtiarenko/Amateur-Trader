import pandas as pd
import os

def preprocess_data():
    # List of ticker symbols to process
    tickers = ['AHH', 'APO']

    for ticker in tickers:
        # Define the output directory for processed data
        output_dir = f'data/{ticker}/processed'
        os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

        # Define the input file path for the stock data
        input_file = f'data/{ticker}/{ticker}_stock_data.csv'
        
        try:
            # Load the stock data into a DataFrame
            data = pd.read_csv(input_file)
            print(f"Columns in {input_file}: {data.columns.tolist()}")  # Display column names
        except FileNotFoundError:
            # Handle the case where the input file is not found
            print(f"Error: file {input_file} not found.")
            continue

        # Check if the 'Close' column exists in the DataFrame
        if 'Close' not in data.columns:
            print(f"Error: 'Close' column not found in {ticker} data.")
            continue

        # Process the data by creating an adjusted close price column
        data['adj_close'] = data['Close'].shift(-1)  # Shift the close prices to create adjusted close
        data.dropna(inplace=True)  # Remove rows with NaN values

        # Define the output file path for the processed data
        output_file = os.path.join(output_dir, f'{ticker}_processed.csv')
        data.to_csv(output_file, index=False)  # Save the processed data to a CSV file
        
        print(f"Processed data for {ticker} saved to {output_file}")  # Confirmation message

if __name__ == "__main__":
    preprocess_data()  # Execute the data preprocessing function

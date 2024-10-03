import pandas as pd
import yfinance as yf

def download_data(ticker):
    # Download stock data
    data = yf.download(ticker, start="2010-01-01", end="2018-01-01")
    return data

# Download data for both tickers
ahh_data = download_data("AHH")
ap_data = download_data("APO")

# Save the data
ahh_data.to_csv("data/AHH/AHH_stock_data.csv")
ap_data.to_csv("data/APO/APO_stock_data.csv")

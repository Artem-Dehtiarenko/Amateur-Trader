import pandas as pd
from sklearn.metrics import (mean_squared_error, mean_absolute_error, 
                             accuracy_score, precision_score, 
                             recall_score, f1_score)

# Function to calculate regression metrics
def calculate_regression_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    return {"MSE": mse, "MAE": mae}

# Function to calculate classification metrics
def calculate_classification_metrics(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    return {"Accuracy": accuracy, "Precision": precision, 
            "Recall": recall, "F1-Score": f1}

if __name__ == "__main__":
    file_path = 'data/stock_data.csv'  
    data = pd.read_csv(file_path)

    # Example data for regression
    data['adj_close'] = data['close'].shift(-1)  # Use "Close" column
    data.dropna(inplace=True)

    # Example data for regression
    X_regression = data[['close']].values.reshape(-1, 1)
    y_regression = data['adj_close'].values

    # Example usage of regression metrics
    from sklearn.linear_model import LinearRegression
    regression_model = LinearRegression()
    regression_model.fit(X_regression, y_regression)
    y_pred_regression = regression_model.predict(X_regression)
    regression_metrics = calculate_regression_metrics(y_regression, y_pred_regression)
    print("Regression Metrics:", regression_metrics)

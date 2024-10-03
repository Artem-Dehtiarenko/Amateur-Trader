import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pickle
import os

# Load the stock data from CSV
data = pd.read_csv("data/stock_data.csv")

# Create target variable: 1 if the next day's closing price is higher, else 0
data['Price_Direction'] = (data['close'].shift(-1) > data['close']).astype(int)  # 1 if price goes up, else 0
data.dropna(inplace=True)  # Remove rows with NaN values

# Features for the classification model
X = data[["open", "high", "low", "volume"]]  # Features
y = data["Price_Direction"]  # Target variable

# Create and train the model
model = LogisticRegression()
model.fit(X, y)

# Save the trained model to a file
with open(f"models/AHH_classification_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Evaluate the model on the training data
y_pred = model.predict(X)

# Calculate metrics
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

# Print classification metrics
print("Classification Metrics:")
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# Main entry point of the script
if __name__ == "__main__":
    pass 

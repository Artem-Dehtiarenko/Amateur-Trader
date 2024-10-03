def define_target_variables():
    target_variables = {
        "Regression": "Predicting the stock price 7 days ahead.",
        "Klassifikation": "Predicting whether the stock price will rise the next day.",
        "Trend Prediction": "Determining whether the stock price trend will be rising, falling, or stable."
    }
    return target_variables

if __name__ == "__main__":
    targets = define_target_variables()
    for task, target in targets.items():
        print(f"{task} Ziel: {target}")

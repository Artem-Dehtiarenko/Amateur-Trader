def define_problems():
    problems = {
        "Stock Price Prediction": {
            "Problem Type": "Regression",
            "Description": "Predicting the stock price 7 days ahead."
        },
        "Price Direction Prediction": {
            "Problem Type": "Classification",
            "Description": "Predicting whether the stock price will rise or fall the next day."
        },
        "Trend Prediction": {
            "Problem Type": "Trend Prediction",
            "Description": "Determining the trend (rising, falling, or stable) for a given period."
        }
    }
    return problems

if __name__ == "__main__":
    problem_definitions = define_problems()
    for problem, details in problem_definitions.items():
        print(f"{problem}: {details}")

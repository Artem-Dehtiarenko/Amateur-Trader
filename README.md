# Aktienprognose
## Overview
This project focuses on predicting stock prices using machine learning techniques. The goal is to develop a reliable ML-based application that can assist amateur traders in making informed decisions. The project includes regression, classification, and trend prediction problems, demonstrating ML pipelines using DVC and Docker.

## Diagrams
Two diagrams were created to illustrate the project’s workflow and interactions:

- **Activity Diagram**: This diagram provides a visual representation of the workflow for training and evaluating the classification model. It outlines the key steps involved, such as data loading, preprocessing, model training, and evaluation. By following this diagram, stakeholders can understand the sequence of actions taken during model development and how data flows through the system.

- **Use Case Diagram**: This diagram illustrates the different use cases of the application and the interactions between users (traders) and the system. It captures the main functionalities provided by the project, such as data input, model training, and performance evaluation. This helps to clarify the roles of users and the expected outcomes of using the application.

## Project Structure

.aktienprognose
- **data/**
  - **AHH/**
    - AHH_stock_data.csv
    - **processed/**
      - AHH_processed_data.csv
  - **APO/**
    - APO_stock_data.csv
    - **processed/**
      - APO_processed_data.csv
- **src/**
  - preprocessing.py
  - evaluation_metrics.py
  - train_classification_model.py
  - evaluate_model.py
- **models/**
  - trained_model.pkl
- **Dockerfile**
- **requirements.txt**
- **README.md**
     
          


File Descriptions

        •download_data.py: Downloads historical stock data for tickers and saves it as CSV files in the appropriate directories.
        •evaluate_model.py: Evaluates regression models using metrics such as Mean Squared Error (MSE) and Mean Absolute Error (MAE) for each ticker.
        •evaluation_metrics.py: Contains functions for calculating evaluation metrics for both regression and classification tasks.
        •input_data.py: Defines input data structures, including historical stock prices and relevant economic indicators.
        •preprocess_data.py: Handles data preprocessing tasks, such as creating adjusted close prices, cleaning the data, and saving the processed results.
        •problem_definition.py: Outlines the machine learning tasks involved in the project, including regression, classification, and trend prediction.
        •target_variables.py: Defines the target variables that will be used for each machine learning task.
        •train_classification_model.py: Trains a classification model that predicts the direction of stock prices (whether the price will go up or down).
        •train_model.py: Trains a regression model based on processed data for each individual ticker.
        •train_regression_model.py: Trains and saves a regression model using a general dataset that is not specific to any particular ticker.
        •main.py: Serves as the main orchestration script that coordinates the entire workflow.
        •requirements.txt: Lists all the Python libraries and dependencies needed to run the project.
        •dvc.yaml: Describes the stages of the DVC pipeline, detailing the processes for loading data, preprocessing it, and training the models.
        •Dockerfile: Specifies the configuration for the Docker image that will be used to run the DVC pipeline in a containerized environment.


How to Run the Project
To run the project, you can follow these steps:
        1.Set Up Environment: Ensure you have Python installed, along with the required libraries. You can install the dependencies using:
                pip install -r requirements.txt
        2.Use DVC for Data Management: To use DVC for tracking your data pipeline, initialize DVC in your project:
                dvc init
        3.After that, you can run the DVC pipeline to load and preprocess data:
                dvc repro
        4.Run the Main Script: Execute the main script to coordinate all stages:
                python src/main.py
This will execute the entire workflow, including downloading data, preprocessing, training models, and evaluating their performance.

# download data
https://drive.google.com/file/d/1GO4j74B3y2zNuL7up1XRFZepmH3gvpJM/view?usp=sharing

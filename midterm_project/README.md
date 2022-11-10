# ML Zoomcamp Mid-Term Project: Travel Insurance Customer Classifier

This repository conatins my MLzoomcamp Midterm Project which is currently being taught by Alexey Grigorev and you can learn more about the free course by following the link [here](https://github.com/alexeygrigorev/mlbookcamp-code).

## The Problem
A Tour & Travels company is offering some if it customers a Travel Insurance Package and requires an intelligent model be built that will predict if a customer will be interested to buy The Travel Insurance Package based on certain parameters. The given data has been extracted from the performance/sales of the Package in 2019.

## The Data
The [data](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data) provided contains almost 2000 of its previous customers based on its database history and was made available on [Kaggle](https://www.kaggle.com/datasets/tejashvi14/travel-insurance-prediction-data) by TEJASHVI and last updated about a year ago.

## The model
The best model was selected from the following:
 * Decision Tree
 * Random Forest
 * XGBoost

The baseline models were built without without scaling the data applying Eensemble modeles and the best model was selected afterwards.

## The metrics
The metrics involved include Confusion Matrix And Scores Of Accuracy, Recall, Precision And F1-Score.

## The Notebook 
 * EDA.ipynb
    * Performs an exploratory data analysis
    * Feature importance analysis
 * modeling.ipynb 
    * Encodes categorical features
    * Allows to build, select and evaluate models
    * Performs model hyperparameter tuning
    * Saves the selected model using BentoML

## Script
 * model.py 
    * Loading the model
    * Serving it via a web serice (BentoML)
 * locustfile.py
    * Model simulation of millions of simultaneous users

## Files with dependencies
 * bentofile.yaml
    * Containerize the packages
 * bentomlconfiguration.yaml
    * For specifiying the Batch Size
    * For specifiying the Latency Period

## Deployment
 * AWS Elastic Container Registry
    * Store the Docker container
 * AWS Elastic Container Service 
    * Run the model in cloud

You can access the model using this API 23.20.98.64:3000

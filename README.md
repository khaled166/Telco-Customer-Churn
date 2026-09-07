# Telco Customer Churn Prediction

A machine learning pipeline that predicts whether a telecom customer is likely to churn, based on account, service, and billing attributes. Includes exploratory analysis, model training, and a lightweight app for making predictions on new customer data.

## Problem

Customer churn is one of the most expensive problems in subscription-based businesses — acquiring a new customer typically costs far more than retaining an existing one. This project builds a classification model that flags at-risk customers so retention efforts (offers, outreach, support) can be targeted before they cancel.

## Approach

1. **Exploratory Data Analysis** (`Telco Customer Churn.ipynb`) — examined churn distribution, key drivers (contract type, tenure, monthly charges, service subscriptions), and class imbalance.
2. **Feature Engineering & Preprocessing** — encoded categorical variables, handled missing values, and prepared the feature set for modeling.
3. **Model Training** — trained and evaluated classification models, selecting the best performer based on precision/recall tradeoffs relevant to a retention use case (catching likely churners matters more than raw accuracy on this kind of imbalanced problem).
4. **Serialization** — saved the trained model (`Model.pkl`) and the input preprocessing pipeline (`Inputs.pkl`) for reuse without retraining.
5. **Prediction App** (`Customer_Churn_App.py`) — a simple app that loads the saved model and pipeline to generate churn predictions on new customer records.

## Repository Contents

| File | Description |
|---|---|
| `Telco Customer Churn.ipynb` | Full analysis: EDA, feature engineering, model training and evaluation |
| `Customer_Churn_App.py` | Application script for running predictions using the trained model |
| `Model.pkl` | Serialized trained classification model |
| `Inputs.pkl` | Serialized preprocessing pipeline for input features |
| `requirements.txt` | Python dependencies |

## Tech Stack

`Python` `Pandas` `scikit-learn` `Jupyter Notebook`

## Running Locally

```bash
pip install -r requirements.txt
python Customer_Churn_App.py
```

## Key Takeaways

- Contract type, tenure, and monthly charges were among the strongest predictors of churn.
- Model evaluation prioritized recall on the churn class to minimize missed at-risk customers, given the business cost of false negatives in a retention context.

## Possible Extensions

- Add SHAP-based explainability to surface *why* a given customer is flagged as high-risk
- Deploy as a REST API (FastAPI) instead of a script-based app
- Track experiments and model versions with MLflow

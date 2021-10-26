## Credit Card Approval

### Summary

Description: Predict credit card approvals and risk scores

Tags: credit, finance, risk

Language: Python

Framework: scikit-learn

Model Type: Gradient boosting classifier

GitHub Link: https://github.com/algorithmiaio/demos/tree/master/credit-card-approval

Demo Link: https://demo.productionize.ai/algorithms/AlgorithmiaSE/CreditCardApproval

### Overview

Given information about a customer from their credit card application, the model
returns whether or not the customer is approved for a credit card and a credit
risk score.

A high risk level is associated with past customers who were 60 days or more
overdue on their payments.

### Inputs

The input parameters include details about age, occupation, family size,
housing, marital status, and education level.

### Outputs

The model returns an `approved` value equal to 1 if the credit card is approved,
and a value equal to 0 if the credit card is denied.

The model returns a credit `risk_score` with a value between 0 and 1. A higher
score indicates that the customer presents a high credit risk. A lower score
indicates that the customer presents a low credit risk.

### Model versions

Model version A was trained using a gradient boosting classifier in
scikit-learn.

Model version B was trained using a random forest classifier in scikit-learn.

### Feature importance

A plot of feature importance for model version A (gradient boosting classifier)
is shown below:

![Feature Importance](https://algosales.productionize.ai/v1/data/algorithmia_se/CreditCardApproval/features-a.png)

A plot of feature importance for model version B (random forest classifier) is
shown below:

![Feature importance](https://algosales.productionize.ai/v1/data/algorithmia_se/CreditCardApproval/features-b.png)

## Example queries

### Approved credit card

Input:

```
{
  "high_balance": 0,
  "owns_home": 1,
  "child_one": 0,
  "child_two_plus": 0,
  "has_work_phone": 0,
  "age_high": 0,
  "age_highest": 1,
  "age_low": 0,
  "age_lowest": 0,
  "employment_duration_high": 0,
  "employment_duration_highest": 0,
  "employment_duration_low": 0,
  "employment_duration_medium": 0,
  "occupation_hightech": 0,
  "occupation_office": 1,
  "family_size_one": 1,
  "family_size_three_plus": 0,
  "housing_coop_apartment": 0,
  "housing_municipal_apartment": 0,
  "housing_office_apartment": 0,
  "housing_rented_apartment": 0,
  "housing_with_parents": 0,
  "education_higher_education": 0,
  "education_incomplete_higher": 0,
  "education_lower_secondary": 0,
  "marital_civil_marriage": 0,
  "marital_separated": 0,
  "marital_single_not_married": 1,
  "marital_widow": 0
}
```

Output:

```
{
  "approved": 1,
  "risk_score": 0.08
}
```

### Denied credit card

Input:

```
{
  "high_balance": 0,
  "owns_home": 1,
  "child_one": 0,
  "child_two_plus": 0,
  "has_work_phone": 0,
  "age_high": 0,
  "age_highest": 0,
  "age_low": 0,
  "age_lowest": 0.25,
  "employment_duration_high": 0,
  "employment_duration_highest": 0,
  "employment_duration_low": 0,
  "employment_duration_medium": 0,
  "occupation_hightech": 0,
  "occupation_office": 0,
  "family_size_one": 1,
  "family_size_three_plus": 0,
  "housing_coop_apartment": 0,
  "housing_municipal_apartment": 0,
  "housing_office_apartment": 0,
  "housing_rented_apartment": 0,
  "housing_with_parents": 0,
  "education_higher_education": 1,
  "education_incomplete_higher": 0,
  "education_lower_secondary": 0,
  "marital_civil_marriage": 0,
  "marital_separated": 0,
  "marital_single_not_married": 0,
  "marital_widow": 0
}
```

Output:

```
{
  "approved": 0,
  "risk_score": 0.77
}
```

## Usage

### Input parameters

| Parameter                   |
| --------------------------- |
| high_balance                |
| owns_home                   |
| child_one                   |
| child_two_plus              |
| has_work_phone              |
| age_high                    |
| age_highest                 |
| age_low                     |
| age_lowest                  |
| employment_duration_high    |
| employment_duration_highest |
| employment_duration_low     |
| employment_duration_medium  |
| occupation_hightech         |
| occupation_office           |
| family_size_one             |
| family_size_three_plus      |
| housing_coop_apartment      |
| housing_municipal_apartment |
| housing_office_apartment    |
| housing_rented_apartment    |
| housing_with_parents        |
| education_higher_education  |
| education_incomplete_higher |
| education_lower_secondary   |
| marital_civil_marriage      |
| marital_separated           |
| marital_single_not_married  |
| marital_widow               |

### Output parameters

| Parameter      | Description                                               |
| -------------- | --------------------------------------------------------- |
| approved       | Whether or not a credit card is approved for the customer |
| risk_score     | Probability of being classified as high-risk credit       |

## Preparatory work

### Prepare data

Downloaded data files from https://www.kaggle.com/rikdifos/credit-card-approval-prediction:

* application_record.csv
* credit_record.csv

and place them in a hosted data collection, `AlgorithmiaSE/CreditCardApproval`
in this case.

The `prepare.py` script was then used to prepare the data.

### Train model

The `train-a.ipynb` and `train-b.ipynb` notebooks were used to train a gradient
boosting classifier and a random forest classifier, respectively, using
scikit-learn.

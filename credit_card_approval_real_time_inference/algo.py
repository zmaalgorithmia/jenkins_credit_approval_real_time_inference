import Algorithmia
import numpy as np
import time
from joblib import load


client = Algorithmia.client()

# Model version A - Gradient boosting classifier
model = load(client.file(
    "data://zma/credit_card_approval/model-a.joblib").getFile().name)

# Model version B - Random forrest classifier
# model = load(client.file(
#     "data://zma/credit_card_approval/model-b.joblib").getFile().name)


def apply(input):

    ##########################
    # Processing input data #
    ##########################
    params = np.array(
        [
            input.get("high_balance", 0),
            input.get("owns_home", 1),
            input.get("child_one", 0),
            input.get("child_two_plus", 0),
            input.get("has_work_phone", 0),
            input.get("age_high", 0),
            input.get("age_highest", 1),
            input.get("age_low", 0),
            input.get("age_lowest", 0),
            input.get("employment_duration_high", 0),
            input.get("employment_duration_highest", 0),
            input.get("employment_duration_low", 0),
            input.get("employment_duration_medium", 0),
            input.get("occupation_hightech", 0),
            input.get("occupation_office", 1),
            input.get("family_size_one", 1),
            input.get("family_size_three_plus", 0),
            input.get("housing_coop_apartment", 0),
            input.get("housing_municipal_apartment", 0),
            input.get("housing_office_apartment", 0),
            input.get("housing_rented_apartment", 0),
            input.get("housing_with_parents", 0),
            input.get("education_higher_education", 0),
            input.get("education_incomplete_higher", 0),
            input.get("education_lower_secondary", 0),
            input.get("marital_civil_marriage", 0),
            input.get("marital_separated", 0),
            input.get("marital_single_not_married", 1),
            input.get("marital_widow", 0),
        ]
    ).reshape(1, -1)

    ###########################################################
    # Inference on risk score and make decision on approval #
    ###########################################################
    risk_score = model.predict_proba(params)
    risk_score = round(float(risk_score[0][1]), 2)
    approved = int(1 - model.predict(params)[0])

    #####################################################
    # Stream inference metrics via Algorithmia Insights #
    #####################################################

    # Inference metrics for business users
    client.report_insights({"risk_score": risk_score, "approved": approved})

    # Inference metrics required by model risk organization (MRO)
    client.report_insights({"n_features": model.n_features_})

    # Inference metrics for data scientists
    client.report_insights({"owns_home": input.get(
        "owns_home", 1), "has_work_phone": input.get("has_work_phone", 0)})

    ##########################################################################################
    # Collect and store adverse action reasons, if credit card application has been declined #
    ##########################################################################################
    if approved != 1:
        adverse_action_reasons = {}

        employment = input.get("has_work_phone")

        if employment == None:
            adverse_action_reasons['unable_to_verfiy_employment'] = 1
        elif employment == 0:
            adverse_action_reasons['no employment'] = 1

        # Store adverse action reasons in built-in storage
        file_path = "data://zma/credit_card_approval/adverse_action_reasons_" + \
            str(time.time()) + ".json"
        client.file(file_path).putJson(adverse_action_reasons)

    #     # Store adverse action reasons on Google Cloud Storage
    #     file_path = "gs://algorithmia_gcp_bucket/Credit_Card_Approval_AAR/adverse_action_reasons_" + \
    #         str(time.time()) + ".json"
    #     client.file(file_path).putJson(adverse_action_reasons)

    ##########################################
    # Return output to consuming application #
    ##########################################
    return {"risk_score": risk_score, "approved": approved}

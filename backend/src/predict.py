import numpy as np
import joblib

# Load trained model
model = joblib.load("model/diabetes_model.pkl")


def predict_diabetes(data):

    # Encode Gender
    gender = 1 if data["Gender"] == "Male" else 0

    # Encode Physical Activity
    activity_map = {
        "Low": 1,
        "Moderate": 2,
        "High": 0
    }

    activity = activity_map[data["PhysicalActivity"]]

    features = np.array([[
        data["Age"],
        gender,
        data["BMI"],
        data["Glucose"],
        data["BloodPressure"],
        data["Insulin"],
        data["HbA1c"],
        data["Cholesterol"],
        data["FamilyHistory"],
        activity,
        data["Smoking"]
    ]])

    prediction = model.predict(features)[0]

    if prediction == 1:
        return "Diabetic"

    else:
        return "Not Diabetic"
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import os

def load_data():

    current_dir = os.path.dirname(__file__)

    dataset_path = os.path.join(
        current_dir,
        "..",
        "data",
        "Diabetes.csv"
    )

    df = pd.read_csv(".\\backend\\data\\diabetes.csv")

    # Encode Gender
    gender_encoder = LabelEncoder()
    df["Gender"] = gender_encoder.fit_transform(df["Gender"])

    # Encode Physical Activity
    activity_encoder = LabelEncoder()
    df["PhysicalActivity"] = activity_encoder.fit_transform(
        df["PhysicalActivity"]
    )

    # Features
    X = df.drop("Diabetes", axis=1)

    # Target
    y = df["Diabetes"]

    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
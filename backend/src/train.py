from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

from preprocess import load_data

# Load dataset
X_train, X_test, y_train, y_test = load_data()

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

# Current directory
current_dir = os.path.dirname(__file__)

# Model save path
model_path = os.path.join(
    current_dir,
    "..",
    "model",
    "diabetes_model.pkl"
)

# Save model
joblib.dump(model, model_path)

print("Model saved successfully!")
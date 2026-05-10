from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from src.predict import predict_diabetes

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():

    return "Diabetes Prediction API Running"


@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Receive data from frontend
        data = request.get_json()

        # Get prediction
        result = predict_diabetes(data)

        # Send response
        return jsonify({
            "prediction": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":

    # Render dynamic port
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
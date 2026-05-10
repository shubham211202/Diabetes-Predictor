from flask import Flask, request, jsonify
from flask_cors import CORS

from src.predict import predict_diabetes

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Diabetes Prediction API Running"


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Receive JSON data from frontend
        data = request.get_json()

        # Get prediction result
        result = predict_diabetes(data)

        # Return response
        return jsonify({
            "prediction": result
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)
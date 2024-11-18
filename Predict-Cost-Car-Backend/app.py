from flask import Flask, request, jsonify
from joblib import load
import numpy as np

app = Flask(__name__)

knn_model = load('model/knn_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'performance' not in data or 'energy_consumed' not in data:
        return jsonify({"error": "Dữ liệu không hợp lệ. Cần có 'performance' và 'energy_consumed'."}), 400

    X_input = np.array([[data['performance'], data['energy_consumed']]])

    prediction = knn_model.predict(X_input)[0]
    return jsonify({"predicted_cost": prediction})

if __name__ == '__main__':
    app.run(debug=True)

"""app.py
Simple Flask API that loads the trained model and returns predictions for incoming JSON payloads.
Run after training ai_model.py to create models/rf_predictive_maintenance.pkl
"""
from flask import Flask, request, jsonify
import joblib
import os
import numpy as np

app = Flask(__name__)
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'rf_predictive_maintenance.pkl')

model = None
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    print('Warning: model file not found. Train the model with src/ai_model.py')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    try:
        temp = float(data['temperature'])
        vib = float(data['vibration'])
        curr = float(data['current'])
    except Exception as e:
        return jsonify({'error': 'invalid input', 'details': str(e)}), 400
    if model is None:
        return jsonify({'error': 'model not available. Train first.'}), 500
    X = np.array([[temp, vib, curr]])
    pred = model.predict(X)[0]
    prob = float(model.predict_proba(X)[0,1]) if hasattr(model, 'predict_proba') else None
    return jsonify({'prediction': int(pred), 'failure_probability': prob})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

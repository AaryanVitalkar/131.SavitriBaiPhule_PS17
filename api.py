from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load Model
if os.path.exists('risk_model.pkl'):
    try:
        model = joblib.load('risk_model.pkl')
        print("✅ Model loaded successfully!")
    except:
        model = None
else:
    print("❌ 'risk_model.pkl' not found. Run train_model.py first.")
    model = None

@app.route('/predict_risk', methods=['POST'])
def predict():
    if not model:
        return jsonify({"status": "error", "message": "Model not loaded"})

    try:
        data = request.json
        print(f"📩 Input: {data}")

        # Features must match train_model.py exactly
        features = [
            float(data.get('attendance', 0)),
            float(data.get('marks', 0)),
            int(data.get('backlogs', 0)),
            float(data.get('hours', 0)),
            int(data.get('failures', 0)),
            int(data.get('year', 1)),
            int(data.get('skills', 1))
        ]

        # Predict
        input_vector = np.array([features])
        prediction = model.predict(input_vector)[0]
        confidence = float(model.predict_proba(input_vector).max())

        return jsonify({
            "status": "success",
            "risk_level": prediction,
            "confidence_score": round(confidence * 100, 2)
        })

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    print("🚀 API running on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)
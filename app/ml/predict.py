import joblib
import pandas as pd
import os

MODEL_PATH = "app/ml/model.pkl"
SCALER_PATH = "app/ml/scaler.pkl"

# ------------------- AUTO LOAD / TRAIN -------------------
def load_model():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        print("⚠️ Model not found. Training model...")
        from app.ml.train import train_model
        train_model()

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    return model, scaler


model, scaler = load_model()

# ------------------- PREDICT FUNCTION -------------------
def predict_risk(features):
    feature_names = ["failures", "avg_response_time", "error_rate", "high_severity_bugs"]

    df = pd.DataFrame([features], columns=feature_names)

    features_scaled = scaler.transform(df)

    prediction = model.predict(features_scaled)[0]
    probability = model.predict_proba(features_scaled)[0][1]

    print("Features:", features)
    print("Prediction:", prediction, "Prob:", probability)

    return {
        "risk": int(prediction),
        "risk_score": float(round(probability, 2))
    }
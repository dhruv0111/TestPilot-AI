import joblib
import pandas as pd

model = joblib.load("app/ml/model.pkl")
scaler = joblib.load("app/ml/scaler.pkl")

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
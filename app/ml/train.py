import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Load data
df = pd.read_csv("data/ml_data.csv")

# Features + target
X = df[["failures", "avg_response_time", "error_rate", "high_severity_bugs"]]
y = df["risk"]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LogisticRegression()
model.fit(X_scaled, y)

# Ensure folder exists
os.makedirs("app/ml", exist_ok=True)

# Save model + scaler
joblib.dump(model, "app/ml/model.pkl")
joblib.dump(scaler, "app/ml/scaler.pkl")

print("✅ Model and scaler saved successfully!")
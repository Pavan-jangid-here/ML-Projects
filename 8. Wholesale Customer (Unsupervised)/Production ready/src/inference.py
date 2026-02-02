import numpy as np
import pandas as pd
import joblib

# Load artifacts
kmeans = joblib.load("models/kmeans_model.pkl")
scaler = joblib.load("models/scaler.pkl")
pca = joblib.load("models/pca.pkl")
feature_order = joblib.load("models/feature_order.pkl")

NUM_COLS = [
    "Fresh", "Milk", "Grocery",
    "Frozen", "Detergents_Paper", "Delicassen"
]

def predict_cluster(input_data: dict) -> int:
    """
    input_data: dict with keys:
    Channel, Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen
    """

    df = pd.DataFrame([input_data])

    # Log transform
    df[NUM_COLS] = np.log1p(df[NUM_COLS])

    # One-hot encode Channel
    df = pd.get_dummies(df, columns=["Channel"], drop_first=True)

    # Ensure feature order
    for col in feature_order:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_order]

    # Scale + PCA
    X_scaled = scaler.transform(df)
    X_pca = pca.transform(X_scaled)

    # Predict cluster
    cluster = kmeans.predict(X_pca)[0]
    return int(cluster)

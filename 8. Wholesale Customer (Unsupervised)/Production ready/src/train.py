import pandas as pd
import numpy as np
import joblib
import mlflow
import mlflow.sklearn

from sklearn.preprocessing import RobustScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# -----------------------------
# Config
# -----------------------------
DATA_PATH = "data/Wholesale customers data.csv"
MODEL_DIR = "models"
RANDOM_STATE = 42
PCA_VARIANCE = 0.9
N_CLUSTERS = 4

NUM_COLS = [
    "Fresh", "Milk", "Grocery",
    "Frozen", "Detergents_Paper", "Delicassen"
]

CAT_COLS = ["Channel"]

# -----------------------------
# MLflow setup
# -----------------------------
mlflow.set_experiment("wholesale-customer-segmentation")

with mlflow.start_run():

    # -----------------------------
    # 1. Load Data
    # -----------------------------
    df = pd.read_csv(DATA_PATH)

    # -----------------------------
    # 2. Validation
    # -----------------------------
    assert (df[NUM_COLS] >= 0).all().all(), "Negative values detected"
    assert df["Channel"].isin([1, 2]).all(), "Invalid Channel values"

    # -----------------------------
    # 3. Feature Engineering
    # -----------------------------
    X_num = np.log1p(df[NUM_COLS])
    X_cat = pd.get_dummies(df[CAT_COLS], drop_first=True)

    X = pd.concat([X_num, X_cat], axis=1)

    # -----------------------------
    # 4. Scaling
    # -----------------------------
    scaler = RobustScaler()
    X_scaled = scaler.fit_transform(X)

    # -----------------------------
    # 5. PCA
    # -----------------------------
    pca = PCA(n_components=PCA_VARIANCE, random_state=RANDOM_STATE)
    X_pca = pca.fit_transform(X_scaled)

    # -----------------------------
    # 6. Train KMeans
    # -----------------------------
    kmeans = KMeans(
        n_clusters=N_CLUSTERS,
        random_state=RANDOM_STATE
    )
    clusters = kmeans.fit_predict(X_pca)

    # -----------------------------
    # 7. Evaluation
    # -----------------------------
    silhouette = silhouette_score(X_pca, clusters)

    # -----------------------------
    # 8. Save Artifacts
    # -----------------------------
    joblib.dump(kmeans, f"{MODEL_DIR}/kmeans_model.pkl")
    joblib.dump(scaler, f"{MODEL_DIR}/scaler.pkl")
    joblib.dump(pca, f"{MODEL_DIR}/pca.pkl")
    joblib.dump(list(X.columns), f"{MODEL_DIR}/feature_order.pkl")

    # -----------------------------
    # 9. MLflow Logging
    # -----------------------------
    mlflow.log_param("model", "KMeans")
    mlflow.log_param("n_clusters", N_CLUSTERS)
    mlflow.log_param("scaler", "RobustScaler")
    mlflow.log_param("pca_variance", PCA_VARIANCE)

    mlflow.log_metric("silhouette_score", silhouette)

    mlflow.sklearn.log_model(kmeans, "kmeans_model")
    mlflow.log_artifact(f"{MODEL_DIR}/scaler.pkl")
    mlflow.log_artifact(f"{MODEL_DIR}/pca.pkl")
    mlflow.log_artifact(f"{MODEL_DIR}/feature_order.pkl")

    print("Training completed successfully")
    print(f"Silhouette Score: {silhouette:.4f}")

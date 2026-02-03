from src.drift import detect_drift
import pandas as pd

train_data = pd.read_csv("data/Wholesale customers data.csv")
new_data = pd.read_csv("data/new_customers.csv")

drift_report = detect_drift(
    train_data[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]],
    new_data[["Fresh","Milk","Grocery","Frozen","Detergents_Paper","Delicassen"]]
)

print(drift_report)

## 📁 Project Structure

```
wholesale-ml/
│
├── data/
├── models/
│   ├── kmeans_model.pkl
│   ├── scaler.pkl
│   ├── pca.pkl
│   └── feature_order.pkl
│
├── src/
│   ├── inference.py
│   ├── train.py
│   └── drift.py
│
├── app.py
├── requirements.txt
└── README.md
```


pip install mlflow
run mlflow ui

pip install fastapi uvicorn

uvicorn app:app --reload


## Test of api:
POST /predict
{
  "Channel": 2,
  "Fresh": 12669,
  "Milk": 9656,
  "Grocery": 7561,
  "Frozen": 214,
  "Detergents_Paper": 2674,
  "Delicassen": 1338
}


# Usage of drift py file:

drift = detect_drift(train_data[numerical_cols], new_data[numerical_cols])


📌 In production:

Run weekly/monthly

Trigger retraining if drift detected
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
pip install fastapi uvicorn

# Run this commands
```
cd to Production Ready folder using cd function
python src/train.py
run mlflow ui
uvicorn app:app --reload
Use py file called usage and detect_drift.py for the testing purpose.
```

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


# How to Dockerize the app

```
1. How to build the image
docker build -t wholesale-ml:latest .

2. How to run the builded image
docker run -p 8000:8000 wholesale-ml:latest

```


# Working on CI/CD pipeline

1. created the ci.yml
2. linux path to be used. like this paths:
      - "8. Wholesale Customer (Unsupervised)/Production ready/**"
3. Always use this "/" instead of "\" for path in ci.yml


# Set to register the API in Github Container register

1. Added lines in ci.yml
2. Also update the build docker image with ghcr.io
3. 🧠 Important Rule (Remember This Forever)
    - Docker image names must be lowercase only
        - This applies to:
            1. Docker Hub
            2. GHCR
            3. Kubernetes
            4. Cloud registries
4. Converted to lower case letter using [:upper:] [:lower:]


# Started with the Image container deployment

1. Using Render free tier as deployment
2. Using Web app services using existing images
3. Use this link: ghcr.io/pavan-jangid-here/wholesale-ml:latest
4. You will find the new app deployed in link called: https://wholesale-ml-api.onrender.com/
5. You will find the API in this place: https://wholesale-ml-api.onrender.com/docs/


# Lets build front end and joint live api

1. We will first build the front end and joint the api.
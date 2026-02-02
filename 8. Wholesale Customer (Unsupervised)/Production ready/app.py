from fastapi import FastAPI
from pydantic import BaseModel
from src.inference import predict_cluster

app = FastAPI(title="Wholesale Customer Segmentation API")

class CustomerInput(BaseModel):
    Channel: int
    Fresh: float
    Milk: float
    Grocery: float
    Frozen: float
    Detergents_Paper: float
    Delicassen: float

@app.post("/predict")
def predict(data: CustomerInput):
    cluster = predict_cluster(data.dict())
    return {
        "customer_segment": cluster
    }

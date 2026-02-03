from src.inference import predict_cluster

customer = {
    "Channel": 2,
    "Fresh": 12669,
    "Milk": 9656,
    "Grocery": 7561,
    "Frozen": 214,
    "Detergents_Paper": 2674,
    "Delicassen": 1338
}

cluster = predict_cluster(customer)
print("Customer Segment:", cluster)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

customer_risk_profile = {
    101:{"name": "Abhishek Kumar", "risk": "low", "score": 0.12},
    102:{"name": "pranay Singh", "risk": "medium", "score": 0.54},
    103:{"name": "Arjun rampal", "risk": "high", "score": 0.89}
}

@app.get("/customerss")
def get_customers(city:str, risk:str):
    return{"city": city, "risk": risk}

@app.get("/customer/{customer_id}")
def get_customer_risk(customer_id: int):
    if customer_id not in customer_risk_profile:
        return {"error": f"customer {customer_id} not in database"}

    profile = customer_risk_profile[customer_id]

    return {
        "customer_id": customer_id,
        "name": profile["name"],
        "risk_level" : profile["risk"],
        "score" : profile["score"]
    }

@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction(model_name: str, customer_id: int):
    return{
        "model" : model_name,
        "customer_id": customer_id,
        "prediction": "high"
    }
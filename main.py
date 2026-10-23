from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first api is working"}

@app.get("/about")
def about():
    return{"project": "Loan Risk Model", "Version": "1.0"}

@app.get("/Customer")
def get_customer(Customer_id: int):
    return{
        "Customer_id": Customer_id,
        "name": "Abhi",
        "status": "active"
    }
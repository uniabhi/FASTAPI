from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanApplication(BaseModel):
    name: str
    age: int
    income: float
    loan_amount: float
    employeement_years: int


@app.post("/predict")
def predict_loan(application: LoanApplication):
    approved = (
        application.income > 50000 and
        application.employeement_years > 2 and
        application.age >=21
    )

    return {
        "applicant name" : application.name,
        "Loan_amount" : application.loan_amount,
        "deision" : "approved" if approved else "rejected",
        "review_income" : application.income 
    }
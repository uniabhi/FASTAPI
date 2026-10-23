from fastapi import FastAPI

app = FastAPI()

all_customers = [
    {"id":101, "name": "Ravi", "city": "bengaluru", "risk": "low"},
    {"id":102, "name": "Dhanu", "city": "mumbai", "risk": "medium"},
    {"id":103, "name": "Sahu", "city": "bengaluru", "risk": "low"},
    {"id":104, "name": "jayram", "city": "noida", "risk": "medium"},
    {"id":105, "name": "roy", "city": "chennai", "risk": "low"},
    {"id":106, "name": "shanu", "city": "pune", "risk": "high"}
]

@app.get("/customers")
def get_customers(city:str, risk:str):
    filtered = [
        c for c in all_customers
        if c["city"] ==city and c["risk"]==risk
    ]

    return {
        "city":city,
        "risk": risk,
        "count": len(filtered),
        "results": filtered
    }
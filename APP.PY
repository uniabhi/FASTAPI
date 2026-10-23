from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# FastAPI application बनाना
app = FastAPI(
    title="Iris Flower Prediction API",
    version="1.0"
)

# ------------------ Model training ------------------
iris = load_iris()

X_train, X_test, y_train, y_test = train_test_split(
    iris.data,
    iris.target,
    test_size=0.20,
    random_state=42,
    stratify=iris.target
)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# Flower class names
class_names = iris.target_names


# ------------------ Input validation schema ------------------
class FlowerInput(BaseModel):
    sepal_length: float = Field(..., gt=0, description="Sepal length in cm")
    sepal_width: float = Field(..., gt=0, description="Sepal width in cm")
    petal_length: float = Field(..., gt=0, description="Petal length in cm")
    petal_width: float = Field(..., gt=0, description="Petal width in cm")


# ------------------ Typed response schema ------------------
class PredictionResponse(BaseModel):
    predicted_class_id: int
    predicted_flower: str
    confidence: float


# ------------------ Health check endpoint ------------------
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "message": "API and model are running"
    }


# ------------------ Prediction endpoint ------------------
@app.post("/predict", response_model=PredictionResponse)
def predict_flower(flower: FlowerInput):
    # API input को model के required list format में convert करना
    features = [[
        flower.sepal_length,
        flower.sepal_width,
        flower.petal_length,
        flower.petal_width
    ]]

    # Prediction और probability निकालना
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    confidence = float(max(probabilities))

    return PredictionResponse(
        predicted_class_id=int(prediction),
        predicted_flower=class_names[prediction],
        confidence=round(confidence, 2)
    )
from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Define input data schema
class Features(BaseModel):
    feature_list: list

app = FastAPI()
model = joblib.load("model.pkl")

@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}

@app.post("/predict")
def predict_price(data: Features):
    prediction = model.predict(np.array(data.feature_list).reshape(1, -1))
    return {"prediction": prediction.tolist()}

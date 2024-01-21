import uvicorn
from fastapi import FastAPI, Query
from src.predict_data.predict import Predict

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "works!"}


@app.get("/predict")
async def predict_data(ticker: str, period: int = Query(1)):
    p = Predict(ticker, period=period)
    predictions = p.get_predicted_data()
    print(type(predictions))
    for prediction in predictions:
        for key, value in prediction.items():
            prediction[key] = float(value)
    print(predictions)
    return predictions


# uvicorn.run(app, host="0.0.0.0", port=5002)

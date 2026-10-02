from fastapi import FastAPI
from app.schemas.predict_schema import PrediccionInput
from app.services.predict import preprocess, predict_survive
import pandas as pd
import joblib

random_forest_model = joblib.load('models/random_forest_model.pkl')

app = FastAPI()

@app.get("/")
def root():
    return {'message': 'API works!'}

@app.post("/predict")
def predict(data: PrediccionInput):

    # Cambiar el objeto a un diccionario simple
    data_dict = data.model_dump()

    # Hay que ocupar [] porque el pd.DataFrame espera varias filas, cada una es un diccionario (con las mismas llaves para que sean las columnas)
    data_df = pd.DataFrame([data_dict])

    # Preprocesar data para que luego pase por el pipeline
    data_df = preprocess(data_df)

    # Enviar la información procesada al modelo
    prediction, prediction_word = predict_survive(random_forest_model, data_df)

    print(prediction, prediction_word)

    return {"prediction": prediction, "label": prediction_word}


import joblib
from src.feature_engineering import extract_title, rename_titles


def preprocess(data_df):

    # Cambiar a binario sex
    data_df['Sex'] = data_df['Sex'].map({'female': 0, 'male': 1})

    # Crear feature FamilySize
    data_df['FamilySize'] = data_df['SibSp'] + data_df['Parch'] + 1

    # Crear feature IsAlone
    data_df['IsAlone'] = (data_df['FamilySize'] == 1).astype(int)

    # Crear feature de Title y luego eliminarlo
    title = data_df['Name'].apply(extract_title)
    data_df['Title'] = title
    data_df['Title'] = data_df['Title'].apply(rename_titles)

    data_df = data_df.drop(columns=['Name'])

    return data_df

def predict_survive(model, data_df):

    # Generar predicción y pasar a int para que el json devuelvo de la api lo pueda procesar
    prediction = model.predict(data_df)[0]
    prediction = int(prediction)

    # Predicción en palabras
    prediction_word = ''
    if prediction == 1:
        prediction_word = 'Survive'
    else:
        prediction_word = 'Not survive'

    return prediction, prediction_word
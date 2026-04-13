def rellenar_age_median(df):
    info_rellenar_datos_age = {'Age': df['Age'].median()}
    df_edad_rellenada = df.fillna(info_rellenar_datos_age)
    return df_edad_rellenada

def eliminar_cabin(df):
    df_drop_cabin = df.drop(columns=['Cabin'])
    return df_drop_cabin

def rellenar_embarked(df):
    moda_embarked = df['Embarked'].mode().iloc[0]
    df['Embarked'] = df['Embarked'].fillna(moda_embarked)
    df_procesado = df
    return df_procesado

def eliminar_columnas_innecesarias(df):
    df_ml = df.drop(columns=['PassengerId', 'Ticket'])
    return df_ml

def rellenar_fare_median(df):
    info_rellenar_datos_age = {'Fare': df['Fare'].median()}
    df_edad_rellenada = df.fillna(info_rellenar_datos_age)
    return df_edad_rellenada

def eliminar_columnas_ml(df_ml):
    df_ml.drop(columns=['Embarked_Q', 'Title', 'Name'])
    return df_ml
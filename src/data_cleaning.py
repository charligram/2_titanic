def rellenar_age_median(df):
    """
    Obtener la mediana de la columna 'Age' y rellenar los valores faltantes con esa mediana

    Args:
        df (pd.DataFrame): DataFrame con los datos faltantes en columna 'Age'

    Returns:
        df_edad_rellenada (pd.DataFrame): DataFrame sin valores faltantes en 'Age'
    """
    info_rellenar_datos_age = {'Age': df['Age'].median()}
    df_edad_rellenada = df.fillna(info_rellenar_datos_age)
    return df_edad_rellenada

def eliminar_cabin(df):
    """
    Eliminar la columna 'Cabin'

    Args:
        df (pd.DataFrame): DataFrame con alguna columna con nombre 'Cabin'

    Returns:
        df_drop_cabin (pd.DataFrame): DataFrame con todos los valores anteriores pero sin 'Cabin'
    """
    df_drop_cabin = df.drop(columns=['Cabin'])
    return df_drop_cabin

def rellenar_embarked(df):
    """
    Rellenar valores faltantes dentro de columna 'Embarked' con el valor que mas se repita

    Args:
        df (pd.DataFrame): DataFrame con valores faltantes en columna 'Embarked'
    
    Returns:
        df_procesado (pd.DataFrame): DataFrame con la columna 'Embarked' rellenada
    """
    moda_embarked = df['Embarked'].mode().iloc[0]
    df['Embarked'] = df['Embarked'].fillna(moda_embarked)
    df_procesado = df
    return df_procesado

def eliminar_columnas_innecesarias(df):
    """
    Quitar columnas que no seran de ayuda para hacer análisis

    Args:
        df (pd.DataFrame): DataFrame con columnas que no sean importantes para el análisis

    Returns:
        df_ml (pd.DataFrame): DataFrame con las columnas que puedan ser importantes para el trabajo
        con machine learning
    """

    df_ml = df.drop(columns=['PassengerId', 'Ticket'])
    return df_ml

def rellenar_fare_median(df):
    """
    Rellenar valores faltantes en columna 'Fare' con la mediana

    Args:
        df (pd.DataFrame): DataFrame con valores faltantes en columna de 'Fare'

    Returns:
        df_fare_rellenado (pd.DataFrame): DataFrame con columna 'Fare' sin valores faltantes
    """
    info_rellenar_datos_fare = {'Fare': df['Fare'].median()}
    df_fare_rellenado = df.fillna(info_rellenar_datos_fare)
    return df_fare_rellenado

def eliminar_columnas_ml(df_ml):
    """
    Eliminar las columnas que se necesiten para que el modelo de machine learning no colapse debido
    a que las columnas eliminadas no son numéricas o son dummys

    Args:
        df_ml (pd.DataFrame): DataFrame con columnas con strings o innecesarias
    
    Returns:
        df_ml (pd.DataFrame): DataFrame listo para ser utilizado en modelo de machine learning
    """
    df_ml = df_ml.drop(columns=['Embarked_Q', 'Title', 'Name'])
    return df_ml
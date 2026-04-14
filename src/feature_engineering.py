def sex_map(df_ml):
    """
    Codificar los valores de 'Sex' en forma "female=0" y "male=1"

    Args:
        df_ml (pd.DataFrame): DataFrame con valores en sex con palabras

    Returns:
        df_ml (pd.DataFrame): DataFrame con sexo binario
    """
    df_ml['Sex'] = df_ml['Sex'].map({'female': 0, 'male': 1})
    return df_ml

def one_hot_embarked(df_ml):
    """
    Convertir la columna de 'Embarked' a 3 columnas individuales, donde cada una represente con
    un 1 en su valor si pertenece al 'Embarked' y 0 si no

    Args:
        df_ml (pd.DataFrame): DataFrame con columna 'Embarked' con valores indicando la letra
        de donde fue embarcado el pasajero
    
    Returns:
        df_ml (pd.DataFrame): DataFrame sin la columna 'Embarked' pero con 3 columnas nuevas
        indicando pertenecer o no al grupo
        Ej:
            Embarked = Q   -->  Embarked_C=0   Embarked_Q=1   Embarked_S=0
    """
    df_ml['Embarked_C'] = (df_ml['Embarked'] == 'C').astype(int)
    df_ml['Embarked_Q'] = (df_ml['Embarked'] == 'Q').astype(int)
    df_ml['Embarked_S'] = (df_ml['Embarked'] == 'S').astype(int)

    df_ml = df_ml.drop(columns=['Embarked'])
    return df_ml

def family_size_isAlone(df_ml):
    """
    Calcular el tamaño de la familia contando el pasajero, creando columna del tamaño. Además de
    crear una segunda columna indicando si el pasajero va solo o no
    
    Args:
        df_ml (pd.DataFrame): DataFrame con columnas de SibSp y Parch, completamente necesarias
        para realizar el calculo
    
    Returns:
        df_ml (pd.DataFrame): DataFrame con columnas para el tamaño de la familia y columnas con
        indicador binario de si va solo o no
    """
    df_ml['tamanio_familia'] = df_ml['SibSp'] + df_ml['Parch'] + 1
    df_ml['isAlone'] = (df_ml['tamanio_familia'] == 1).astype(int)
    return df_ml

def one_hot_titles(df_ml):
    """
    Crear columnas One-Hot indicando el título de cada pasajero

    Args:
        df_ml (pd.DataFrame): DataFrame con columna 'Name' desde donde se pueda extraer la información
        del título del pasajero
    
    Returns:
        df_ml (pd.DataFrame): DataFrame con columnas para cada título, considerando 4 títulos
        generales y que mas se repitan y 1 (Rare) con la combinación de títulos poco frecuentes,
        indicando si pertenece o no al título de forma binaria
    """
    titulos_totales = []
    for nombre in df_ml['Name']:
        titulo_antes_del_punto = ''
        for letra in nombre:
            if letra != '.':
                titulo_antes_del_punto += letra
            else:
                break
        titulo = titulo_antes_del_punto.split(' ')[-1]
        titulos_totales.append(titulo)

    df_ml['Title'] = titulos_totales
    lista_titulos_normales = ['Mr', 'Miss', 'Mrs', 'Master']
    df_ml['Title'] = df_ml['Title'].apply(
        lambda titulo: titulo if titulo in lista_titulos_normales else 'Rare'
    )
    df_ml['isMr'] = (df_ml['Title'] == 'Mr').astype(int)
    df_ml['isMrs'] = (df_ml['Title'] == 'Mrs').astype(int)
    df_ml['isMiss'] = (df_ml['Title'] == 'Miss').astype(int)
    df_ml['isMaster'] = (df_ml['Title'] == 'Master').astype(int)
    df_ml['isRare'] = (df_ml['Title'] == 'Rare').astype(int)
    return df_ml
def sex_map(df_ml):
    df_ml['Sex'] = df_ml['Sex'].map({'female': 0, 'male': 1})
    return df_ml

def one_hot_embarked(df_ml):
    df_ml['Embarked_C'] = (df_ml['Embarked'] == 'C').astype(int)
    df_ml['Embarked_Q'] = (df_ml['Embarked'] == 'Q').astype(int)
    df_ml['Embarked_S'] = (df_ml['Embarked'] == 'S').astype(int)

    df_ml = df_ml.drop(columns=['Embarked'])
    return df_ml

def family_size_isAlone(df_ml):
    df_ml['tamanio_familia'] = df_ml['SibSp'] + df_ml['Parch'] + 1
    df_ml['isAlone'] = (df_ml['tamanio_familia'] == 1).astype(int)
    return df_ml

def one_hot_titles(df_ml):
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
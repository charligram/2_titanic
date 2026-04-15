def contar_sobrevivientes(df_sobrevivientes):
    """
    Genenrar información resumida de cantidad de sobrevivientes

    Args:
        df_sobrevivientes (pd.DataFrame): DataFrame con los valores de una columna en específico y su valor de sobreviviente
    
    Returns:
        cuenta_sobrevivientes (pd.DataFrame): Cuenta total de sobrevivientes y no sobrevivientes
    """
    cuenta_sobrevivientes = df_sobrevivientes['Sobreviviente'].value_counts()
    cuenta_sobrevivientes = cuenta_sobrevivientes.reset_index()
    return cuenta_sobrevivientes
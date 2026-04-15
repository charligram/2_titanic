def contar_sobrevivientes(df_sobrevivientes):
    cuenta_sobrevivientes_mujeres = df_sobrevivientes['Sobreviviente'].value_counts()
    cuenta_sobrevivientes_mujeres = cuenta_sobrevivientes_mujeres.reset_index()
    return cuenta_sobrevivientes_mujeres
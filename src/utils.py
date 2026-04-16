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

def conf_titulo_fig(fig, titulo):
    """
    Configurar el título de un figure

    Args:
        fig (px.Figure): Figure con los datos ya plasmados pero sin título

        titulo (str): Nombre para el título

    Returns:
        None
    """
    fig.update_layout(
        title=titulo
    )

def guardar_fig(fig, nombre):
    """
    Guardar una figura creada dentro de la carpeta figures en outputs

    Args:
        fig (px.Figure): Figura que se quiere almacenar

        nombre (str): Nombre para la imagen
    Returns:
        None

    """
    fig.write_image(f'../outputs/figures/{nombre}.png')
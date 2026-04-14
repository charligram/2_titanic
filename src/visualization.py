import plotly.express as px

def create_fig_pie__sobrevivientes(df_sobrevivientes):
    mapeo_colores = {
        'Sobrevivió': '#4365ff',
        'No sobrevivió': '#ff4848'
    }
    fig_pie_sobrevivientes = px.pie(
        df_sobrevivientes,
        values='count',
        names='Sobreviviente',
        color='Sobreviviente',
        color_discrete_map=mapeo_colores
    )
    return fig_pie_sobrevivientes
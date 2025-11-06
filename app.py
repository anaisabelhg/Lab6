#GITHUB incluir en el mismo chunk la carga de los paquetes que usamos (no instalacion)
import plotly as pl
import plotly.express as px
#import numpy as np
import pandas as pd
import pathlib
import dash
#para hacer dashboards
#from dash import Dash,
from dash import dcc,html,dash_table,Input,Output
import dash_bootstrap_components as dbc

# Paso 1_: crear app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Linea para Github
server=app.server

# Paso 2_: layout
app.layout = html.Div([
    # titulo Dashboard:
    html.H1("Evolución de la media de la edad por departamento"),

    # titulo gráfica 1
    html.H3("Edad Media de Departamentos"),

    # Dropdown
    dcc.Dropdown(
        id="Departamentos",
        options=["Guatemala", "Escuintla","Quetzaltenango","Sololá","Quiche"],
        value="Guatemala"
    ),
    dcc.Graph(id="line-plot")
])

# Paso 3 y 4_: Callbacks

@app.callback(
    Output("line-plot", "figure"),
    Input("Departamentos", "value")
)

def update_line_plot(Departamentos):
    fig = px.line(
        dfc,
        x="Year",
        y=Departamentos,
        title=f"Evolución de la edad media en {Departamentos}",
        markers=True
    )
    fig.update_layout(
        xaxis_title="Año",
        yaxis_title="Edad media",
        template="plotly_white"
    )
    return fig

#Paso 5
if __name__ =="__main__":
    app.run(debug=False,host="0.0.0.0",port=2240)


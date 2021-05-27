import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import modulos
from modulos import Connection

external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


#Cases by country
con = Connection()
con.openConnection()
consulta1 = pd.read_sql_query(modulos.consulta1(), con.connection)
consulta1a = pd.read_sql_query(modulos.consulta1a(), con.connection)
consulta2 = pd.read_sql_query(modulos.consulta2(), con.connection)
consulta2a = pd.read_sql_query(modulos.consulta2a(), con.connection)
consulta3 = pd.read_sql_query(modulos.consulta3(), con.connection)
consulta4 = pd.read_sql_query(modulos.consulta4(), con.connection)
con.closeConnection()
consulta1 = pd.DataFrame(consulta1, columns=["anio", "mes", "nombre", "llamadas_recibidas"])
consulta1a = pd.DataFrame(consulta1a, columns=["id", "nombre", "total_habitantes"])
consulta2 = pd.DataFrame(consulta2, columns=["incidente", "total"])
consulta2a = pd.DataFrame(consulta2a, columns=["incidente", "total_2019"])
consulta3 = pd.DataFrame(consulta3, columns=["mes", "total"])
consulta4 = pd.DataFrame(consulta4, columns=["nombre","total"])
figConsulta1 = px.bar(consulta1.head(20), x="nombre", y="llamadas_recibidas")
figConsulta1a = px.bar(consulta1a.head(20), x="nombre", y="total_habitantes")
figConsulta2 = px.pie(consulta2.head(20), values='total', names='incidente')
figConsulta2a = px.pie(consulta2a.head(20), values="total_2019", names="incidente")
figConsulta3 = px.bar(consulta3.head(20), x="mes", y="total")
figConsulta4 = px.pie(consulta4.head(20), values="total", names="nombre")

#Layout
app.layout = html.Div(children=[
    html.H1(children="Llamadas realizadas al 123", className="text-center"),
    html.H2(children="Llamadas recibidas por localidad durante el año 2020", className="text-center"),
    dcc.Graph(
        id="consulta1",
        figure=figConsulta1
    ),
    html.H2(children="Habitantes por localidad", className="text-center"),
    dcc.Graph(
        id="consulta1a",
        figure=figConsulta1a
    ),
    html.H2(children="Tipos de llamada más comunes durante el año 2020", className="text-center"),
    dcc.Graph(
        id="consulta2",
        figure=figConsulta2
    ),
    html.H2(children="Tipos de llamada más comunes durante el año 2019", className="text-center"),
    dcc.Graph(
        id="consulta2a",
        figure=figConsulta2a
    ),
    html.H2(children="Flujo de llamadas por mes", className="text-center"),
    dcc.Graph(
        id="consulta3",
        figure=figConsulta3
    ),
    html.H2(children="UPZs con la mayor cantidad de hurtos reportados en los últimos 5 años", className="text-center"),
    dcc.Graph(
        id="consulta4",
        figure=figConsulta4
    ),
])

if __name__ == "__main__":
   app.run_server(debug=False)
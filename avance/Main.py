import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import der as sql
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Localidad
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.localidad(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["id", "nombre", "total_habitantes"])
figBarCases = px.bar(dfCases.head(20), x="nombre", y="total_habitantes")

#Casos marzo 2020 

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.enero(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=[ "mes","nombre", "llamadas_recibidas"])
casos22 = px.bar(dfCases.head(20), x="nombre", y="llamadas_recibidas")


#2020
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.incidentesa(), con.connection)
con.closeConnection()
cas = pd.DataFrame(query, columns=["incidente", "total_2020", "anio"])
casos = px.pie(cas.head(20), values="total_2020", names="incidente")

#2019
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.incidentesb(), con.connection)
con.closeConnection()
cas = pd.DataFrame(query, columns=["incidente", "total_2019", "anio"])
casos19 = px.pie(cas.head(20), values="total_2019", names="incidente")



#Layout
app.layout = html.Div(children=[
    html.H1(children='LLamadas al 1234'),
    html.H2(children='Habitantes por localidad'),
    dcc.Graph(
        id='barCasesByCountry',
        figure=figBarCases
    ),
    html.H2(children="LLamadas al 1234 en marzo de 2020"),
    dcc.Graph(
        id="Marzo 2020",
        figure=casos22
    ),
    html.H2(children="incidentes en el 2020"),
    dcc.Graph(
        id="incidentes 2020",
        figure=casos
    ),
    html.H2(children="incidentes en el 2019"),
    dcc.Graph(
        id="incidentes 2019",
        figure=casos19
    ),
    
    
])

if __name__ == '__main__':
    app.run_server(debug=False)
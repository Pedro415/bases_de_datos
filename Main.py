import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from Connection import Connection
import der as sql
external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

#Cases by country
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.totalCasesByCountry(), con.connection)
con.closeConnection()
dfCases = pd.DataFrame(query, columns=["id", "nombre", "total_habitantes"])
figBarCases = px.bar(dfCases.head(20), x="nombre", y="total_habitantes")
#figMapCases = px.choropleth(dfCases, locations="country", locationmode="country names", color="amount", hover_name="country", color_continuous_scale=["#99ccff", "#ff3333"])


#Layout
app.layout = html.Div(children=[
    html.H1(children='LLamadas a 1234'),
    html.H2(children='Habitantes por localidad'),
    dcc.Graph(
        id='barCasesByCountry',
        figure=figBarCases
    ),
    
])

if __name__ == '__main__':
    app.run_server(debug=False)
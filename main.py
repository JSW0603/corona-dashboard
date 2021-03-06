import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from data import countries_df, totals_df, dropdown
from builder import make_table
from dash.dependencies import Input, Output


stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap"
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(
    countries_df,
    size="Confirmed",
    size_max=40,
    title="Confirmed by country",
    color="Confirmed",
    hover_name="Country_Region",
    locationmode="country names",
    locations="Country_Region",
    template="plotly_dark",
    projection="equirectangular",
    color_continuous_scale=px.colors.sequential.Oryel,
    hover_data={
        "Confirmed": ':,f',
        "Deaths": ':,f',
        "Recovered": ':,f',
        "Country_Region": False,
    },
)

bubble_map.update_layout(
    margin=dict(l=0, r=0, t=50, b=10)
)

bars_graph = px.bar(
    totals_df,
    x="condition",
    y="count",
    hover_data={"count": ":,"},
    template="plotly_dark",
    title="Total Global Case",
    labels={
        "condition": "Condition",
        "count": "Count",
        "color": "Condition"
    }
)

bars_graph.update_traces(
    marker_color=["#e74c3c", "#8e44ad", "#27ae60"]
)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "black",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif"
    },
    children=[
        html.Header(
            style={"textAlign": "center", "paddingTop": "50px", "marginBottom": 100},
            children=[html.H1("Corona Dashboard", style={"fontSize": 40})]
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(
                    style={"grid-column": "span 3"},
                    children=[dcc.Graph(figure=bubble_map)]),
                html.Div(children=[make_table(countries_df)]),
            ],
        ),
        html.Div(
            style={
                "display": "grid",
                "gap": 50,
                "gridTemplateColumns": "repeat(4, 1fr)",
            },
            children=[
                html.Div(children=[dcc.Graph(figure=bars_graph)]),
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id="country",
                            options=[
                                {'label': country, "value": country} for country in dropdown
                            ],
                        ),
                        html.H1(id="country-output"),
                    ]
                ),
            ],
        ),
    ],
)

@app.callback(Output("country-output", "children"),[Input("country", "value")])
def update_hello(value):
    print(value)

if __name__ == '__main__':
    app.run_server(debug=True)

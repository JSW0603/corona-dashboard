import dash_html_components as html

def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                    style={"display": "block", "marginBottom": 25},
                    children=[
                        html.Tr(  # Header title 지정
                            children=[
                                html.Th(column_name.replace("_", " "))
                                for column_name in df.columns
                            ],
                            style={
                                "display": "grid",
                                "gridTemplateColumns": "repeat(4, 1fr)",
                                "fontWeight": "600",
                                "fontSize": 15,
                            },
                        )
                    ],
                ),
            html.Tbody(
                style={"display": "block", "textAlign": "center"},
                children=[
                    html.Tr(
                        style={
                            "display": "grid",
                            "gridTemplateColumns": "repeat(4, 1fr)",
                            "border-top": "1px solid white",
                            "padding": "30px 0px",
                        },
                        children=[
                            html.Td(
                                value_column
                            ) for value_column in value
                        ],
                    )
                    for value in df.values
                ],
            ),
        ],
    )

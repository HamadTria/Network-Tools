from dash import html, clientside_callback, register_page, dcc
from dash.dependencies import Input, Output
from view import navbar

register_page(__name__)

def layout():
    nav_bar = navbar.draw_navbar()
    
    contents = html.Div([
        html.Div(id="dummy-output"),
        dcc.Store(id="graph-data", data={}),
        html.Div(id="sigma-container", style={"width": "100%", "height": "500px", "border": "1px solid #ccc"}),
        html.Button(id="center-graph-button", children="Center Graph"),
        html.Div(id="node-info", style={"margin-top": "20px", "font-size": "16px"}),
        html.Label("Select Graph:"),
        dcc.Dropdown(id="graph-selector", options=[
            {"label": "Graph 1", "value": "graph1"},
            {"label": "Graph 2", "value": "graph2"}
        ], value="graph1")
    ])
    return html.Div([nav_bar, contents])

with open('assets/sigma_functions.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("dummy-output", "children"),
    Input("center-graph-button", "n_clicks"),
    Input("graph-selector", "value"),
    prevent_initial_call=False
)

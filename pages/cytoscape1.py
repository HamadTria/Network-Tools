import json
from dash import Input, Output, html, clientside_callback, register_page
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from view import navbar

cyto.load_extra_layouts()

register_page(__name__)

def layout():
    nav_bar = navbar.draw_navbar()
    cyto_div = html.Div([
                    html.Div(id="dummy-output-cyto"),
                    dbc.Row([
                        html.Div(id="cyto-container", style={"width": "100%", "height": "800px", "display": "inline-block"}),
                    ]),
                    dbc.Col(
                        html.Div(id="cyto-small-container", style={"width": "100%", "height": "200px", "display": "inline-block"}), 
                        width=3, lg = 1
                    )
                ])
    return html.Div([nav_bar, cyto_div])

with open('assets/cytoscape1.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("dummy-output-cyto", "children"),
    Input("dummy-output-cyto", "children")
)

from dash import Input, Output, html, clientside_callback, register_page
import dash_bootstrap_components as dbc
from view import navbar

register_page(__name__)

def layout():
    card_style = {
        "margin": "1rem",
        "boxShadow": "0px 0px 15px rgba(0,0,0,0.2)",
        "width": "300px",
    }

    card_header_style = {
        "fontSize": "1.5rem",
        "fontWeight": "bold",
        "color": "#FFFFFF",
    }

    nav_bar = navbar.draw_navbar()

    cyto_div = html.Div([
                    dbc.CardHeader([
                        html.Img(src="/assets/cytoscape.png",
                                style={
                                    "height": "2rem",
                                    "marginRight": "10px"
                                }),
                                "Cytoscape"
                    ], className="text-center", style=card_header_style),
                    html.Div(id="dummy-output-cyto"),
                    html.Div(id="cyto-container", style={"height": "700px"}),
                    dbc.Card([
                        html.Div(id="cyto-small-container", style={"height": "300px", "width": "300px"}),
                    ], style=card_style, className="ms-auto"),
                ])
    return html.Div([nav_bar, cyto_div])

with open('assets/cntx.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("dummy-output-cyto", "children"),
    Input("dummy-output-cyto", "children")
)

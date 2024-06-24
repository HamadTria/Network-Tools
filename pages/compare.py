from dash import html, clientside_callback, register_page, page_registry
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from view import navbar

register_page(__name__)

def layout():
    nav_bar = navbar.draw_navbar()

    card_style = {
        "margin": "1rem",
        "boxShadow": "0px 0px 15px rgba(0,0,0,0.2)",
    }

    card_header_style = {
        "fontSize": "1.5rem",
        "fontWeight": "bold",
        "color": "#FFFFFF",
    }

    cytograph = html.Div([
                    html.Div(id="cytos-compare"),
                    html.Div(id="cyto-container-compare", style={"width": "100%", "height": "500px"}),
    ])
    
    card_content_cyto = [
        dbc.CardHeader([
            html.Img(src="/assets/cytoscape.png",
                        style={
                            "height": "2rem",
                            "marginRight": "10px"
                        }), "Cytoscape"
        ],
                        className="text-center",
                        style=card_header_style),
        dbc.CardBody(cytograph)
    ]

    sigma = html.Div([
        html.Div(id="sigma-compare"),
        html.Div(id="sigma-container-compare", style={"width": "100%", "height": "500px"}),
    ])

    card_content_sigma = [
        dbc.CardHeader([
            html.Img(src="/assets/sigma-js.png",
                     style={
                         "height": "2rem",
                         "marginRight": "10px"
                     }), "Sigma.js"
        ],
                       className="text-center",
                       style=card_header_style),
        dbc.CardBody(sigma)
    ]

    contents = dbc.Row([
                        dbc.Col([dbc.Card(card_content_sigma, 
                                        color="primary",
                                        outline=True,
                                        style=card_style),
                                dbc.Button(dbc.NavLink("Discover more on sigma.js", 
                                                       href=page_registry['pages.sigma']['path']), 
                                                       className="ms-3"),
                        ]), 
                        dbc.Col([dbc.Card(card_content_cyto,
                                        color="primary",
                                        outline=True,
                                        style=card_style),
                                dbc.Button(dbc.NavLink("Discover more on cytoscape", 
                                                       href=page_registry['pages.cytoscape']['path']), 
                                                       className="ms-3"),
                        ])
                ])
    return html.Div([nav_bar, contents])

with open('assets/compare_sigma.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("sigma-compare", "children"),
    Input("sigma-compare", "children"),
)

with open('assets/compare_cytoscape.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("cytos-compare", "children"),
    Input("cytos-compare", "children"),
)

import configparser
import dash
import dash_bootstrap_components as dbc
from dash import html, dcc
from view import story, navbar

config = configparser.ConfigParser()
config.read('data/config.ini')

dash.register_page(__name__, path='/')

def layout():
    nav_bar = navbar.draw_navbar()

    card_style = {
        "margin": "1rem",
        "boxShadow": "0px 0px 15px rgba(0,0,0,0.2)",
        "height": "1350px"
    }

    card_header_style = {
        "fontSize": "1.5rem",
        "fontWeight": "bold",
        "color": "#FFFFFF",
    }

    card_content_sigma = [
        dbc.CardHeader([
            html.Img(src="/assets/sigma-js.png",
                    style={
                        "height": "2rem",
                        "marginRight": "10px"
                    }), 
                    "Sigma.js"
        ], className="text-center", style=card_header_style),
        dbc.CardBody(story.sigm_story())
    ]

    card_content_cyto = [
        dbc.CardHeader([
            html.Img(src="/assets/cytoscape.png",
                    style={
                        "height": "2rem",
                        "marginRight": "10px"
                    }), 
                    "Cytoscape"
        ], className="text-center", style=card_header_style),
        dbc.CardBody(story.cyto_story())
    ]

    return html.Div([
        nav_bar,
        dbc.Row([
            dbc.Col(
                dcc.Link(
                    dbc.Card(card_content_sigma,
                            color="primary",
                            outline=True,
                            style=card_style),
                            href=dash.page_registry['pages.sigma']['path']
                ), width=18, lg=6),
            dbc.Col(
                dcc.Link(
                    dbc.Card(card_content_cyto,
                            color="primary",
                            outline=True,
                            style=card_style),
                            href=dash.page_registry['pages.cytoscape']['path']
                ), width=18, lg=6)
            ], className="mt-3 g-0"),
        html.Footer(html.P("Stage M1 - Hamad Tria - CMI ISI - 2024", className="text-center"))
    ])



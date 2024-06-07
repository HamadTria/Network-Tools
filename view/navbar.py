import dash_bootstrap_components as dbc
import configparser
from dash import html, page_registry
import os

config = configparser.ConfigParser()
config_path = os.path.abspath('/Users/hamadtria/Documents/CMI_Cours_M1/stage M1/code/APP/data/config.ini')
config.read(config_path)

def draw_navbar():
    bar = dbc.Navbar(
        dbc.Container( 
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src="/assets/logo.svg" , height="30px"), className="ms-3"),
                            dbc.Col(dbc.NavbarBrand("Graph Visualisation Tools", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavItem(dbc.Button(dbc.NavLink("Compare", href=page_registry['pages.compare']['path']), className="ms-auto me-3"))
            ],
            fluid=True,
        ),
        color=config['Colors']['navbar'],
        dark=True
    )
    return bar

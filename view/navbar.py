import dash_bootstrap_components as dbc
import configparser
from dash import html, page_registry
import os

config = configparser.ConfigParser()
config_path = os.path.abspath('data/config.ini')
config.read(config_path)

def draw_navbar():
    bar = dbc.Navbar(
            dbc.Container([
                html.A(
                    dbc.Row([
                            dbc.Col(html.Img(src="/assets/logo.svg" , height="30px"), className="ms-3"),
                            dbc.Col(dbc.NavbarBrand("Graph Visualisation Tools", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavItem(
                    dbc.DropdownMenu([
                            dbc.DropdownMenuItem("Home", href="/"),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem("Compare", href=page_registry['pages.compare']['path']),
                            dbc.DropdownMenuItem("Cytoscape", href=page_registry['pages.cytoscape']['path']),
                            dbc.DropdownMenuItem("Sigma", href=page_registry['pages.sigma']['path']),
                            dbc.DropdownMenuItem(divider=True),
                            dbc.DropdownMenuItem("Context-menu", href=page_registry['pages.cntx']['path']),
                            dbc.DropdownMenuItem("Mode transformation", href=page_registry['pages.mode']['path']),
                            dbc.DropdownMenuItem("Big Data Network", href=page_registry['pages.bigdata']['path']),
                        ], 
                        label="Menu", className="ms-auto me-3", align_end=True)
            )],
            fluid=True,
        ),
        color=config['Colors']['navbar'],
        dark=True
    )
    return bar

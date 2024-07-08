import configparser
from dash import Dash, html, dcc, page_container
import dash_bootstrap_components as dbc
import os

config = configparser.ConfigParser()
config_path = os.path.abspath('/Users/hamadtria/Documents/CMI_Cours_M1/stage_M1/code/Network-Tools/data/config.ini')
config.read(config_path)

app = Dash(__name__,
           use_pages=True,
           suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.CYBORG],
           external_scripts=[config['Sigma']['script'], config['Cytoscape']['script'], config['Chroma']['script']],
           title=config['General']['title'])


app.layout = html.Div(
    style={'backgroundColor': str(config['Colors']['background'])},
    children=[dcc.Location(id="url"), page_container])

if __name__ == '__main__':
    app.run(debug=True, dev_tools_ui=False, dev_tools_props_check=False, dev_tools_serve_dev_bundles=False)

# python -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
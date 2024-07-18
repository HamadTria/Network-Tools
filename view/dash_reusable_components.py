from dash import dcc, html
import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.abspath('data/config.ini')
config.read(config_path)

def NamedDropdown(name, **kwargs):
    return html.Div(
        style={"margin": "10px 0px"},
        children=[
            html.P(children=f"{name}:", style={"margin-left": "3px"}),
            dcc.Dropdown(**kwargs),
        ],
    )

def NamedRadioItems(name, **kwargs):
    return html.Div(
        style={"padding": "20px 10px 25px 4px"},
        children=[html.P(children=f"{name}:"), dcc.RadioItems(**kwargs)],
    )

# Utils
def DropdownOptionsList(*args):
    return [{"label": val.capitalize(), "value": val} for val in args]
import json
import dash
from dash import Input, Output, State, dcc, html, callback, register_page, clientside_callback
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from view import dash_reusable_components as drc
import dash_mantine_components as dmc
from view import navbar
from data import cytoData
import os
import configparser

config = configparser.ConfigParser()
config_path = os.path.abspath('data/config.ini')
config.read(config_path)

cyto.load_extra_layouts()

register_page(__name__)

def layout():
    layout_options_style = {
        "width": "150px", 
        "margin-left": "auto", 
        'background-color':'#299FD6', 
        "border": "0px", 
        "border-radius":"5px"
    }
    
    layout_options= [
        {"label": "Breadthfirst", "value": "breadthfirst"},
        {"label": "Circle", "value": "circle"},
        {"label": "Concentric", "value": "concentric"},
        {"label": "Cose", "value": "cose"}, 
        {"label": "Cose-bilkent", "value": "cose-bilkent"},
        {"label": "Cola", "value": "cola"},
        {"label": "Dagre", "value": "dagre"},
        {"label": "Grid", "value": "grid"},
        {"label": "Klay", "value": "klay"},
        {"label": "Spread", "value": "spread"},
        {"label": "Random", "value": "random"}
    ]

    card_style = {
        "margin": "1rem",
        "boxShadow": "0px 0px 15px rgba(0,0,0,0.2)",
    }

    default_mode = ["fab-whatsapp"]
    default_layout = "random"
    nav_bar = navbar.draw_navbar()
    content = html.Div([
        html.Div([
            html.Label("Select Modes to Consider:"),
            dcc.Dropdown(
                    id="bigdata-dropdown",
                    options=[{"label": mode, "value": mode} for mode in cytoData.node_types],
                    multi=True,
                    value=default_mode,
                    style= {'background-color':'#299FD6', "border": "0px", "border-radius":"5px"}
                ),
        ], className="ms-3", style={"width": "48%"}),
        
        dbc.Card([
            dbc.CardBody([
                html.Div(id="bigdata-dummy-output"),
                html.Div(id="bigdata-container", style={"width": "100%", "height": "1000px"}),
                html.Link(rel="stylesheet", type="text/css", href=config['Cytoscape']['qtip_css']),
                dbc.Row([
                    dbc.Col([
                        dbc.Button("Download Image", id="bigdata-download-btn", n_clicks=0),
                    ]),
                    dbc.Col([
                        dcc.Dropdown(
                            id="bigdata-layout-dropdown",
                            options=layout_options,
                            value=default_layout,
                            clearable=False,
                            style=layout_options_style
                        )
                    ])
                ]),
            ]),
        ], style=card_style, outline=True, color="primary", className="ms-3"),

        dbc.Col([
            dmc.Title(id = "bigdata-graph-data", order=3),
            dbc.Card(style={"width": "400px", "height":"250px"}, outline=True, color="primary", 
                        className="ms-1",children=[
                dmc.ScrollArea(w=385, h=250, type='hover', id = "multi-mode-scroll-area",children=[
                    dbc.Tabs([
                        dbc.Tab(html.Pre(id="bigdata-edges"), label="Edges"),
                        dbc.Tab(html.Pre(id="bigdata-nodes"), label="Nodes")
                    ])
                ]),
                dcc.Clipboard(target_id="bigdata-scroll-area", className="ms-auto me-3")
            ])
        ], className="ms-3", id="bigdata-jsons"),
    ])
    return html.Div([nav_bar, content])

@callback(
    [Output("bigdata-nodes", "children"),
    Output("bigdata-edges", "children"),
    Output("bigdata-graph-data", "children")],
    Input("bigdata-dropdown", "value")
)
def update_bigdata_data(selected_modes):
    nodes, nodes_count = [], 0
    edges, edges_count = [], 0
    for edge in cytoData.cy_edges:
        if edge["data"]["source_type"] in selected_modes and edge["data"]["target_type"] in selected_modes:
            edges.append(edge)
            edges_count += 1
    for node in cytoData.cy_nodes:
        if node["classes"] in selected_modes:
            nodes.append(node)
            nodes_count += 1
    if not nodes:
        nodes = "No data"
    if not edges:
        edges = "No data"
    return json.dumps(nodes, indent=2), json.dumps(edges, indent=2), f"Graph Data: {nodes_count} Nodes, {edges_count}  Edges"

with open('assets/bigdata.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("bigdata-dummy-output", "children"),
    [Input("bigdata-dummy-output", "children"),
    Input("bigdata-dropdown", "value")]
)

clientside_callback(
    """
    function(n_clicks) {
        const png = cyBigdata.png({ output: 'blob', bg: 'black', full: true });
        const url = URL.createObjectURL(png);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'filter_mode.jpg';

        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }
    """,
    Output("bigdata-dummy-output", "data"),
    Input("bigdata-download-btn", "n_clicks"),
    prevent_initial_call=True
)

clientside_callback(
    """
    function(value) {
        cyBigdata.layout({name: value}).run();
    }
    """,
    Output("bigdata-container", "children"),
    Input("bigdata-layout-dropdown", "value"),
    prevent_initial_call=True
)
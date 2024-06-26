from dash import Input, Output, dcc, html, callback, register_page, clientside_callback
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from view import dash_reusable_components as drc
from view import navbar
from data.authors import nodes, edges
import json

register_page(__name__)

default_dropdown_values = ["Paper", "Conference"]

# Create multi-mode graph elements
multi_mode_nodes = [
    {"data": {"id": node, "label": node}, "classes": mode.lower()} 
    for mode, node_list in nodes.items() 
    for node in node_list
]

multi_mode_edges = [
    {"data": {"source": edge[0], "target": edge[1]}} for edge in edges
]


# Function to perform the n-mode to one-mode transformation
def n_mode_to_one_mode(nodes, edges, target_mode, other_modes):
    target_nodes = nodes[target_mode]
    other_nodes = {node for mode in other_modes for node in nodes[mode]}
    
    one_mode_edges = []
    for i, node1 in enumerate(target_nodes):
        for j, node2 in enumerate(target_nodes):
            if i < j:
                shared_neighbors = [
                    other_node for other_node in other_nodes 
                    if ((node1, other_node) in edges or (other_node, node1) in edges)
                    and ((node2, other_node) in edges or (other_node, node2) in edges)
                ]
                if shared_neighbors:
                    one_mode_edges.append((node1, node2, len(shared_neighbors), shared_neighbors))
    return one_mode_edges

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

    content = html.Div([
                    html.Div([
                        html.Label("Select Modes to Consider:"),
                        dcc.Dropdown(
                                id="mode-dropdown",
                                options=[{"label": mode, "value": mode} for mode in nodes.keys() if mode != "Author"],
                                value=default_dropdown_values,
                                multi=True
                            ),
                        ], className="ms-3", style={"width": "48%"}),
                        
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader("Filter-Mode Graph", 
                                                className="text-center",
                                                style=card_header_style),
                                dbc.CardBody([
                                    html.Div(id="filter-mode-dummy-output"),
                                    html.Div(id="filter-mode-container", style={"width": "100%", "height": "500px"}),
                                    dbc.Button("Download Image", id="filter-graph-download-btn", n_clicks=0),
                                ])
                            ], style=card_style, outline=True, color="primary", className="ms-3"),
                        ]),

                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader("One-Mode Graph", 
                                                className="text-center",
                                                style=card_header_style),
                                dbc.CardBody([
                                    html.Div(id="one-mode-dummy-output"),
                                    html.Div(id="one-mode-container", style={"width": "100%", "height": "500px"}),
                                    dbc.Button("Download Image", id="one-graph-download-btn", n_clicks=0),
                                ])
                            ], style=card_style, outline=True, color="primary", className="ms-3"),
                        ]),
                    ]),

                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardHeader("Multi-Mode Graph", 
                                                className="text-center",
                                                style=card_header_style),
                                dbc.CardBody([
                                    html.Div(id="multi-mode-dummy-output"),
                                    html.Div(id="multi-mode-container", style={"width": "100%", "height": "500px"}),
                                    dbc.Button("Download Image", id="multi-graph-download-btn", n_clicks=0),
                                ])
                            ], style=card_style, outline=True, color="primary", className="ms-3"),
                        ]),
                    ]),

                    dbc.Row([
                        dbc.Col([
                                dmc.Title("Filter-Mode Graph Data", order=3),
                                dbc.Card(style={"width": "350px", "height":"250px"}, outline=True, color="primary", 
                                            className="ms-1",children=[
                                    dmc.ScrollArea(h=250, w=335, type='hover', id = "filter-mode-scroll-area",children=[
                                        dbc.Tabs([
                                            dbc.Tab(html.Pre(id="filter-mode-edges"), label="Edges"),
                                            dbc.Tab(html.Pre(id="filter-mode-nodes"),label="Nodes")
                                        ])
                                    ]),
                                    dcc.Clipboard(target_id="filter-mode-scroll-area", className="ms-auto me-3")
                                ])
                            ], className="ms-3", id="filter-mode-jsons"),
                        dbc.Col([
                                dmc.Title("One-Mode Graph Data", order=3),
                                dbc.Card(style={"width": "350px", "height":"250px"}, outline=True, color="primary", 
                                            className="ms-1",children=[
                                    dmc.ScrollArea(h=250, w=335, type='hover', id = "one-mode-scroll-area",children=[
                                        dbc.Tabs([
                                            dbc.Tab(html.Pre(id="one-mode-edges"), label="Edges"),
                                            dbc.Tab(html.Pre(id="one-mode-nodes"),label="Nodes")
                                        ])
                                    ]),
                                    dcc.Clipboard(target_id="one-mode-scroll-area", className="ms-auto me-3")
                                ])
                            ], className="ms-3", id="one-mode-jsons"),
                        dbc.Col([
                                dmc.Title("Multi-Mode Graph Data", order=3),
                                dbc.Card(style={"width": "350px", "height":"250px"}, outline=True, color="primary", 
                                            className="ms-1",children=[
                                    dmc.ScrollArea(h=250, w=335, type='hover', id = "multi-mode-scroll-area",children=[
                                        dbc.Tabs([
                                            dbc.Tab(html.Pre(id="multi-mode-edges", children=json.dumps(multi_mode_edges, indent=2)), label="Edges"),
                                            dbc.Tab(html.Pre(id="multi-mode-nodes", children=json.dumps(multi_mode_nodes, indent=2)), label="Nodes")
                                        ])
                                    ]),
                                    dcc.Clipboard(target_id="multi-mode-scroll-area", className="ms-auto me-3")
                                ])
                            ], className="ms-3", id="multi-mode-jsons"),
                    ]),
                ])
    return html.Div([nav_bar, content])

with open('assets/multi_mode.js', 'r') as file:
    js_code = file.read()

clientside_callback(
    js_code,
    Output("multi-mode-dummy-output", "children"),
    [Input("multi-mode-dummy-output", "children"),
    Input("mode-dropdown", "value")]
)

clientside_callback(
    """
    function(n_clicks) {
        const png = cyFilter.png({ output: 'blob', bg: 'black', full: true });
        const url = URL.createObjectURL(png);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'filter_mode.jpg';

        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }
    """,
    Output("filter-mode-dummy-output", "data"),
    Input("filter-graph-download-btn", "n_clicks"),
    prevent_initial_call=True
)

clientside_callback(
    """
    function(n_clicks) {
        const png = cyOne.png({ output: 'blob', bg: 'black', full: true });
        const url = URL.createObjectURL(png);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'one_mode.jpg';

        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }
    """,
    Output("one-mode-dummy-output", "data"),
    Input("one-graph-download-btn", "n_clicks"),
    prevent_initial_call=True
)

clientside_callback(
    """
    function(n_clicks) {
        const png = cyMulti.png({ output: 'blob', bg: 'black', full: true });
        const url = URL.createObjectURL(png);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'multi_mode.jpg';

        link.click();
        document.body.removeChild(link);
        URL.revokeObjectURL(url);
    }
    """,
    Output("multi-mode-dummy-output", "data"),
    Input("multi-graph-download-btn", "n_clicks"),
    prevent_initial_call=True
)

@callback(
    [Output("one-mode-nodes", "children"),
    Output("one-mode-edges", "children"), 
    Output("filter-mode-edges", "children"),
    Output("filter-mode-nodes", "children")],
    Input("mode-dropdown", "value")
)
def update_one_mode_graph_and_data(selected_modes):
    one_mode_edges = n_mode_to_one_mode(nodes, edges, "Author", selected_modes)

    # Create JSON data for one-mode graph
    one_mode_edges_data = [{"data": {"source": edge[0], "target": edge[1], "weight": edge[2], "shared": edge[3]}} for edge in one_mode_edges]
    one_mode_nodes_data = [{"data": {"id": node, "label": node}, "classes": "author"} for node in nodes["Author"]]

    # Create JSON data for filter-mode graph
    filter_mode_nodes = [
        {"data": {"id": node, "label": node}, "classes": mode.lower()} 
        for mode, node_list in nodes.items() if mode in selected_modes + ["Author"]
        for node in node_list
    ]
    filter_mode_edges = [
        {"data": {"source": edge[0], "target": edge[1]}} 
        for edge in edges 
        if edge[0] in [node["data"]["id"] for node in filter_mode_nodes] 
        and edge[1] in [node["data"]["id"] for node in filter_mode_nodes]
    ]
    return (json.dumps(one_mode_nodes_data, indent=2), json.dumps(one_mode_edges_data, indent=2), 
            json.dumps(filter_mode_edges, indent=2), json.dumps(filter_mode_nodes, indent=2))

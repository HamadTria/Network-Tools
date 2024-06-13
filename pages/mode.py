from dash import Input, Output, dcc, html, callback, register_page
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from view import dash_reusable_components as drc
from view import navbar
from data.authors import nodes, edges

register_page(__name__)

# Create multi-mode graph elements
multi_mode_elements = [
    {"data": {"id": node, "label": node}, "classes": mode.lower()} 
    for mode, node_list in nodes.items() 
    for node in node_list
] + [
    {"data": {"source": edge[0], "target": edge[1]}} for edge in edges
]

# Function to perform the n-mode to one-mode transformation
def n_mode_to_one_mode(nodes, edges, target_mode, other_modes):
    """Transforms an n-mode graph to a one-mode graph by considering the shared neighbors between target_mode nodes.
    
    Args:
        nodes (dict): A dictionary of nodes for each mode.
        edges (list): A list of edges between nodes in different modes.
        target_mode (str): The target mode to consider.
        other_modes (list): A list of modes to consider for shared neighbors.
        
    Returns:
        list: A list of edges between target_mode nodes.
    """
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
                    one_mode_edges.append((node1, node2, len(shared_neighbors)))
    return one_mode_edges

def layout():
    card_style = {
        "margin": "1rem",
        "boxShadow": "0px 0px 15px rgba(0,0,0,0.2)",
        "width": "48%", 
        "display": "inline-block", 
        "vertical-align": "top"
    }

    card_header_style = {
        "fontSize": "1.5rem",
        "fontWeight": "bold",
        "color": "#FFFFFF",
    }

    content = html.Div([
                        html.Div([
                            dbc.Card([
                                dbc.CardHeader("Multi-Mode Graph", 
                                               className="text-center",
                                               style=card_header_style),
                                dbc.CardBody(
                                    cyto.Cytoscape(
                                        id="multi-mode-graph",
                                        elements=multi_mode_elements,
                                        style={"width": "100%", "height": "500px"},
                                        layout={"name": "breadthfirst"},
                                        stylesheet=[
                                            {"selector": ".author", "style": {"background-color": "lightblue", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": ".paper", "style": {"background-color": "lightgreen", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": ".conference", "style": {"background-color": "lightcoral", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": ".book", "style": {"background-color": "lightyellow", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": ".institution", "style": {"background-color": "lightpink", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": ".journal", "style": {"background-color": "red", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": ".publisher", "style": {"background-color": "purple", "label": "data(label)", 'color': '#fff',}},
                                            {"selector": "edge", "style": {"line-color": "#aaa"}},
                                        ]
                                    )   
                                )
                            ], style=card_style, outline=True, color="primary"),
                            dbc.Card([
                                dbc.CardHeader("One-Mode Graph",
                                            className="text-center",
                                            style=card_header_style),
                                dbc.CardBody(
                                    cyto.Cytoscape(
                                        id="one-mode-graph",
                                        elements=[],
                                        style={"width": "100%", "height": "500px"},
                                        layout={"name": "cose"},
                                        stylesheet=[
                                            {"selector": ".author", "style": {"background-color": "lightblue", "label": "data(label)", 'color': '#fff'}},
                                            {"selector": "edge", "style": {"line-color": "#aaa", "label": "data(weight)", 'color': '#fff'}}
                                        ]
                                    )
                                )
                            ], style=card_style, outline=True, color="primary",)
                        ]),
                        html.Div([html.Label("Select Modes to Consider:"),
                                dcc.Dropdown(
                                        id="mode-dropdown",
                                        options=[{"label": mode, "value": mode} for mode in nodes.keys() if mode != "Author"],
                                        value=["Paper", "Conference"],
                                        multi=True
                                    ),
                                ], className="ms-3", style={"width": "48%"}),
                ])
    return html.Div([navbar.draw_navbar(), content])

@callback(
    Output("one-mode-graph", "elements"),
    Input("mode-dropdown", "value")
)
def update_one_mode_graph(selected_modes):
    one_mode_edges = n_mode_to_one_mode(nodes, edges, "Author", selected_modes)
    one_mode_elements = [
        {"data": {"id": node, "label": node}, "classes": "author"} for node in nodes["Author"]
    ] + [
        {"data": {"source": edge[0], "target": edge[1], "weight": edge[2]}} for edge in one_mode_edges
    ]
    return one_mode_elements
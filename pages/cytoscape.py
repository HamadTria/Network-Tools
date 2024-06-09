import json
import dash
from dash import Input, Output, State, dcc, html, callback, register_page
import dash_cytoscape as cyto
import dash_bootstrap_components as dbc
from view import dash_reusable_components as drc
from view import navbar
from data import cytoData

cyto.load_extra_layouts()

register_page(__name__)

context_menu = [
    {
        "id": "add-node",
        "label": "Add Node",
        "tooltipText": "Add Node",
        "availableOn": ["canvas"],
        "onClick": "add_node",
    },
    {
        "id": "remove",
        "label": "Remove",
        "tooltipText": "Remove",
        "availableOn": ["node", "edge"],
        "onClick": "remove",
    },
    {
        "id": "add-edge",
        "label": "Add Edge",
        "tooltipText": "add edge",
        "availableOn": ["node"],
        "onClick": "add_edge",
    },
]

default_stylesheet = [
    {   
        "selector": "node", 
        "style": {"opacity": 0.65, 
                  "z-index": 9999}
    },
    {
        "selector": "edge",
        "style": {'width': 'data(weight)', 
                  "curve-style": "bezier", 
                  "opacity": 0.65, 
                  "z-index": 5000},
    },
    {
        "selector": ".followerEdge",
        "style": {
            "mid-target-arrow-color": "white",
            "mid-target-arrow-shape": "vee",
            "line-color": "#0074D9",
        },
    },
    {
        "selector": ".followingEdge",
        "style": {
            "mid-target-arrow-color": "red",
            "mid-target-arrow-shape": "vee",
            "line-color": "#FF4136",
        },
    },
    {
        "selector": ".genesis",
        "style": {
            "background-color": "#B10DC9",
            "border-width": 2,
            "border-color": "purple",
            "border-opacity": 1,
            "opacity": 1,
            "label": "data(label)",
            "color": "#75abd2",
            "text-opacity": 1,
            "font-size": 12,
            "z-index": 9999,
        },
    },
    {
        "selector": ":selected",
        "style": {
            "border-width": 2,
            "border-color": "black",
            "border-opacity": 1,
            "opacity": 1,
            "label": "data(label)",
            "color": "#75abd2",
            "font-size": 12,
            "z-index": 9999,
        },
    },
]

styles = {
    "json-output": {
        "overflow-y": "scroll",
        "height": "calc(50% - 25px)",
        "border": "thin lightgrey solid",
    },
    "tab": {"height": "calc(98vh - 80px)"},
}

def layout():
    nav_bar = navbar.draw_navbar()
    return html.Div(
    [   nav_bar,
        dbc.Row([
            dbc.Col(html.Div(
                        className="eight columns",
                        children=[
                            cyto.Cytoscape(
                                id="cytoscape",
                                elements=cytoData.default_elements,
                                stylesheet=default_stylesheet,
                                style={"height": "95vh", "width": "100%"},
                                contextMenu=context_menu,
                            )
                        ],
                    ),
                    width=8
            ),
            dbc.Col(
                dbc.Card(
                    html.Div(
                            className="four columns",
                            children=[
                                dcc.Tabs(
                                    id="tabs",
                                    children=[
                                        dcc.Tab(
                                            label="Control Panel",
                                            children=[
                                                drc.NamedDropdown(
                                                    name="Layout",
                                                    id="dropdown-layout",
                                                    options=drc.DropdownOptionsList(
                                                        "random",
                                                        "grid",
                                                        "circle",
                                                        "concentric",
                                                        "breadthfirst",
                                                        "cose",
                                                        "cose-bilkent",
                                                        "dagre",
                                                        "cola",
                                                        "klay",
                                                        "spread",
                                                        "euler",
                                                    ),
                                                    value="random",
                                                    clearable=False
                                                ),
                                                drc.NamedRadioItems(
                                                    name="Expand",
                                                    id="radio-expand",
                                                    options=drc.DropdownOptionsList(
                                                        "followers", "following"
                                                    ),
                                                    value="followers",
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ]
                    )
                )
            )
        ])
    ]
)


@callback(Output("tap-node-json-output", "children"), Input("cytoscape", "tapNode"))
def display_tap_node(data):
    return json.dumps(data, indent=2)


@callback(Output("tap-edge-json-output", "children"), Input("cytoscape", "tapEdge"))
def display_tap_edge(data):
    return json.dumps(data, indent=2)


@callback(Output("cytoscape", "layout"), Input("dropdown-layout", "value"))
def update_cytoscape_layout(layout):
    return {"name": layout}


@callback(
    Output("cytoscape", "elements"),
    Input("cytoscape", "tapNodeData"),
    State("cytoscape", "elements"),
    State("radio-expand", "value"),
)
def generate_elements(nodeData, elements, expansion_mode):
    if not nodeData:
        return cytoData.default_elements

    # If the node has already been expanded, we don't expand it again
    if nodeData.get("expanded"):
        return elements

    # This retrieves the currently selected element, and tag it as expanded
    for element in elements:
        if nodeData["id"] == element.get("data").get("id"):
            element["data"]["expanded"] = True
            break

    if expansion_mode == "followers":
        followers_nodes = cytoData.followers_node_di.get(nodeData["id"])
        followers_edges = cytoData.followers_edges_di.get(nodeData["id"])

        if followers_nodes:
            for node in followers_nodes:
                node["classes"] = "followerNode"
            elements.extend(followers_nodes)

        if followers_edges:
            for follower_edge in followers_edges:
                follower_edge["classes"] = "followerEdge"
            elements.extend(followers_edges)

    elif expansion_mode == "following":
        following_nodes = cytoData.following_node_di.get(nodeData["id"])
        following_edges = cytoData.following_edges_di.get(nodeData["id"])

        if following_nodes:
            for node in following_nodes:
                if node["data"]["id"] != cytoData.genesis_node["data"]["id"]:
                    node["classes"] = "followingNode"
                    elements.append(node)

        if following_edges:
            for follower_edge in following_edges:
                follower_edge["classes"] = "followingEdge"
            elements.extend(following_edges)

    return elements
from dash import html, clientside_callback, register_page
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from view import navbar
import time

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
                    html.Div(id="cyto-container-compare", style={"width": "100%", "height": "500px"})
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
                        dbc.Col(dbc.Card(card_content_sigma, 
                                        color="primary",
                                        outline=True,
                                        style=card_style)), 
                        dbc.Col(dbc.Card(card_content_cyto,
                                        color="primary",
                                        outline=True,
                                        style=card_style))
                        ])
    return html.Div([nav_bar, contents])

clientside_callback(
    """
    function() {

        let start = Date.now();

        var container = document.getElementById('sigma-container-compare');

        while (container.firstChild) {
            container.removeChild(container.firstChild);
        }

        var s = new sigma({
            renderer: {
                container: container,
                type: 'webgl'
            },
        });

        var graphData = {
            nodes: [
                { id: "n0", label: "Node A", x: 0, y: 0, size: 3, color: '#75abd2' },
                { id: "n1", label: "Node B", x: 3, y: 1, size: 3, color: '#75abd2' },
                { id: "n2", label: "Node C", x: 1, y: 3, size: 3, color: '#75abd2' },
                { id: "n3", label: "Node D", x: 4, y: 2, size: 3, color: '#75abd2' },
                { id: "n4", label: "Node E", x: 2, y: 4, size: 3, color: '#75abd2' },
                { id: "n5", label: "Node F", x: 3, y: 3, size: 3, color: '#75abd2' },
                { id: "n6", label: "Node G", x: 0, y: 5, size: 3, color: '#75abd2' },
                { id: "n7", label: "Node H", x: 4, y: 4, size: 3, color: '#75abd2' },
                { id: "n8", label: "Node I", x: 5, y: 1, size: 3, color: '#75abd2' }
            ],
            edges: [
                { id: "e0", source: "n0", target: "n1", color: '#75abd2', type: 'line', size: 2 },
                { id: "e1", source: "n1", target: "n2", color: '#75abd2', type: 'curve', size: 2 },
                { id: "e2", source: "n2", target: "n0", color: '#75abd2', type: 'line', size: 2 },
                { id: "e3", source: "n1", target: "n3", color: '#75abd2', type: 'line', size: 2 },
                { id: "e4", source: "n3", target: "n4", color: '#75abd2', type: 'curve', size: 2 },
                { id: "e5", source: "n4", target: "n5", color: '#75abd2', type: 'line', size: 2 },
                { id: "e6", source: "n5", target: "n6", color: '#75abd2', type: 'curve', size: 2 },
                { id: "e7", source: "n6", target: "n7", color: '#75abd2', type: 'line', size: 2 },
                { id: "e8", source: "n7", target: "n8", color: '#75abd2', type: 'curve', size: 2 },
                { id: "e9", source: "n8", target: "n0", color: '#75abd2', type: 'line', size: 2 }
            ]
        };

        s.graph.read(graphData);

        s.refresh();

        let timeTaken = Date.now() - start;

        // Print the time taken to render the graph
        let timeText = document.createElement("p");
        timeText.innerText = "Time taken: " + timeTaken + "ms";
        timeText.style.position = "absolute";
        timeText.style.bottom = "10px";
        timeText.style.left = "10px";
        timeText.style.color = "#FFFFFF";
        timeText.style.fontSize = "0.8rem";
        container.appendChild(timeText);
    }
    """,
    Output("sigma-compare", "children"),
    Input("sigma-compare", "children"),
)

clientside_callback(
    """
    function initializeCytoscape() {
        
        let start = Date.now();

        var cy = window.cy = cytoscape({
            container: document.getElementById('cyto-container-compare'),
            ready: function(){
            },
            style: [
						{
							selector: 'node',
							css: {
								'content': 'data(label)',
                                'background-color': '#75abd2',
                                'color': '#fff',
                            }
						},

						{
							selector: 'edge',
							css: {
								'curve-style': 'bezier',
								'target-arrow-shape': 'triangle'
                                
							}
						}
					],
                                        
			layout: {name: 'preset'},
                                        
            elements: {
						nodes: [
                                {'data': {'id': 'n0', 'label': 'Node A'}, 'position': {'x': 0, 'y': 0}},
                                {'data': {'id': 'n1', 'label': 'Node B'}, 'position': {'x': 300, 'y': 100}},
                                {'data': {'id': 'n2', 'label': 'Node C'}, 'position': {'x': 100, 'y': 300}},
                                {'data': {'id': 'n3', 'label': 'Node D'}, 'position': {'x': 400, 'y': 200}},
                                {'data': {'id': 'n4', 'label': 'Node E'}, 'position': {'x': 200, 'y': 400}},
                                {'data': {'id': 'n5', 'label': 'Node F'}, 'position': {'x': 300, 'y': 300}},
                                {'data': {'id': 'n6', 'label': 'Node G'}, 'position': {'x': 0, 'y': 500}},
                                {'data': {'id': 'n7', 'label': 'Node H'}, 'position': {'x': 400, 'y': 400}},
                                {'data': {'id': 'n8', 'label': 'Node I'}, 'position': {'x': 500, 'y': 100}},
						],
						edges: [
                                {'data': {'source': 'n0', 'target': 'n1'}},
                                {'data': {'source': 'n1', 'target': 'n2'}},
                                {'data': {'source': 'n2', 'target': 'n0'}},
                                {'data': {'source': 'n1', 'target': 'n3'}},
                                {'data': {'source': 'n3', 'target': 'n4'}},
                                {'data': {'source': 'n4', 'target': 'n5'}},
                                {'data': {'source': 'n5', 'target': 'n6'}},
                                {'data': {'source': 'n6', 'target': 'n7'}},
                                {'data': {'source': 'n7', 'target': 'n8'}},
                                {'data': {'source': 'n8', 'target': 'n0'}}
						]
					}
        });

        let timeTaken = Date.now() - start;

        // Print the time taken to render the graph
        let timeText = document.createElement("p");
        timeText.innerText = "Time taken: " + timeTaken + "ms";
        timeText.style.position = "absolute";
        timeText.style.bottom = "10px";
        timeText.style.left = "10px";
        timeText.style.color = "#FFFFFF";
        timeText.style.fontSize = "0.8rem";
        document.getElementById('cyto-container-compare').appendChild(timeText);
    }
    """,
    Output("cytos-compare", "children"),
    Input("cytos-compare", "children"),
)

# from dash import html, clientside_callback, register_page, dcc
# from dash.dependencies import Input, Output
# from view import navbar

# register_page(__name__)

# def layout():
#     nav_bar = navbar.draw_navbar()
    
#     contents = html.Div([
#         html.Div(id="dummy-output"),
#         dcc.Store(id="graph-data", data={}),
#         html.Div(id="sigma-container", style={"width": "100%", "height": "500px", "border": "1px solid #ccc"}),
#         html.Button(id="center-graph-button", children="Center Graph"),
#         html.Div(id="node-info", style={"margin-top": "20px", "font-size": "16px"}),
#         html.Label("Select Graph:"),
#         dcc.Dropdown(id="graph-selector", options=[
#             {"label": "Graph 1", "value": "graph1"},
#             {"label": "Graph 2", "value": "graph2"}
#         ], value="graph1")
#     ])
#     return html.Div([nav_bar, contents])

# clientside_callback(
#     """
#     function(nClicks, selectedGraph) {
#         var container = document.getElementById('sigma-container');
#         while (container.firstChild) {
#             container.removeChild(container.firstChild);
#         }

#         var s = new sigma({
#             renderer: {
#                 container: container,
#                 type: 'webgl'
#             },
#         });

#         var graphData = {
#             graph1: {
#                 nodes: [
#                     { id: "n0", label: "Node A", x: 0, y: 0, size: 3, color: '#75abd2' },
#                     { id: "n1", label: "Node B", x: 3, y: 1, size: 3, color: '#75abd2' },
#                     { id: "n2", label: "Node C", x: 1, y: 3, size: 3, color: '#75abd2' },
#                     { id: "n3", label: "Node D", x: 4, y: 2, size: 3, color: '#75abd2' },
#                     { id: "n4", label: "Node E", x: 2, y: 4, size: 3, color: '#75abd2' },
#                     { id: "n5", label: "Node F", x: 3, y: 3, size: 3, color: '#75abd2' },
#                     { id: "n6", label: "Node G", x: 0, y: 5, size: 3, color: '#75abd2' },
#                     { id: "n7", label: "Node H", x: 4, y: 4, size: 3, color: '#75abd2' },
#                     { id: "n8", label: "Node I", x: 5, y: 1, size: 3, color: '#75abd2' }
#                 ],
#                 edges: [
#                     { id: "e0", source: "n0", target: "n1", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e1", source: "n1", target: "n2", color: '#75abd2', type: 'curve', size: 2 },
#                     { id: "e2", source: "n2", target: "n0", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e3", source: "n1", target: "n3", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e4", source: "n3", target: "n4", color: '#75abd2', type: 'curve', size: 2 },
#                     { id: "e5", source: "n4", target: "n5", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e6", source: "n5", target: "n6", color: '#75abd2', type: 'curve', size: 2 },
#                     { id: "e7", source: "n6", target: "n7", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e8", source: "n7", target: "n8", color: '#75abd2', type: 'curve', size: 2 },
#                     { id: "e9", source: "n8", target: "n0", color: '#75abd2', type: 'line', size: 2 }
#                 ]
#             },
#             graph2: {
#                 nodes: [
#                     { id: "n9", label: "Node J", x: 0, y: 0, size: 3, color: '#d27575' },
#                     { id: "n10", label: "Node K", x: 2, y: 2, size: 3, color: '#d27575' },
#                     { id: "n11", label: "Node L", x: 4, y: 0, size: 3, color: '#d27575' },
#                     { id: "n12", label: "Node M", x: 1, y: 3, size: 3, color: '#d27575' },
#                     { id: "n13", label: "Node N", x: 3, y: 4, size: 3, color: '#d27575' },
#                     { id: "n14", label: "Node O", x: 5, y: 2, size: 3, color: '#d27575' },
#                     { id: "n15", label: "Node P", x: 4, y: 3, size: 3, color: '#d27575' }
#                 ],
#                 edges: [
#                     { id: "e10", source: "n9", target: "n10", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e11", source: "n10", target: "n11", color: '#75abd2', type: 'curve', size: 2 },
#                     { id: "e12", source: "n11", target: "n12", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e13", source: "n12", target: "n13", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e14", source: "n13", target: "n14", color: '#75abd2', type: 'curve', size: 2 },
#                     { id: "e15", source: "n14", target: "n15", color: '#75abd2', type: 'line', size: 2 },
#                     { id: "e16", source: "n15", target: "n9", color: '#75abd2', type: 'curve', size: 2 }
#                 ]
#             }
#         };

#         s.graph.read(graphData[selectedGraph]);

#         s.bind('overNode', function(e) {
#             var node = e.data.node;
#             document.getElementById('node-info').innerHTML = 'Hovered over node: ' + node.label;
#         });

#         s.bind('clickNode', function(e) {
#             var node = e.data.node;
#             alert('Clicked on node: ' + node.label);
#         });

#         s.refresh();
#     }
#     """,
#     Output("dummy-output", "children"),
#     Input("center-graph-button", "n_clicks"),
#     Input("graph-selector", "value"),
#     prevent_initial_call=False
# )

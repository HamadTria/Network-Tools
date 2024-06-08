import json
from dash import Input, Output, html, clientside_callback, register_page

import dash_cytoscape as cyto
from view import navbar

cyto.load_extra_layouts()

register_page(__name__)

def layout():
        nav_bar = navbar.draw_navbar()
        cyto = html.Div([
                    html.Div(id="dummy-output-cytos"),
                    html.Div(id="cyto-container", style={"width": "100%", "height": "1000px"}),
                    html.Script(src="assets/cytoscape-cxtmenu.js")])
        return html.Div([nav_bar, cyto])

clientside_callback(
    """
    function initializeCytoscape() {
        var cy = window.cy = cytoscape({
            container: document.getElementById('cyto-container'),
            ready: function(){
            },
            style: [
						{
							selector: 'node',
							css: {
								'content': 'data(name)',
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

        cy.cxtmenu({
					selector: 'node, edge',

					commands: [
						{
							content: 'expand node',
							select: function(ele){
								console.log( ele.id() );
							}
						},

						{
							content: 'isolate node',
							select: function(ele){
								console.log(ele.data('name'));
							},
						},

						{
							content: 'change shape',
							select: function(ele){
								console.log(ele.position());
							}
						},
                                                
                        {
							content: 'change size',
							select: function(ele){
								console.log( ele.position() );
							}
						}
					]
				});
                                
        cy.cxtmenu({
					selector: 'core',

					commands: [
						{
							content: 'bg1',
							select: function(){
								console.log( 'bg1' );
							}
						},

						{
							content: 'bg2',
							select: function(){
								console.log( 'bg2' );
							}
						}
					]
				});
    }
    """,
    Output("dummy-output-cytos", "children"),
    Input("dummy-output-cytos", "children")
)
        
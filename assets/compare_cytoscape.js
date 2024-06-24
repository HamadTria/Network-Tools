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
                            'target-arrow-shape': 'none',
                            'line-color': '#75abd2',
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
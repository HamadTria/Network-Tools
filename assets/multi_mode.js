function initializeCytoscape() {
    var multi_mode_nodes = JSON.parse(document.getElementById('multi-mode-nodes').textContent);
    var multi_mode_edges = JSON.parse(document.getElementById('multi-mode-edges').textContent);
    
    // Create a new Cytoscape instance for multi-mode graph
    var cyMulti = window.cyMulti = cytoscape({
        container: document.getElementById('multi-mode-container'),
        ready: function(){},
        style: [
            {
                selector: 'node',
                css: {
                    'content': 'data(label)',
                    "font-size": "30px",
                    'background-color': 'lightblue',
                    'color': '#fff',
                    'shape': 'ellipse',
                    'width': '50px',
                    'height': '50px'
                }
            },
            {
                selector: '.author',
                css: {
                    'background-color': 'lightblue',
                    'width': '100px',
                    'height': '100px'
                }
            },
            {
                selector: '.paper',
                css: {
                    'background-color': 'lightgreen',
                }
            },
            {
                selector: '.conference',
                css: {
                    'background-color': 'purple',
                }
            },
            {
                selector: '.book',
                css: {
                    'background-color': 'lightyellow',
                }
            },
            {
                selector: '.institution',
                css: {
                    'background-color': 'lightpink',
                }
            },
            {
                selector: '.journal',
                css: {
                    'background-color': 'orange',
                }
            },
            {
                selector: '.publisher',
                css: {
                    'background-color': 'lightcoral',
                }
            },
            {
                selector: 'edge',
                css: {
                    'line-color': '#aaa',
                    'curve-style': 'bezier', // bezier curve control point to show curvature
                    'target-arrow-shape': 'triangle'
                }
            },
            {
                selector: 'node:selected',
                css: {
                    'background-color': '#4c7dab'
                }
            }
        ],
        layout: {name: 'breadthfirst'},
        elements: {
            nodes: multi_mode_nodes,
            edges: multi_mode_edges
        }
    });

    // Store original colors
    cyMulti.nodes().forEach(node => {
        node.data('originalColor', node.style('background-color'));
    });


    // Context menu for graphs
    cyMulti.cxtmenu({
        selector: 'node, edge',
        commands: [
            {
                content: 'change size',
                select: function(ele){
                    if (ele.style('width') === '100'){
                        ele.animate({
                            style: { 'width': '50px', 'height': '50px' }
                        }, { duration: 500 });
                    } else {
                        ele.animate({
                            style: { 'width': '100px', 'height': '100px' }
                        }, { duration: 500 });
                    }
                }
            },
            {
                content: 'isolate node',
                select: function(ele){
                    let connectedNodesAndEdges = ele.connectedEdges().connectedNodes().union(ele.connectedEdges()).union(ele);
                    if (cyMulti.elements().not(connectedNodesAndEdges).style('visibility') === 'hidden') {

                        cyMulti.elements().not(connectedNodesAndEdges).show();
                        cyMulti.elements().not(connectedNodesAndEdges).style('visibility', 'visible');

                    } else {
                        cyMulti.elements().not(connectedNodesAndEdges).hide();
                        cyMulti.elements().not(connectedNodesAndEdges).style('visibility', 'hidden');
                    }
                }
            },
            {
                content: 'change shape',
                select: function(ele){
                    if (ele.style('shape') === 'square') {
                        ele.style('shape', 'ellipse');
                    } else {
                        ele.style('shape', 'square');
                    }
                }
            },
            {
                content: 'mark node',
                select: function(ele){
                    if (ele.style('background-color') === 'rgb(255,0,0)') {
                        ele.style('background-color', ele.data('originalColor'));
                    } else {
                        ele.style('background-color', 'red');
                    }
                }
            },
            {
                content: 'delete',
                select: function(ele){
                    ele.hide();
                    ele.style('visibility', 'hidden');
                }
            },
        ]
    });

    cyMulti.cxtmenu({
        selector: 'core',
        commands: [
            {
                content: 'bg1',
                select: function(){
                    for (let node of cyMulti.nodes()) {
                        if (node.style('background-color') === 'rgb(173,216,230)') {
                            node.style('background-color', node.data('originalColor'));
                        } else {
                            node.style('background-color', 'rgb(173,216,230)');
                        }
                    }
                }
            },
            {
                content: 'bg2',
                select: function(){
                    for (let node of cyMulti.nodes()) {
                        if (node.style('background-color') === 'rgb(144,238,144)') {
                            node.style('background-color', node.data('originalColor'));
                        } else {
                            node.style('background-color', 'rgb(144,238,144)');
                        }
                    }
                }
            },
            {
                content: 'bring back nodes',
                select: function(){
                    cyMulti.elements().show();
                    cyMulti.elements().style('visibility', 'visible');
                }
            }
        ]
    });
};

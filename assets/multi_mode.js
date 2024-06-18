function initializeCytoscape() {
    // Delay the initialization to ensure that elements are available in the DOM
    var nodes = JSON.parse(document.getElementById('multi-mode-nodes').textContent);
    var edges = JSON.parse(document.getElementById('multi-mode-edges').textContent);
    
    var cy = window.cy = cytoscape({
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
            nodes: nodes,
            edges: edges
        }
    });

    // Store original colors
    cy.nodes().forEach(node => {
        node.data('originalColor', node.style('background-color'));
    });

    cy.cxtmenu({
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
                    if (cy.elements().not(connectedNodesAndEdges).style('visibility') === 'hidden') {

                        cy.elements().not(connectedNodesAndEdges).show();
                        cy.elements().not(connectedNodesAndEdges).style('visibility', 'visible');

                    } else {
                        cy.elements().not(connectedNodesAndEdges).hide();
                        cy.elements().not(connectedNodesAndEdges).style('visibility', 'hidden');
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

    cy.cxtmenu({
        selector: 'core',
        commands: [
            {
                content: 'bg1',
                select: function(){
                    for (let node of cy.nodes()) {
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
                    for (let node of cy.nodes()) {
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
                    cy.elements().show();
                    cy.elements().style('visibility', 'visible');
                }
            }
        ]
    });
};

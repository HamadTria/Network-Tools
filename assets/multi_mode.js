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
                    'width': '50',
                    'height': '50'
                }
            },
            {
                selector: '.author',
                css: {
                    'background-color': 'lightblue',
                    'width': '100',
                    'height': '100'
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
                    'curve-style': 'bezier',
                    'target-arrow-shape': 'triangle'
                }
            },
            {
                selector: 'node:selected',
                css: {
                    // 'background-color': function(ele) {
                    //     return chroma(ele.data('originalColor')).darken(2).hex();
                    // },
                    'border-color': 'red',
                    'border-width': '4',
                }
            },
            {
                selector: 'edge:selected',
                css: {
                    'line-color': '#4c7dab'
                }
            }
        ],
        layout: {name: 'breadthfirst'},
        elements: {
            nodes: multi_mode_nodes,
            edges: multi_mode_edges
        }
    });

    // Store original colors for multi-mode graph
    cyMulti.nodes().forEach(node => {
        node.data('originalColor', node.style('background-color'));
    });
    
    // Delay one-mode and filter-mode graphs to wait for dropdown menu callback
    setTimeout(function() {
        var one_mode_nodes = JSON.parse(document.getElementById('one-mode-nodes').textContent);
        var one_mode_edges = JSON.parse(document.getElementById('one-mode-edges').textContent);
    
        // Create a new Cytoscape instance for one-mode graph
        var cyOne = window.cyOne = cytoscape({
            container: document.getElementById('one-mode-container'),
            ready: function(){},
            style: [
                {
                    selector: ".author", 
                    css : 
                    {
                        "background-color": "lightblue", 
                        "label": "data(label)", 
                        'color': '#fff',
                        "font-size": "20px",
                        'width': '100',
                        'height': '100'
                    }
                },
                {
                    selector: 'edge', 
                    css: 
                    {
                        "line-color": "#aaa", 
                        "font-size": "20px",
                        'curve-style': 'unbundled-bezier',
                        'color': '#fff',
                    }
                },
                {
                    selector: '.hasLabel',
                    css: {
                      'label': (ele) => {
                        if(ele.isEdge()) return ele.data('weight');         
                      }
                    }
                },
                {
                    selector: 'node:selected',
                    css: {
                        // 'background-color': function(ele) {
                        //     return chroma(ele.data('originalColor')).darken(2).hex();
                        // },
                        'border-color': 'red',
                        'border-width': '4',
                    }
                },
                {
                    selector: 'edge:selected',
                    css: {
                        'line-color': '#4c7dab'
                    }
                }
            ],
            layout: {name: 'cose'},
            elements: {
                nodes: one_mode_nodes,
                edges: one_mode_edges
            }
        });
    
        // Store original colors for one-mode graph
        cyOne.nodes().forEach(node => {
            node.data('originalColor', node.style('background-color'));
        });

        // Add label to edges
        cyOne.edges().forEach(edge => {
            edge.toggleClass('hasLabel');
        });

        var filter_mode_nodes = JSON.parse(document.getElementById('filter-mode-nodes').textContent);
        var filter_mode_edges = JSON.parse(document.getElementById('filter-mode-edges').textContent);

        // Create a new Cytoscape instance for filter-mode graph
        var cyFilter = window.cyFilter = cytoscape({
            container: document.getElementById('filter-mode-container'),
            ready: function(){},
            layout: {name: 'breadthfirst'},
            style: [
                {
                    selector: 'node',
                    css: {
                        'content': 'data(label)',
                        "font-size": "30px",
                        'background-color': 'lightblue',
                        'color': '#fff',
                        'shape': 'ellipse',
                        'width': '50',
                        'height': '50'
                    }
                },
                {
                    selector: '.author',
                    css: {
                        'background-color': 'lightblue',
                        'width': '100',
                        'height': '100'
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
                        'curve-style': 'bezier',
                        'target-arrow-shape': 'triangle'
                    }
                },
                {
                    selector: 'node:selected',
                    css: {
                        // 'background-color': function(ele) {
                        //     return chroma(ele.data('originalColor')).darken(2).hex();
                        // },
                        'border-color': 'red',
                        'border-width': '4',
                    }
                },
                {
                    selector: 'edge:selected',
                    css: {
                        'line-color': '#4c7dab'
                    }
                }
            ],
            elements: {
                nodes: filter_mode_nodes,
                edges: filter_mode_edges
            }
        });

        // Store original colors for filter-mode graph
        cyFilter.nodes().forEach(node => {
            node.data('originalColor', node.style('background-color'));
        });

        // Synchronize author node selection between the two graphs
        function syncSelection(cyFrom, cyTo) {
            cyFrom.on('select unselect', 'node', function(evt) {
                let node = evt.target;
                let correspondingNode = cyTo.getElementById(node.id());
                if (node.selected()) {
                    correspondingNode.select();
                } else {
                    correspondingNode.unselect();
                }
            });
        }

        // Apply synchronization
        syncSelection(cyMulti, cyOne);
        syncSelection(cyOne, cyMulti);
        syncSelection(cyMulti, cyFilter);
        syncSelection(cyFilter, cyMulti);

        // Synchronize node and edge selection between multi-mode and one-mode graphs
        function syncNodeAndEdgeSelection(cyMulti, cyOne) {
            // When a node is selected in multi-mode graph
            cyMulti.on('select', 'node', function(evt) {
                let node = evt.target;
                if (!node.hasClass('author')) {
                    cyOne.edges().forEach(edge => {
                        let sharedNodes = edge.data('shared');
                        if (sharedNodes && sharedNodes.includes(node.id())) {
                            edge.select();
                        }
                    });
                }
            });

            // When an edge is selected in one-mode graph
            cyOne.on('select', 'edge', function(evt) {
                let edge = evt.target;
                let sharedNodes = edge.data('shared');
                if (sharedNodes) {
                    sharedNodes.forEach(nodeId => {
                        let correspondingNode = cyMulti.getElementById(nodeId);
                        correspondingNode.select();
                    });
                }
            });

            // When an edge is unselected in one-mode graph
            cyOne.on('unselect', 'edge', function(evt) {
                let edge = evt.target;
                let sharedNodes = edge.data('shared');
                if (sharedNodes) {
                    sharedNodes.forEach(nodeId => {
                        let correspondingNode = cyMulti.getElementById(nodeId);
                        correspondingNode.unselect();
                    });
                }
            });

            // When a node is unselected in multi-mode graph
            cyMulti.on('unselect', 'node', function(evt) {
                let node = evt.target;
                if (!node.hasClass('author')) {
                    cyOne.edges().forEach(edge => {
                        let sharedNodes = edge.data('shared');
                        if (sharedNodes && sharedNodes.includes(node.id())) {
                            edge.unselect();
                        }
                    });
                }
            });
        }

        // Apply synchronization
        syncNodeAndEdgeSelection(cyMulti, cyOne);
        syncNodeAndEdgeSelection(cyMulti, cyFilter);

        // Define context menu commands
        const contextMenuCommands = [
            {
                content: 'change size',
                select: function(ele){
                    if (ele.style('width') === '100' || ele.style('width') === '100px'){
                        cyMulti.getElementById(ele.id()).animate({
                            style: { 'width': '50', 'height': '50' }
                        }, { duration: 500 });

                        cyOne.getElementById(ele.id()).animate({
                            style: { 'width': '50', 'height': '50' }
                        }, { duration: 500 });

                        cyFilter.getElementById(ele.id()).animate({
                            style: { 'width': '50', 'height': '50' }
                        }, { duration: 500 });
                    } else {
                        cyMulti.getElementById(ele.id()).animate({
                            style: { 'width': '100', 'height': '100' }
                        }, { duration: 500 });

                        cyOne.getElementById(ele.id()).animate({
                            style: { 'width': '100', 'height': '100' }
                        }, { duration: 500 });

                        cyFilter.getElementById(ele.id()).animate({
                            style: { 'width': '100', 'height': '100' }
                        }, { duration: 500 });
                    }
                }
            },
            {
                content: 'isolate node',
                select: function(ele){
                    let connectedNodesAndEdges = ele.connectedEdges().connectedNodes().union(ele.connectedEdges()).union(ele);
                    if (cyMulti.elements().not(connectedNodesAndEdges).style('visibility') === 'hidden' 
                        || cyOne.elements().not(connectedNodesAndEdges).style('visibility') === 'hidden'
                        || cyFilter.elements().not(connectedNodesAndEdges).style('visibility') === 'hidden'){

                        cyMulti.elements().not(connectedNodesAndEdges).show();
                        cyMulti.elements().not(connectedNodesAndEdges).style('visibility', 'visible');

                        cyOne.elements().not(connectedNodesAndEdges).show();
                        cyOne.elements().not(connectedNodesAndEdges).style('visibility', 'visible');

                        cyFilter.elements().not(connectedNodesAndEdges).show();
                        cyFilter.elements().not(connectedNodesAndEdges).style('visibility', 'visible');
                    } else {
                        cyMulti.elements().not(connectedNodesAndEdges).hide();
                        cyMulti.elements().not(connectedNodesAndEdges).style('visibility', 'hidden');

                        cyOne.elements().not(connectedNodesAndEdges).hide();
                        cyOne.elements().not(connectedNodesAndEdges).style('visibility', 'hidden');

                        cyFilter.elements().not(connectedNodesAndEdges).hide();
                        cyFilter.elements().not(connectedNodesAndEdges).style('visibility', 'hidden');
                    }
                }
            },
            {
                content: 'change shape',
                select: function(ele){
                    if (ele.style('shape') === 'square') {
                        cyMulti.getElementById(ele.id()).style('shape', 'ellipse');

                        cyOne.getElementById(ele.id()).style('shape', 'ellipse');

                        cyFilter.getElementById(ele.id()).style('shape', 'ellipse');
                    } else {
                        cyMulti.getElementById(ele.id()).style('shape', 'square');

                        cyOne.getElementById(ele.id()).style('shape', 'square');

                        cyFilter.getElementById(ele.id()).style('shape', 'square');
                    }
                }
            },
            {
                content: 'mark node',
                select: function(ele){
                    if (ele.style('background-color') === 'rgb(255,0,0)') {
                        cyMulti.getElementById(ele.id()).style('background-color', ele.data('originalColor'));

                        cyOne.getElementById(ele.id()).style('background-color', ele.data('originalColor'));

                        cyFilter.getElementById(ele.id()).style('background-color', ele.data('originalColor'));
                    } else {
                        cyMulti.getElementById(ele.id()).style('background-color', 'red');

                        cyOne.getElementById(ele.id()).style('background-color', 'red');

                        cyFilter.getElementById(ele.id()).style('background-color', 'red');
                    }
                }
            },
            {
                content: 'delete',
                select: function(ele){
                    cyMulti.getElementById(ele.id()).hide();
                    cyMulti.getElementById(ele.id()).style('visibility', 'hidden');

                    cyOne.getElementById(ele.id()).hide();
                    cyOne.getElementById(ele.id()).style('visibility', 'hidden');

                    cyFilter.getElementById(ele.id()).hide();
                    cyFilter.getElementById(ele.id()).style('visibility', 'hidden');
                }
            }
        ];

        // Apply context menu to all graphs
        cyMulti.cxtmenu({
            selector: 'node',
            commands: contextMenuCommands
        });

        cyOne.cxtmenu({
            selector: 'node',
            commands: contextMenuCommands
        });

        cyFilter.cxtmenu({
            selector: 'node',
            commands: contextMenuCommands
        });

        // Core context menu
        const coreContextMenuCommands = [
            {
                content: 'bring back nodes',
                select: function(){
                    cyMulti.nodes().show();
                    cyMulti.edges().show();
                    cyMulti.edges().style('visibility', 'visible');
                    cyMulti.nodes().style('visibility', 'visible');

                    cyOne.nodes().show();
                    cyOne.edges().show();
                    cyOne.edges().style('visibility', 'visible');
                    cyOne.nodes().style('visibility', 'visible');

                    cyFilter.nodes().show();
                    cyFilter.edges().show();
                    cyFilter.edges().style('visibility', 'visible');
                    cyFilter.nodes().style('visibility', 'visible');
                }
            },
            {
                content: 'reset colors',
                select: function(){
                    cyMulti.nodes().forEach(node => {
                        node.style('background-color', node.data('originalColor'));
                        cyOne.getElementById(node.id()).style('background-color', node.data('originalColor'));
                        cyFilter.getElementById(node.id()).style('background-color', node.data('originalColor'));
                    });
                }
            }
        ];

        // Apply core context menu to cyMulti and cyOne
        cyMulti.cxtmenu({
            selector: 'core',
            commands: coreContextMenuCommands
        });

        cyOne.cxtmenu({
            selector: 'core',
            commands: coreContextMenuCommands
        });

        cyFilter.cxtmenu({
            selector: 'core',
            commands: coreContextMenuCommands
        });

        const edgesContextMenuCommands = [
            {
                content: 'straighten edge',
                select: function(ele){
                    if (ele.style('curve-style') === 'unbundled-bezier') {
                        cyMulti.getElementById(ele.id()).style('curve-style', 'bezier');

                        cyOne.getElementById(ele.id()).style('curve-style', 'bezier');

                        cyFilter.getElementById(ele.id()).style('curve-style', 'bezier');
                    } else {
                        cyMulti.getElementById(ele.id()).style('curve-style', 'unbundled-bezier');

                        cyOne.getElementById(ele.id()).style('curve-style', 'unbundled-bezier');

                        cyFilter.getElementById(ele.id()).style('curve-style', 'unbundled-bezier');
                    }
                }
            },
            {
                content: 'show weight',
                select: function(ele){
                    cyOne.getElementById(ele.id()).toggleClass('hasLabel');
                    
                    cyMulti.getElementById(ele.id()).toggleClass('hasLabel');

                    cyFilter.getElementById(ele.id()).toggleClass('hasLabel');
                }
            }            
        ];

        // Apply context menu to all graphs
        cyMulti.cxtmenu({
            selector: 'edge',
            commands: edgesContextMenuCommands
        });

        cyOne.cxtmenu({
            selector: 'edge',
            commands: edgesContextMenuCommands
        });

        cyFilter.cxtmenu({
            selector: 'edge',
            commands: edgesContextMenuCommands
        });

    }, 1);
};